# Procedure Module
import pygame, time, sys
sys.path.append('Modules')
from loadImages import load, Transform # loads images
pygame.init()
SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg = load()
SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg = Transform(SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg)

def BubbleSort(List):

    # Sorts A list by bubbling the largest values to the Top ( Left side of the list )

    for i in range(len(List)):

        Sorted = False

        for j in range(len(List) - i - 1):

            if int(List[j]) < int(List[j+1]): # Bubbling Largest Value < For Left > For Right 

                List[j], List[j+1] = List[j+1], List[j] # Swaps Values

                Sorted = True

        if Sorted == False:
        
            break

    return List # Returns Sorted List


def DisplayAll(Game, Screen):

    Grid = Game._Grid

    # When game is over or during each iteration of maingame loop, shows everything under the tiles

    Images = [EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg] # list of images 

    for i in range(0, Game._boardSize[0]):

        for j in range(0, Game._boardSize[1]): # Loops through each value of 2Darray Grid 

            if Grid[j][i] == 'X': # Checks if its a Bomb

                Screen.blit(BombImg, ((24 * i)+5, (24 * j) + 55)) # If its a bomb it displays Bomb

            for x in range(8): # Loops through every possible number 1-8, if its equal to x ( 1-8 ) then it displays Xs position value of Images ( 1-8 )

                if Grid[j][i] == str(x):

                    Screen.blit(Images[x], ((24*i)+5, (24*j) + 55)) # Displays Number Image


def RemoveTiles(AllTiles, FlagLock, Hud, Game, clicks):

    for i in range(len(AllTiles)):

        if AllTiles[i]._checkForClick() == True: # Checks What Remaining On Tiles Collides with Mouse Position using Button Method checkForClick

            clicks = clicks + 1

            if (FlagLock == False or FlagLock == True) and AllTiles[i]._FlagOn == False:

                Hud._CalculateScore() # Calculates Score based of time and Mine/Area Ratio

                AllTiles[i]._TileOn = False

                X = AllTiles[i]._TileNumber[0]
                Y = AllTiles[i]._TileNumber[1]

                TileNum = [X, Y]

                if Game._Grid[Y][X] == 'X':

                    return False, TileNum, clicks, False
 

                if clicks == 1:

                    return True, TileNum, clicks, True
                else:
                    return True, TileNum, clicks, False
        
    TileNum = [-1, -1]

    return True, TileNum, clicks, False

def AddFlag(AllTiles, Hud):

    time.sleep(0.09)

    MousePosition = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[2] == 1:

        time.sleep(0.15) # Delay So it doesnt immediatly Turn it back off 

        for i in range(len(AllTiles)):

            if AllTiles[i]._rect.collidepoint(MousePosition) and AllTiles[i]._TileOn == True:

                if AllTiles[i]._FlagOn == True:

                    AllTiles[i]._FlagOn = False
                    Hud._Flags.remove(AllTiles[i]._TileNumber)

                else:

                    AllTiles[i]._FlagOn = True
                    Hud._Flags.append(AllTiles[i]._TileNumber)


def RemoveAdjacentTiles(Grid, AllTiles, MousePos, Game, Hud):

    boardSize = Game._boardSize

    # Find Empty Tiles
  
    EmptyTiles = []  # Acts as A Queue
    Checked = [] # Stores Tiles that have been Checked
    RecordedEmptyTiles = [] # Stores all Empty Tiles

    if MousePos[0] > -1 and MousePos[1] > -1:

        EmptyTiles.append(MousePos)

    if len(EmptyTiles) > 0:

        x = EmptyTiles[0][0]
        y = EmptyTiles[0][1]
                

        # All Connecting Ones

        if Grid[y][x] == '0':


            while len(EmptyTiles) > 0:

                x = EmptyTiles[0][0]
                y = EmptyTiles[0][1]

                if Grid[y][x] == '0' and [x, y] not in Checked:
                        
                        for i in range(len(AllTiles)-1):

                            if AllTiles[i]._TileNumber[0] == x and AllTiles[i]._TileNumber[1] == y:

                                AllTiles[i]._TileOn = False
                            
                        Checked.append([x, y])
                        EmptyTiles.append([x, y])
                        RecordedEmptyTiles.append([x, y])

        
                if x - 1 > -1:

                    if Grid[y][x-1] == '0' and [x-1, y] not in Checked:
                        
                        for i in range(len(AllTiles)-1):

                            if AllTiles[i]._TileNumber[0] == x-1 and AllTiles[i]._TileNumber[1] == y:

                                AllTiles[i]._TileOn = False
                            

                            
                        Checked.append([x-1, y])
                        EmptyTiles.append([x-1, y])
                        RecordedEmptyTiles.append([x-1, y])
                        

                if x + 1 < boardSize[0]:


                    if Grid[y][x+1] == '0' and [x+1, y] not in Checked:

                        for i in range(len(AllTiles)-1):

                            if AllTiles[i]._TileNumber[0] == x+1 and AllTiles[i]._TileNumber[1] == y:

                                    AllTiles[i]._TileOn = False

                        Checked.append([x+1, y])
                        EmptyTiles.append([x+1, y])
                        RecordedEmptyTiles.append([x+1, y])


                if y - 1 > -1:

                    if Grid[y-1][x] == '0' and [x, y-1] not in Checked:

                        for i in range(len(AllTiles)-1):

                            if AllTiles[i]._TileNumber[0] == x and AllTiles[i]._TileNumber[1] == y-1:

                                    AllTiles[i]._TileOn = False

                        Checked.append([x, y-1])
                        EmptyTiles.append([x, y-1])
                        RecordedEmptyTiles.append([x, y-1])


                if y + 1 < boardSize[1]:

                    if Grid[y+1][x] == '0' and [x, y+1] not in Checked:

                        for i in range(len(AllTiles)-1):

                            if AllTiles[i]._TileNumber[0] == x and AllTiles[i]._TileNumber[1] == y+1:

                                    AllTiles[i]._TileOn = False

                        Checked.append([x, y+1])
                        EmptyTiles.append([x, y+1])
                        RecordedEmptyTiles.append([x, y+1])
                        
                EmptyTiles.pop(0)

    for i in range(len(RecordedEmptyTiles)):

        Hud._CalculateScore()

    return RecordedEmptyTiles


