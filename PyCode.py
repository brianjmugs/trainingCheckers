import os

#import the training text file, strip characters. Leave only the movements and weights. 
#Doing this so I can over time see which movements I'm missing and work on them throughout the month/year
files = os.listdir()
content = ""
for i in files:
    if ".txt" in i:
        f = open(i, 'r',encoding='utf8', errors='ignore')
        content = content + f.read()
        print(i)
        f.close()
content = content.replace("- ","")
content = content.replace("[","")
content = content.replace("]","")
content = content.lower()
content = content.strip()
content = content.replace("ttb","toes to bar")
content = content.replace("ctb","chest to bar")
content = content.replace("press up","push-ups")
content = content.replace("snatch deadlift","sntchdeadlift")
content = content.replace("db snatch", "dbsnatch")
content = content.replace("dumbbell snatch", "dbSnatch")
content = content.replace("db ","db")
content = content.replace("wall ball","wallball")
content = content.replace("weightlifting, strength + accessory", "")
content = content.replace("rowing progression", "")
content = content.replace("strict hspu + deadlift progression", "")
content = content.replace("ring dip", "ring dips")

def removeLine(word):
    for item in content.split("\n"):
        if word in item:
            content = content.replace(item,"")

removeLine("minutes to build")
removeLine("window")  
#find unqiue words
unique_words = set(content.split(' '))

#movements looking to check 
movements = ['deadlift ',"overhead squats","clean","back squat","front squat","power clean","chest to bar","burpee","jerk","hspu",'snatch ',"row","bike erg","echo bike",
"pistols","strict press","push press","split jerk","push jerk","ski","bar muscle up","ring muscle up","strict hspu", "wall walk","power snatch","squat snatch",
"pull ups","double under","squat clean","toes to bar","ring dips","strict pull up","thrusters","hang power snatch","push-ups","rope climb","wallball","chest to bar","ring dip"]

weightlfiting = []
gymnastics = []

#return line with 
#for i in movements:
#    print(i.upper())
#    for item in content.split("\n"):
#        if i in item:
#            print (item.strip())
#    print("\n")

#check through string and print count 
resultList = []
for i in movements:
    count = content.count(i)
    resultList.append([count,i])

resultList.sort()
def printList(list):
    for i in list:
        print(i)

movementSort = ""
#listByName = sorted(resultList, key=lambda x : x[1])
#for i in listByName:
#    movements.append(i)
##print(movementSort)

#printList(resultList)