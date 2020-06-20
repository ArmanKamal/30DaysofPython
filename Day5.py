## Formatted String ###

# name='Arman'

# print(f"hello{name} this is awesome")

### Without format ###
template = """ Hello there,
...{name} this is awesome """

print(template)

### With Format ###

print(template.format(name='Arman'))


### Now if want \\ how we can print that in a string ###

print("http::\\\\gmail.com")


### If you want to use {} in format  ###
template = "{name} you are not cool like I thought you would be {{}} ".format(name='Aria')
print(template)
pi=3.141523

print(format(pi,".2f"))


