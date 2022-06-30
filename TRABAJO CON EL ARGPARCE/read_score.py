def music_debussy(filename):
    """
    Lee la partitura
    Parametros:
    ----------
        filename -> Archivo de la partitura
    Return:
        list_notes -> Lista con las notas ordenadas según la partitura
        list_t0_time -> Lista con el los tiempos de inicio de cada nota
        list_time -> Lista de la duración de cada nota
    """
    with open(filename,"r") as debussy:
        list_1 = []
        for line in debussy:
            line = line.strip()
            list_2 = line.split(" ")
            list_2 = tuple(list_2)
            list_1.append(list_2)
        list_t0_time = []
        list_notes = []
        list_time = []
        for one,two,three in list_1:
            list_t0_time.append(one)
            list_notes.append(two)
            list_time.append(three)
        return list_notes,list_time,list_t0_time