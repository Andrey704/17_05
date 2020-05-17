filename = 'data2.txt'
new_data = []
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        print(int(line)**2)
        new_data.append(int(line))

print(lines)
print(new_data)