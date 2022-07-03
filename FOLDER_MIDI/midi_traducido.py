"""
This module implements some useful functions as an aside for the Synthesizer project of a programming course at the
Universidad de San Andrés, Argentina.
With it, standard midi files can be converted to the type of music score that the project needs.

@author Patricio Moreno
@institution Universidad de San Andrés
@date 2022-06-09 Thu 16:30:58 -0300
"""
from notes import notes_mapping

import argparse
import math
from typing import Optional, IO
import mido

def m2f(midi_note: int, freq_la4: int = 440) -> float:
    """
    Convierte una nota midi a la frecuencia correspondiente, basada en LA4 @ 440 Hz

    Tenga en cuenta que una nota midi es un valor entero en el rango [0, 127].
    Los valores fuera de ese rango darán respuestas sin significado real (en el campo MIDI).

    Parámetros
    ----------
    midi_nota: int
        El número que representa la nota midi.

    freq_la4 : int
        La frecuencia (en Hz) de un A4 sintonizado, típicamente 440 Hz.

    Devoluciones
    -------
        La frecuencia de la nota oscila entre aproximadamente 8 Hz y 12,5 kHz.
    """
    return (freq_la4 / 32) * (2 ** ((midi_note - 9) / 12))


def f2m(freq: float) -> int:
    """
    Convertir una frecuencia a la nota midi correspondiente

    Ten en cuenta que el rango de frecuencias válido para un archivo midi está entre 8 Hz y 12,5 kHz.
    Los valores fuera de ese rango pueden no tener sentido o generar un error (ValueError: error de dominio matemático).

    Parámetros
    ----------
    frecuencia: flotante
        La frecuencia (en Hz) a convertir

    Devoluciones
    -------
        La nota midi correspondiente
    """
    return 69 + round(12 * math.log2(freq / 440))


def freq2cypher(frequency: float, notes: dict[str, float]) -> Optional[str]:
    """
    Convierta una frecuencia a la cifra correspondiente en notación inglesa.

    Parámetros
    ----------
    frecuencia : flotante
        La frecuencia a convertir, en Hz.

    nota: dict[str, float]
        Un mapeo de la notación inglesa a la frecuencia y viceversa.

    Devoluciones
    -------
        La frecuencia representada usando notación inglesa (para un valor aproximado de la frecuencia) o Ninguno
    """
    for note, f in notes:
        if f - 1 < frequency < f + 1:
            return note
    return None


def convert_midi(ofile: str, midifile: str, tracks: Optional[list[int]] = None) -> None:
    """
    Convierta las pistas deseadas de un archivo midi en una partitura común basada en texto

    Parámetros
    ----------
    ofile : str
        La ruta al archivo de salida (texto)

    archivo_midi: cadena
        La ruta al archivo midi de entrada

    pistas: list[int] o None
        Si se proporciona, debe contener los números de las pistas para convertir

    Devoluciones
    -------
        Nada
    """
    midi = mido.MidiFile(midifile)
    if tracks is None or tracks == []:
        tracks = list(range(len(midi.tracks)))
    with open("Audio.txt", 'wt') as output:
        playing = {}
        t = 0
        for msg in midi:
            t += msg.time
            if msg.is_meta:
                pass
            elif msg.type == 'note_on' and msg.channel in tracks:
                freq = m2f(msg.note)
                score = freq2cypher(freq, notes_mapping)
                if score is None:
                    score = (None, freq)
                playing[msg.note] = (t, score)
            elif msg.type == 'note_off' and msg.channel in tracks:
                start, note = playing[msg.note]
                output.write(f"{start} {note} {t - start}\n")


def load_midi(filepath: str) -> IO:
    """
    Cargue un archivo midi en un objeto MidiFile

    Parámetros
    ----------
    ruta de archivo: str
        La ruta al archivo midi de entrada

    Devoluciones
    -------
        El objeto MidiFile
    """
    return mido.MidiFile(filepath)


def main() -> None:
    parser = argparse.ArgumentParser(description='Conversor de MIDI')
    parser.add_argument('-i', '--input', help='archivo MIDI')
    parser.add_argument('-o', '--output', help='archivo de salida')
    parser.add_argument('-t', '--tracks', help='tracks a convertir (CSV)')

    # ------------------------------------------------------------------
    # Parseo de argumentos
    # ------------------------------------------------------------------
    arg = parser.parse_args()

    if arg.tracks is not None:
        tracks = arg.tracks.replace(" ", "").split(",")
    else:
        tracks = None

    convert_midi(arg.output, arg.input, tracks)


if __name__ == '__main__':
    main()
