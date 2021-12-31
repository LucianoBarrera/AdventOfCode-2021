with open("./D02/input.txt") as f:
    input = f.read().splitlines()
    formated = []
    for i in input:
        x = i.split()
        formated.append([x[0],int(x[1])])

def part_One():
    horizontal = 0
    depth = 0
    for i in formated:
        if i[0] == "forward":
            horizontal += i[1]
        elif i[0] == "down":
            depth += i[1]
        else:
            depth -= i[1]
    return (horizontal*depth)

def part_Two():
    horizontal = 0
    depth = 0
    aim = 0
    for i in formated:
        if i[0] == "forward":
            horizontal += i[1]
            depth += (aim*i[1])
        elif i[0] == "down":
            aim += i[1]
        else:
            aim -= i[1]
    return (horizontal*depth)

print(part_One())
print(part_Two())