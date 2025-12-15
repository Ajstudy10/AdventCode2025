INPUT_PATH = "Day2/input.txt"

with open(INPUT_PATH, "r") as file:
    lines = file.readlines()
    lines=lines[0]
    lines = lines.split(',')
invalid_ids = []

for i in lines:
    b,e = i.split('-')
    b,e = int(b),int(e)
    for i in range(b,(e+1)):
        i = str(i)
        for j in range(1,((len(i)//2)+1)):
            segment = i[:j]
            repeated_string = segment * int((len(i)/j))
            if(repeated_string == i):
                invalid_ids.append(i)
                break

sum_of_ids = 0

for i in invalid_ids:
    sum_of_ids = sum_of_ids + int(i)

print(sum_of_ids)
4174379265