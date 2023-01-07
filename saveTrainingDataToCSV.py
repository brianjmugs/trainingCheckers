import csv

def add_entry(date, movement, weight):
  with open('TrainingLog.txt', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow([date, movement, weight])

date = input("Enter date: ")
while True:
  movement = input("Enter movement: ")
  weight = input("Enter weight: ")
  add_entry(date, movement, weight)
  another = input("Add another entry for this date? (y/n)")
  if another.lower() == 'n':
    break