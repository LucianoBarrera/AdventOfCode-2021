with open("./D03/input.txt") as f:
    input = f.read().splitlines()
gama  = [0] * 12
epsilon =  [0] * 12
position = 0

for i in input:
    for x in i:
        if int(x) == 1:
            gama[position] += 1
        else:
            gama[position] -= 1
        position += 1
    position = 0


for i in range (12):
    if gama[i] > 0:
        gama[i] = 1
        epsilon[i] = 0
    else:
        gama[i] = 0
        epsilon[i] = 1


dec_gama = 0
dec_epsilon = 0
for i in range(12):
    dec_epsilon += (int(epsilon[11-i]) * pow(2,i))
    dec_gama += (int(gama[11-i]) * pow(2,i))

print(dec_epsilon)
print(dec_gama)

print(dec_gama*dec_epsilon)
