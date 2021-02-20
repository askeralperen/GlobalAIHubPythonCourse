# user: Alperen Aydın
# mail: aae.aydin@gmail.com

# HW2

import random as rnd

NameL = ["Cheddar Dogie","Charles Boyle","Amy Santiago","Terry Jeffords","Jake Peralta"] # manual input for fun names
GradesM = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]               #dummy matrix of grades
GradesL = []                      # empty list for all grades to be generated randomly to be placed inside GradesM matrix

MLen = len(GradesM)
mLen = len(GradesM[1])

while len(GradesL) != MLen*mLen:
  
  g = rnd.randint(0,100)          # random grade generation
  GradesL.append(g)               # entering random grades into grades list for further matrix filling

counter = 0 

for i in range(MLen):             # dummy matrix to real grades matrix step
  for j in range(mLen):
    GradesM[i][j] = GradesL[counter]
    counter += 1

"""print(len(GradesM)*len(GradesM[1]))
print(g)
print(GradesL)
print(GradesM)"""

# info named dict creation

Info = {}

for i in range(MLen):           # fill the dict
  Info[NameL[i]] = GradesM[i] 

# prints of first tasks
# print("Names: ",NameL)   
# print("Corresponding Grades: ",GradesM)
# print("Student Info Dict: ",Info)


# average detection and max finding tasks

AvGrades = []      # to be filled with names and avg grades

for i in range(MLen):
  Current_Avg = sum(GradesM[i])/len(GradesM[i])      # for the sake of clean coding
  z = [NameL[i], round(Current_Avg,2)]
  AvGrades.append(z)

# print("Names and Averages: ",AvGrades)

AvGrades.sort(key=lambda x: x[1], reverse=True)     # https://stackoverflow.com/a/4174956   # https://stackoverflow.com/a/4183540
# print("new",AvGrades)

print("Congrats", AvGrades[0][0], "with the score of", AvGrades[0][1])

# print(sum(GradesM[0])/3)
# z = [NameL[0],sum(GradesM[0])/3]

input()
