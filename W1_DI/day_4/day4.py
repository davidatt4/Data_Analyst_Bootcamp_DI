#functions
def say_hello(username,language):
    if language=="EN":
        print("Hello"+username)
    elif language=="FR":
        print("Bonjour"+username)
    else:
        print("This language is not supported"+language)

    
username="Rick"
language="FR"

say_hello()

#Default values
def say_hello(username,language):
    if language=="EN":
        print("Hello"+username)
    elif language=="FR":
        print("Bonjour"+username)
    else:
        print("This language is not supported"+language)
        