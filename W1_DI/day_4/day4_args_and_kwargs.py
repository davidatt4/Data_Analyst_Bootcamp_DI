def print_names(*args):
    for name in args:
        print(name)

#args= *
print_names('David')

#kwargs =**

def print_info(**kwargs):
    print(kwargs['adress'])

print_info(adress=(5,7),score=[25,47,899])


def gamer_info(*args,**kwargs):
    print(max(args))
    print(kwargs)

gamer_info(150,123,544,534,783,name='John',last_name='Doe',age='23')
