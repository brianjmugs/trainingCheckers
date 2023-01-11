# The list of movements
movement_list = []

# A dictionary to keep track of the number of times each movement has been done
movement_count = {movement: 0 for movement in movement_list}



with open('TrainingLog.txt', 'r') as file:
    for line in file:
        elements = line.strip().split(',')
        if len(elements) == 3:
            date, movement, weight = elements
            if movement not in movement_list:
                movement_list.append(movement)
                movement_count[movement] = 0
            movement_count[movement] += 1
        else:
            print(f"Line {line}")

least_3_movements = [(movement, count) for movement, count in sorted(movement_count.items(), key=lambda item: item[1])][:3]
print("The 3 least done movements and their count:", least_3_movements)
