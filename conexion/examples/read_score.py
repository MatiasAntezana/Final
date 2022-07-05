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
        list_org = []
        for one,two,three in list_1:
            one = float(one)
            list_t0_time.append(one)
            list_notes.append(two)
            list_time.append(three)
        
        return list_notes,list_time,list_t0_time

def organization(filename):
    """
    Function that reads a file and separates it into a dictionary.
    Parameters:
    ----------
        filename -> Sheet music file
    Return:
        separate:list -> List of lists with the notes, the duration and the initial times
    """
    with open(filename,"r") as debussy:
        list_1 = []
        list_org = []
        for line in debussy:
            line = line.strip()
            list_2 = line.split(" ")
            list_2 = tuple(list_2)
            list_1.append(list_2)

        for one,two,three in list_1:
            empty_list = []
            one = float(one)
            three = float(three)
            empty_list.append(one)
            empty_list.append(two)
            empty_list.append(three)
            empty_list = tuple(empty_list)
            list_org.append(empty_list)
        
        dic = {}
        for i in range(1,len(list_org)):
            dic[i] = list_org[i]

        separate = org_dic(dic)
        return separate

def org_dic(dic):
    """
    Function that organizes the dictionary according to the initial times of each note.
    Parameters:
    ----------
        dic:dict -> Dictionary with the initial times, the notes and the duration of each note
    Return:
        separate:list -> List of lists with the notes, the duration and the initial times
    """
    suf = 1
    while suf != len(dic):
        for i in range(suf,len(dic)+1):
            if dic[i][0] < dic[suf][0]:
                dic[suf], dic[i] = dic[i], dic[suf]
        suf += 1
    separate = separate_list(dic)
    return separate
    

def separate_list (dic):
    """
    Function to sort the notes according to the order in which they sound.
    Parameters:
    ----------
        dic:dict -> Dictionary that will sort
    Return:
        notes:list -> Correctly sorted notes
        list_duration:list -> List the duration of the notes
        list_time:list -> List of the initial beats of each note, in order
    """
    list_time = []
    notes = []
    list_duration = []
    for i in range(1,len(dic)+1):
        time_inital = dic[i][0] 
        note = dic[i][1]
        duration = dic[i][2]
        list_time.append(time_inital)
        notes.append(note)
        list_duration.append(duration)
    
    return notes,list_duration,list_time
