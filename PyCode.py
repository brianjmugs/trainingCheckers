#import the training text file, strip characters. Leave only the movements and weights. 
#Doing this so I can over time see which movements I'm missing and work on them throughout the month/year
f = open('7th Training.txt', 'r')
content = f.read()
content = content.replace("- ","")
content = content.replace("[","")
content = content.replace("]","")

    
