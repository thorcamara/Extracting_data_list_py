values = []
while True:
    values.append(int(input('Type a number: ')))
    answer = str(input('Do you want to continue? [\033[1;32mY\033[m/\033[1;31mN\033[m] '))
    if answer in 'Nn':
        break
print('-=' * 30)
print(f'You entered \033[4;33m{len(values)}\033[m elements')
values.sort(reverse=True)
print(f'The values in \033[4;31mdescending\033[m order are \033[4;33m{values}\033[m')
if 5 in values:
    print('Number \033[4;32m5\033[m is on the List!')
else:
    print('The number \033[4;31m5\033[m was not found on the List!')
