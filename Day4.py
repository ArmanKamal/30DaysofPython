### Conditionals & Control Flow ###
state = True

if state:
    print('Hi There')
else :
    print('Nothing')


print(str(True).lower() == 'true')


abc = [1,2,3,4,5]
abc_sq = []
for num in abc:
    new_number = num**2
    abc_sq.append(new_number)
print(abc_sq)

## Using if else to find even and odd number ##
is_even = []
is_odd = []

for num in abc_sq:
    if num % 2 == 0:
        is_even.append(num)
    else:
        is_odd.append(num)
print(f'Even numbers{is_even}')
print(f'Odd numbers{is_odd}')


### if else elif for showing grades according to user number ###

number = 40

if number>=80:
    print('Congrats you got a++')
elif number >=60:
    print('You got B+')
else:
    print('So low number D+')


#### While Loop ###

x = 10
i = 0
while i<x:
    print(i)
    i = i+1
### You can use break function for stopping a loop ##
