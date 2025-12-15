INPUT_PATH = "Day3/input.txt"

input_data = []
with open(INPUT_PATH, "r") as file:
    lines = file.readlines()
    for line in lines:
        input_data.append(line.strip())

count = 0
for i in input_data:
    pointer1 = 0
    current_max = 0
    val_max = (int(i[0]))*10 + int(i[1])

    for pointer2 in range(1,len(i)):
        current_max = (int(i[pointer1]))*10 + int(i[pointer2])
        if val_max < current_max:
            val_max = current_max

        if (pointer2 < (len(i)-1) and (int(i[pointer2]) > int(i[pointer1]))):
            pointer1 = pointer2

    count = count + val_max

print(count)