#KH 2nd args kwargs notes
'''def hello(name):
    return f"Hello {name}! You are {age}"

print(hello("Treyson", 19))
#the positinal arguemnt is the positional arguement
# OR

def hello(name):
    return f"Hello {name}! You are {age}"

print(hello(name = "Treyson", age = 19))
#This is keyword arguement

#OR


def hello(name="Hi", age = 29):
    return f"Hello {name}! You are {age}"

print(hello())
print(hello(name = "Treyson", age = 19))'''
#This is keyword arguement


def hello(last, *names):
    print(type(names))
    for name in names:
        print(f"Hello {name} {last}")

hello("Hugashu","me","ne","be","ve","ce","xe","ze")