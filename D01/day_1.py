    
with open("input_day_1.txt") as f:
    report = f.read().splitlines()
    report = [int(i) for i in report]


def part_One():
    count = 0 
    for i in range (1,len(report)):
        if report[i] > report[i-1]:
            count += 1
    return count

def part_two():
    count = 0 
    for i in range(3, len(report)):
        previus = report[i-1] + report[i-2] + report[i-3]
        new = report[i-1] + report[i-2] + report[i] 
        if new > previus:
            count += 1
    return count

print(part_One())
print(part_two())
