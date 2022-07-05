def read_instru (filename):
    with open (filename,"r") as mem:
        list_1 = []
        for line in mem:
            line = line.strip()
            list_2 = line.split(" ")
            list_2 = tuple(list_2)
            list_1.append(list_2)
        
