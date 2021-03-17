o = 'o'
x = 'x'
win = 2
r1c1 = 'a'
r1c2 = 'b'
r1c3 = 'c'
r2c1 = 'd'
r2c2 = 'e'
r2c3 = 'f'
r3c1 = 'g'
r3c2 = 'h'
r3c3 = 'i'
z = 1
c = ""
b = ""
row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']

def tictacboard():
    if win != 1:
        print row1 
        print row2
        print row3

def boardchangerx():
    if win != 1:
        print ('Format your response with rows and then columns i.e. r1c1')
        changex = (input("(X) which tile do you want to change?"))
        if changex == r1c1:
            if row1[0] != 'O':
                row1[0] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r1c2:
            if row1[1] != 'O':
                row1[1] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r1c3:
            if row1[2] != 'O':
                row1[2] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r2c1:
            if row2[0] != 'O':
                row2[0] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r2c2:
            if row2[1] != 'O':
                row2[1] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r2c3:
            if row2[2] != 'O':
                row2[2] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r3c1:
            if row3[0] != 'O':
                row3[0] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r3c2:
            if row3[1] != 'O':
                row3[1] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))
        if changex == r3c3:
            if row3[2] != 'O':
                row3[2] = 'X'
            else:
                changex = (input("(X) which tile do you want to change?"))

def boardchangero():
    if win != 1:
        print ('Format your response with rows and then columns i.e. r1c1')
        changeo = (input("(O) which tile do you want to change?"))
        if changeo == r1c1:
            if row1[0] != 'X':
                row1[0] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r1c2:
            if row1[1] != 'X':
                row1[1] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r1c3:
            if row1[2] != 'X':
                row1[2] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r2c1:
            if row2[0] != 'X':
                row2[0] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r2c2:
            if row2[1] != 'X':
                row2[1] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r2c3:
            if row2[2] != 'X':
                row2[2] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r3c1:
            if row3[0] != 'X':
                row3[0] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r3c2:
            if row3[1] != 'X':
                row3[1] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))
        if changeo == r3c3:
            if row3[2] != 'X':
                row3[2] = 'O'
            else:
                changeo = (input("(O) which tile do you want to change?"))

def winchecker():
    global win
    if win != 1:
        if row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row1[2] == 'X' and row2[1] == 'X' and row3[0] == 'X':
            print ('X wins!')
            celebrationx()
            win = 1
        elif row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row3[0] == 'O' and row3[1] == 'O' and row3[2] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row1[2] == 'O' and row2[1] == 'O' and row3[0] == 'O':
            print ('O wins!')
            celebrationo()
            win = 1
        elif row1[0] != '-':
            if row1[1] != '_':
                if row1[2] != '_':
                    if row2[0] != '_':
                        if row2[1] != '_':
                            if row2[2] != '_':
                                if row3[0] != '_':
                                    if row3[1] != '_':
                                        if row3[2] != '_':
                                            print ('Tie!')
                                            celebrationtie()
                                            win = 1
        
def celebrationx():                                                            
    print ('                     @@@%    @@@                       ')
    print ('                      @@@ .@@@                         ')
    print ('                       .@@@@                           ')
    print ('                       @@@@@%                          ')
    print ('                     &@@@  @@@                         ')
    print ('                    @@@     ,@@@                       ')
    print ('                                                       ')
    print ('                                                       ')
    print ('                                                       ')
    print ('@@@    @@@    @@@  @@@                         @@@     ')
    print (',@@    @@@@   *@@                              @@@     ')
    print ('@@@  @@*@@@  @@@   @@@  %@@@@@@@@   @@@@@@@@   @@@     ')
    print ('  @@*@@@  @@%&@@   @@@  %@@    @@*  @@@@@&     ,@%     ')
    print ('  @@@@@    @@@@,   @@@  %@@    @@*       @@@,   ,      ')
    print ('   @@@*    &@@@    @@@  %@@    @@*  &@@@@@@#   @@@     ')
    print ('                                                       ')
                                                            
def celebrationo():                                                               
    print ('                          @@@@@@@/                         ')
    print ('                       &@@@     @@@@                       ')
    print ('                      #@@@        @@@                      ')
    print ('                      @@@(        @@@                      ')
    print ('                       @@@       @@@@                      ')
    print ('                        @@@@@@@@@@@.                       ')
    print ('                             .                             ')
    print ('                                                           ')
    print ('                                                           ')
    print ('                                                           ')
    print (' ...     ....     ... ...                             ...  ')
    print (' @@@,   &@@@@    @@@  @@@                            ,@@@  ')
    print ('  @@@   @@/@@@  .@@&        @@@ @@@@@     @@@@@@@     @@@  ')
    print ('  /@@( @@@  @@& @@@   @@@   @@@*   @@@   @@%   ,      @@   ')
    print ('   @@@@@@   @@@/@@,   @@@   @@@    @@@    @@@@@@@@    @@   ')
    print ('    @@@@/    @@@@@    @@@   @@@    @@@  @@@/   ,@@#   &&&  ')
    print ('    @@@@      @@@     @@@   @@@    @@@    *@@@@@/     @@@  ')
    print ('                                                           ')

def celebrationtie():                                                                                                    
    print ('                                                        ')
    print ('  @@@@@@@@@@@@@@@@  @@@@                    /@@@@       ')
    print ('  ((((((@@@@((((((                          /@@@@       ')
    print ('        @@@@        @@@@       @@@@@@        @@@@       ')
    print ('        @@@@        @@@@    @@@@@  &@@@@     @@@        ')
    print ('        @@@@        @@@@   @@@@      @@@%    @@@        ')
    print ('        @@@@        @@@@   @@@@@@@@@@@@@@    &@@        ')
    print ('        @@@@        @@@@   *@@@#    *@&(.               ')
    print ('        @@@@        @@@@     @@@@@@@@@@      @@@%       ')
    print ('                                                        ')
                                                            
                                                            

while z is 1:
    tictacboard()
    boardchangerx()
    winchecker()
    tictacboard()
    boardchangero()
    winchecker()
