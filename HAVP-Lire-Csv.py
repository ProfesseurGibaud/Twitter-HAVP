import csv
import os


def dossier():
    os.chdir("Google Drive\Python\Twitter HAVP\Twitter-HAVP")


Dico = {}    
with open("liste.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader :
        print(dict(row))
    