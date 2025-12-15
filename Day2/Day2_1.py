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
        if(len(i) % 2 == 0):
            max_len = len(i)//2
            if(i[:(max_len)]==i[(max_len):]):
                invalid_ids.append(i)

sum_of_ids = 0

for i in invalid_ids:
    sum_of_ids = sum_of_ids + int(i)

print(sum_of_ids)
# 18371837

# 43204932

# 43204321