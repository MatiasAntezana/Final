import sys
from read_score import organization
from note import XyloNote
import argparse

def notes_for_xylo ():
    list_t = organization("alladin_note_modi.txt")
    list_1 = list_t[0]
    list_2 = list_t[2]
    list_new = []
    i = 0
    for notes in list_1:
        new = XyloNote(notes,list_2[i],90)
        i += 1
        list_new.append(new)
    print(len(list_new))
    print(list_new)

if __name__ == "__main__":
    notes_for_xylo()
