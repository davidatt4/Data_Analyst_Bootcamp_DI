#opening a file
#old fashion way

#f=open("example.txt"):
#f.readlines()
#f.close()

with open('example.txt',encoding='utf-8',mode='r')as f:
    my_line='HELLO TESTING'
    my_line+=f.read()
    print(my_line)
