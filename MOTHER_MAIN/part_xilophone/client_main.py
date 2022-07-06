#/usr/bin/env python

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote

def filter(notes_times,ip_xylophone:str):
    """
    Function will allow us to pass the notes to the metalofon once we have it (if we have the ip).
    Parameters:
    ----------
        notes_times:list -> List with the notes and the initial times
        ip_xylophone:str -> IP address of the xylophone
    """
    client = XyloClient(host=ip_xylophone, port=8080)
    client.load(notes_times)
    client.play()

def create_notes_for_xylophone(list_final):
    """
    Function that will go through each element of the list that we pass to it to return a list with: notes, initial times and speed.
    Parameters:
    ----------
        list_final:list -> List with the notes and the initial times of a score
    
    Return:
        notes_times:list -> List with the notes and the initial times
    """
    notes_times = []
    for element in list_final:
        notes_times.append(XyloNote(element[0],element[1],90))
    return notes_times      