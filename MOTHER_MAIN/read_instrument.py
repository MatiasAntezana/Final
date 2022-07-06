def separate_tuples_values_for3(element):
    """
    Function will return in a list the type of attack, sustain and decay, along with their values (in case attack, sustain and decay have 3 values ​​as parameter).
    Parametros:
    ----------
        element:list -> List with the lines of the attack, sustain and decay file of the instrument
    
    Return:
        list_final:list -> List with the type of attack, sustain and decay, with their values
    """
    type_function = element[0]
    type_function = type_function.lower()
    num1 = element[1]
    num1 = float(num1)
    num2 = element[2]
    num2 = float(num2)
    num3 = element[3]
    num3 = float(num3)
    list_final = []
    list_final.append(type_function)
    list_final.append(num1)
    list_final.append(num2)
    list_final.append(num3)
    return list_final

def separate_tuples_values_for2 (element):
    """
    Function will return in a list the type of attack, sustain and decay, along with their values (in case attack, sustain and decay have 2 values ​​as parameter).
    Parametros:
    ----------
        element:list -> List with the lines of the attack, sustain and decay file of the instrument
    
    Return:
        list_final:list -> List with the type of attack, sustain and decay, with their values
    """
    type_function = element[0]
    type_function = type_function.lower()
    num1 = element[1]
    num1 = float(num1)
    num2 = element[2]
    num2 = float(num2)
    list_final = []
    list_final.append(type_function)
    list_final.append(num1)
    list_final.append(num2)
    return list_final

def atack_sust_decay_separator(number,mem):
    """
    Función que separará el ataque, sostenido o decaimiento, dependiendo el que haya
    Parametros:
    ----------
        number:int -> Numero de la cantidad de armonicos que hay (especificado en la primera linea del archivo del piano)
        mem -> Variable en donde se guarda el archivo abierto
    Return:
        list_func:list -> List of tuples with the types of attacks, sustains and decays
    """
    list_new = []
    for line in mem:
        line = line.strip()
        list_2 = line.split(" ")
        list_2 = list(list_2)
        if "CONSTANT" == list_2[0]:
            list_2.append(0)
        list_2[1] = float(list_2[1])
        list_2 = tuple(list_2)
        list_new.append(list_2)

    list_func = []
    for element in list_new:
        if len(element) == 4:
            result_element = separate_tuples_values_for3(element)
            result_element = tuple(result_element)
            list_func.append(result_element)

        elif len(element) == 3:
            result_element = separate_tuples_values_for2(element)
            result_element = tuple(result_element)
            list_func.append(result_element)


        elif len(element) == 2:
            list_empty = []
            type_function = element[0]
            type_function = type_function.lower()
            num = element[1]
            num = float(num)
            list_empty.append(type_function)
            list_empty.append(num)
            list_empty = tuple(list_empty)
            list_func.append(list_empty)
    return list_func
    #return list_type_function,list_num

def harmonics_separator (number,mem):
    """
    Función que separa el numero de los armonicos.
    Parametros:
    ----------
        number:int -> Numero de la cantidad de armonicos que hay (especificado en la primera linea del archivo del piano)
        mem -> Variable en donde se guarda el archivo abierto
    
    Return:
        list_numbers,list_harmonics,result2 -> Tuple of lists of the numbers next to the harmonics, of the harmonics and of the types of attack, sustain and decay
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
    Function to read the instrumen file.txt 
  
    Parametros:
    ----------
        filename -> Nombre del archivo del instrumento
    
    Return:
        result:tuple -> The result of calling the harmonics_separator function (tuple of lists)
    """
    with open (filename,"r") as mem:
        for line in mem:
            line = line.strip()
            line = int(line)
            break
        result = harmonics_separator(line,mem)
        return result