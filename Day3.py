## Iteration ##

my_list = [1,2,3,4,5]

### There are many types of Loop ###
### Such as FOR, While,Do While ###

for x in my_list:  ## x is refering to individual element of my_list
    print(x)

for i in "abc":
    print(i)  ### print a then b then c

### Python has to be indented perfectly otherwise this will give error



### THis will give you an error beacuse int obj is not iterable ###

# for x in 10:
#     print(x)

### F

for x in range(10):
    print(x)

for x in range(0,10):
    print(x)     


### Iterate through list of dictonaries ### 

user_1 = {'username': 'Arman', 'id':2}
user_2 = {'username': 'Justin', 'id':31}

my_user = [user_1,user_2]

user_2['email'] = 'abc@abc.com'


for user in my_user:
    print(user)
    print(user['username'])
    print(user['id'])


for user in my_user:
    if 'email' in user:
        print(user['email'])

selected_user = {}
my_user_lookup = 2

### Looking for a specific user with any given id and set the value to an empty dictonary


for user in my_user:
    if 'id' in user:
        if user['id'] == my_user_lookup:
            selected_user = user

print(selected_user)


### Looking for a specific user with any given id by looping through number 

for x in range(0,10):
    for user in my_user:
        if user['id'] == x:
            print(user)

