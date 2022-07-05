def atack_sust_decay_separator(number,mem):
    """
    Función que separará el ataque, sostenido o decaimiento, dependiendo el que haya
    Parametros:
    ----------
        number:int -> Numero de la cantidad de armonicos que hay (especificado en la primera linea del archivo del piano)
        mem -> Variable en donde se guarda el archivo abierto
    Return:

    """
    list_new = []
    conta = 1
    for line in mem:
        line = line.strip()
        list_2 = line.split(" ")
        list_2 = list(list_2)
        if "CONSTANT" == list_2[0]:
            list_2.append(0)
        list_2[1] = float(list_2[1])
        list_2 = tuple(list_2)
        if number > conta:
            list_new.append(list_2)
        conta += 1
    list_type_function = []
    list_num = []
    for type_function,num in list_new:
        type_function = type_function.lower()
        list_type_function.append(type_function)
        list_num.append(num)
    return list_type_function,list_num

def harmonics_separator (number,mem):
    """
    Función que separa el numero de los armonicos.
    Parametros:
    ----------
        number:int -> Numero de la cantidad de armonicos que hay (especificado en la primera linea del archivo del piano)
        mem -> Variable en donde se guarda el archivo abierto
    
    Return:

    """
    list_new = []
    conta = 1
    for line in mem:
        line = line.strip()
        list_2 = line.split(" ")
        list_2 = tuple(list_2)
        list_new.append(list_2)
        if conta >= number:
            break
        conta += 1
    list_numbers = []
    list_harmonics = []
    for num,harmonics in list_new:
        num = int(num)
        harmonics = float(harmonics)
        list_numbers.append(num)
        list_harmonics.append(harmonics)

    result2 = atack_sust_decay_separator(number,mem)
    return list_numbers,list_harmonics,result2

def read_instru (filename):
    """
    Función que leé el archivo del instrumento.
    Parametros:
    ----------
        filename -> Nombre del archivo del instrumento
    
    Return:

    """
    with open (filename,"r") as mem:
        for line in mem:
            line = line.strip()
            line = int(line)
            break
        result = harmonics_separator(line,mem)
        return result