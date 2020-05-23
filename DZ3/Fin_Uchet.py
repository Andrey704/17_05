filename = 'salary.txt'
filename_anwer = 'Otvet.txt'
sum = 0
with open('salary.txt') as file:
    salary = file.readlines()
    for line in salary:
        sum += int(line.strip())

#print (sum)
#print (sum/(len(salary)))

with open(filename_anwer, 'w') as file:
    file.write('Sum of salary is ' + str(sum) + '\n')
    file.write('Average of salary is ' + str(sum/(len(salary))))


