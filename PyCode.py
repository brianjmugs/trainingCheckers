import os

#import the training text file, strip characters. Leave only the movements and weights. 
#Doing this so I can over time see which movements I'm missing and work on them throughout the month/year
files = os.listdir("data")
content = ""
trainingLogContent = ""
trainFile = os.listdir()
for i in files:
    #print(i)
    if ".txt" in i:
        i = "data/"+str(i)
        #print(i)
        f = open(i, 'r',encoding='utf8', errors='ignore')
        content = content + f.read()
        #print(i)
        f.close()

for i in trainFile:
    #print(i)
    if ".txt" in i:
        #print(i)
        f = open(i, 'r',encoding='utf8', errors='ignore')
        trainingLogContent = trainingLogContent + f.read()
        f.close()

def cleanData(cleanDataList):
    cleanDataList = cleanDataList.replace("- "," ")
    cleanDataList = cleanDataList.replace("-"," ")
    cleanDataList = cleanDataList.replace("[","")
    cleanDataList = cleanDataList.replace("]","")
    cleanDataList = cleanDataList.lower()
    cleanDataList = cleanDataList.strip()
    cleanDataList = cleanDataList.replace("ttb","toes to bar")
    cleanDataList = cleanDataList.replace("ctb","chest to bar")
    cleanDataList = cleanDataList.replace("press up","push ups")
    cleanDataList = cleanDataList.replace("snatch deadlift","sntchdeadlift")
    cleanDataList = cleanDataList.replace("db snatch", "dbsnatch")
    cleanDataList = cleanDataList.replace("dumbbell snatch", "dbSnatch")
    cleanDataList = cleanDataList.replace("db ","db")
    cleanDataList = cleanDataList.replace("wall ball","wallball")
    cleanDataList = cleanDataList.replace("weightlifting, strength + accessory", "")
    cleanDataList = cleanDataList.replace("rowing progression", "")
    cleanDataList = cleanDataList.replace("strict hspu + deadlift progression", "")
    cleanDataList = cleanDataList.replace("ring dip", "ring dips")
    cleanDataList = cleanDataList.replace("rmu", "ring muscle up")
    cleanDataList = cleanDataList.replace("bench", "bench press")
    cleanDataList = cleanDataList.replace("cal erg", "calorie erg")
    cleanDataList = cleanDataList.replace("kbs","kettlebell swing")
    cleanDataList = cleanDataList.replace("c2 bike","bike erg")
    cleanDataList = cleanDataList.replace("bar muscle-up","bar muscle up")
    cleanDataList = cleanDataList.replace("sit up","sit-up")
    cleanDataList = cleanDataList.replace("Devil's","devils")
    cleanDataList = cleanDataList.replace("devils","devil")
    cleanDataList = cleanDataList.replace("kb swing","kettlebell swing")
    return cleanDataList
contentOrig = cleanData(content)
content = cleanData(content)
trainingLogContentOrigi = cleanData(trainingLogContent)
trainingLogContent = cleanData(trainingLogContent)
#print("test1")
#def removeLine(word):
#    for item in content.split("\n"):
#        if word in item:
#            content = content.replace(item,"")

#removeLine("minutes to build")
#removeLine("window")  
#find unqiue words
unique_words = set(content.split(' '))

#movements looking to check 
movements = ['deadlift',"overhead squat","clean","back squat","front squat","power clean","chest to bar","burpee","jerk","hspu",'snatch',"row","bike erg","echo bike",
"pistol","strict press","push press","split jerk","push jerk","ski ","bar muscle up","ring muscle up","strict hspu", "wall walk","power snatch","squat snatch",
"pull up","double under","squat clean","toes to bar","ring dip","strict pull up","thruster","hang power snatch","push ups","rope climb","wallball","bench press",
"lunge","sotts press","sumo deadlift","snatch balance","ghd","devil press","sit-up", "run","d ball","sandbag","air squat","kettlebell swing"]

weightlfiting = [
'Back Pause Squat',
'Back Rack Lunges',
'Back Squat',
'Bench Press',
'Clean',
'Clean & Jerk',
'Clean & Jerk',
"Deadlift",
"Floor Press",
"Front Pause Squat",
"Front Rack Lunges",
"Front Squat",
"Hang Clean",
"Hang Power Clean",
"Hang Power Clean",
"Hang Squat Clean",
"Hang Squat Snatch",
"High Bar Back Squat",
"Jerk Balance",
"Jerk Dip",
"Overhead Squat",
"Power Clean",
"Power Clean & Jerk",
"Power Snatch",
"Push Jerk",
"Push Press",
"Romanian Deadlift",
"Seated Press",
"Shoulder Press",
"Snatch",
"Snatch Balance",
"Snatch Grip Deadlift",
"Snatch Grip Push Press",
"Sotts Press",
"Split Jerk",
"Squat Clean",
"Squat Jerk",
"Squat Pause Clean",
"Sumo Deadlift",
"Thruster"]
gymnastics = []

#return line with 
def moveToCheck(moveToCheck,list2):
    #print("test1-1")
    print(moveToCheck.upper())
    for item in list2.split("\n"):
        if moveToCheck in item:
            print (item.strip())
    print("\n")

#check through string and print count 
def checkFromList(moveList):
    resultList = []
    for i in movements:
        count = moveList.count(i.lower())
        resultList.append([count,i])
    return resultList

def printList(list):
    for i in list:
        print(i)

checkFromList(content)
#listByName = sorted(resultList, key=lambda x : x[1])
#for i in listByName:
#    movements.append(i)
##print(movementSort)
def trainingListPrint(file):
    with open('results/training.txt', 'w') as f:
        for i in resultList:
            f.write(str(i))


def printWeak3(list3,list2):
    print("3 Least Done")
    #print(list3[0:3])
    for i in list3[0:3]:
        #print("test1-1-1")
        moveToCheck(i[1],list2)


def runTest(formatted):
    #print(formatted[0:100])
    original = ""
    original = formatted
    #print(original[0:100])
    #print("Test1")
    formatted = checkFromList(formatted)
    #print("Test2", formatted[0:1],original[0:50])
    formatted.sort()
    #print("Test3")
    printWeak3(formatted,original)

print("Programming Data")
runTest(content)
print("Completed Data")
runTest(trainingLogContent)