def AddExtraNumberTiles(AllTiles, RecordedEmptyTiles):

    ExtraNumberTiles = []

    for i in range(len(RecordedEmptyTiles)):

        x = RecordedEmptyTiles[i][0]
        y = RecordedEmptyTiles[i][1]

        ExtraNumberTiles.append([x+1,y])
        ExtraNumberTiles.append([x-1,y])
        ExtraNumberTiles.append([x,y+1])
        ExtraNumberTiles.append([x,y-1])


    for i in range(len(AllTiles)):

        if [AllTiles[i]._TileNumber[0], AllTiles[i]._TileNumber[1]] in ExtraNumberTiles:

            AllTiles[i]._TileOn = False


def FetchInputText(InputType, MaxSize, POS, whichInput, Texts, Screen):

    # Gets the users text input

    Done = False

    Text = '' # Empty Starting string

    print(MaxSize)

    while Done == False and len(Text) < MaxSize:

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE: # 

                    if len(Text) > 0: # Makes sure there is text to get rid of

                        Text = Text.rstrip(Text[-1]) # Removes the last character of the string

                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                
                    Done = True

                if event.key == pygame.K_SPACE and InputType == 'Alpha': # for the name, allows you to enter a space

                    Text = Text + ' '
                    

                else:

                    if InputType == 'Alpha':

                        if event.unicode.isalpha(): # Returns True if they key pressed is an alphabetic character
                    
                            Text = Text + event.unicode

                    else:

                        if event.unicode.isdigit():

                            Text = Text + event.unicode
                            
            pygame.font.init()
            Font2 = pygame.font.Font('freesansbold.ttf', 15)
            TextDisplay = Font2.render(Text, True, (0, 0, 0))

            if whichInput == 'Name':

                Screen.blit(SelectedNameImg, (20, 10))

            else:
                
                Screen.blit(InputNameImg, (20, 10))
                
            Screen.blit(InputImg, (70, 198))
            Screen.blit(InputImg, (70, 175))
            Screen.blit(InputImg, (205, 195))

            if whichInput == 'Name':
                
                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[1], (10, 180))
                Screen.blit(Texts[2], (10, 200))

            if whichInput == 'Mines':

                Screen.blit(Texts[1], (10, 180))
                Screen.blit(Texts[2], (10, 200))
                Screen.blit(Texts[3], (25, 15))

            if whichInput == 'Width':

                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[2], (10, 200))
                Screen.blit(Texts[3], (25, 15))

            if whichInput == 'Height':

                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[1], (10, 180))
                Screen.blit(Texts[3], (25, 15))
                

            Screen.blit(TextDisplay, (POS[0], POS[1]))

            pygame.display.update()
                        
    return Text


def DisplayLeaderBoard(Screen):

    File = open('MineSweeperScores.txt', 'r')

    data = File.readlines()

    ListOfScores = []

    # Sort Through Data and Find top 3 Highest Scores, Score is First Number
    for i in range(len(data)):

        j = 0
        Text = ''

        while data[i][j] != '/':

            Text = Text + str(data[i][j])

            j = j + 1

        Text = Text + '0'
        ListOfScores.append(Text)
        
    Scores = []
    Names = []

    for i in range(len(ListOfScores)):

        j = 0

        TempScore = ''
        TempName = ''

        while ListOfScores[i][j].isnumeric():

            TempScore = TempScore + str(ListOfScores[i][j])

            j = j + 1

        while ListOfScores[i][j].isalpha():

            TempName = TempName + str(ListOfScores[i][j])

            j = j + 1

        Scores.append(TempScore)
        Names.append(TempName)

    # Bubble Sort Algorithm

    OriginalListOfScores = Scores.copy() # Deep Copy so they dont share the change

    # Bubble Sort Algorithm

    Scores = BubbleSort(Scores)

    # Get Top 5 Scores

    if len(Scores) > 0:
        n = len(Scores)
        if n > 4:
            n = 4
        for i in range(n):
            Text = Scores[i]
            NamePos = OriginalListOfScores.index(Text)
            Font = pygame.font.Font('freesansbold.ttf', 15)
            Text = Font.render(Text, True, (0, 0, 0))
            Screen.blit(Text, (300, 150 + i*20))

            # Find Number in List Of Scores to fetch name at same Position, if duplicat Scores it doesnt matter

            Name = Names[NamePos]

            Font = pygame.font.Font('freesansbold.ttf', 15)
            Name = Font.render(Name, True, (0, 0, 0))
            Screen.blit(Name, (360, 150 + i*20))
