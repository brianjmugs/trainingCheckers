#import the training text file, strip characters. Leave only the movements and weights. 
#Doing this so I can over time see which movements I'm missing and work on them throughout the month/year
f = open('7th Training.txt', 'r')
content = f.read()
content = content.replace("- ","")
content = content.replace("[","")
content = content.replace("]","")
content = content.lower()
content = content.strip()

#find unqiue words
unique_words = set(content.split(' '))
print(unique_words)

#movements looking to check 
movements = ['deadlift',"overhead squat","clean","back squat","front squat","power clean","ctb","burpee", "clean and jerk","jerk","hspu",'snatch',"row","bike erg","echo bike",
"pistols","ttb","strict press","push press","split jerk","push jerk","ski","bar muscle up","ring muscle up","strict hspu", "wall walk","power snatch","squat snatch",
"pull ups","double under"]

#check through string and print count 
resultList = []
for i in movements:
    count = content.count(i)
    print(i,count)
    resultList.append([count,i])

print(resultList)
resultList.sort(reverse=True)
print(resultList)
for i in resultList:
    print(i)