# Nakul Thureja 
# ROLL NO :- 2020528 
# BRANCH  :- CSE
# AI Assignment 5 

import nltk
import pyswip

prolog = pyswip.Prolog()
prolog.consult("NakulThureja_2020528_A1.pl")

f = open("facts.txt", "w")
print("Elective Advisory System (NLP)")
sen1 = input("Enter your name and branch\n").lower()
tokens = nltk.word_tokenize(sen1)
branch = 1
for token in tokens:
    if (token == "cse"):
        branch = 1
        break
    elif (token == "csam"):
        branch = 2
        break
    elif (token == "csai"):
        branch = 3
        break
    elif (token == "csd"):
        branch = 4
        break
    elif (token == "csb"):
        branch = 5
        break
    elif (token == "csss"):
        branch = 6
        break
    elif (token == "ece"):
        branch = 7
        break

f.write("branches("+str(branch)+").\n")

sem = 1
sen2 = input("\nWhat semester are you in?\n")
new_sen2 = nltk.word_tokenize(sen2)
sem_dict = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "6th": 6, "7th": 7, "8th": 8,
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eight": 8
}

for word in new_sen2:
    if (word.lower() in sem_dict):
        sem = sem_dict[word.lower()]

f.write("sems("+str(sem)+").\n")

sen3 = input("\nWhat is your current grade?\n")
new_sen3 = nltk.word_tokenize(sen3)
grade_dict = {
    "0": 6, "1": 6, "2": 6, "3": 6, "4": 6, "5": 6, "6": 5, "7": 4, "8": 3, "9": 2, "10": 1,
    "good": 3, "bad": 6, "average": 5, "excellent": 1, "poor": 6
}
grade = 3
for word in new_sen3:
    if (word.lower() in grade_dict):
        grade = grade_dict[word.lower()]

f.write("grades("+str(grade)+").\n")

print("\nInterests")
flag = True
if(flag):
  sen4 = input("Are you interested in the field of Machine Learning / Artificial Intelligence\n")
  sen4 = sen4.lower()
  if ('y' in sen4 and flag):
      f.write("interests(1).\n")
      flag = False

if(flag):
  sen4 = input("Are you interested in the field of Cyber Secuirty / Networks\n")
  sen4 = sen4.lower()
  if ('y' in sen4 ):
      f.write("interests(2).\n")
      flag = False

if(flag):
  sen4 = input("Are you interested in the field of Computer Architechture\n")
  sen4 = sen4.lower()
  if ('y' in sen4 and flag):
      f.write("interests(3).\n")
      flag = False

if(flag):
  sen4 = input("Are you interested in the field of UI-UX Designer\n")
  sen4 = sen4.lower()
  if ('y' in sen4 and flag):
      f.write("interests(4).\n")
      flag = False

if(flag):
  sen4 = input("Are you interested in the field of Computational Biology\n")
  sen4 = sen4.lower()
  if ('y' in sen4 and flag):
      f.write("interests(5).\n")
      flag = False

if(flag):
  sen4 = input("Are you interested in the field of Electronics\n")
  sen4 = sen4.lower()
  if ('y' in sen4 and flag):
      f.write("interests(6).\n")
      flag = False

if(flag):
  sen4 = input("Are you interested in the field of Mathematics and Computing\n")
  sen4 = sen4.lower()
  if ('y' in sen4 and flag):
      f.write("interests(7).\n")
      flag = False

if(flag):
  print("You aren't interested in any fields, system encourages you to take courses in the field of AI/ML as it is growing field\n")
  f.write("interests(1).\n")
  flag = False

f.close()
query = list(prolog.query("begin(X)."))
print(query[0])