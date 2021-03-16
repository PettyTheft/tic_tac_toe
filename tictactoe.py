o = 'o'
x = 'x'
r1c1 = '_'
r1c2 = '_'
r1c3 = '_'
r2c1 = '_'
r2c2 = '_'
r2c3 = '_'
r3c1 = '_'
r3c2 = '_'
r3c3 = '_'
z = 1
row1 = [r1c1,r1c2,r1c3]
row2 = [r2c1,r2c2,r2c3]
row3 = [r3c1,r3c2,r3c3]

def tictacboard():
    print row1 
    print row2
    print row3

def boardchangerx():
    print ('Format your response with rows and then columns i.e. r1c1')
    changex = (input("(X) which tile do you want to change?"))
    global r1c1
    global o
    if changex is r1c1:
        if r1c1 is not o:
            row1[0] = 'X'
    if changex is r1c2:
        if r1c2 is not o:
            row1[1] = 'X'
    if changex is r1c3:
        if r1c3 is not o:
            row1[2] = 'X'

while z is 1:
    tictacboard()
    boardchangerx()