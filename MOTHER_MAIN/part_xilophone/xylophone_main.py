from client import create_notes_for_xylophone,filter
import argparse
import sys
from read_score import organization

parser = argparse.ArgumentParser()
parser.add_argument("-s",default = "example_debussy-clair-de-lune.txt",help="Enter the score file")
parser.add_argument("-ip",default = "10.42.0.1",help="Please enter an ip for the metalofon")
args = parser.parse_args()
score_music = args.s
ip = args.ip

list_new = organization(score_music)
list_note = list_new[0]
list_time0 = list_new[1]
list_final = []
for i in range(0,len(list_note)+1):
    list_emply = []
    note = list_note[i]
    time = list_time0[i]
    list_emply.append(note)
    list_emply.append(time)
    list_emply = tuple(list_emply)
    list_final.append(list_emply)
notes = create_notes_for_xylophone(list_final)
filter(notes,args.ip)



