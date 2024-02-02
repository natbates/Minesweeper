import time, pygame, random, os, sys, math  # Imports

pygame.init() # Initialise Pygame Libaries


print('BombMopper Final Version')

# Constants

TileX = 24
TileY = 24

previousTick = 0  # Resets Clock Using Ticks
MenuTick = 0

Font = pygame.font.Font('freesansbold.ttf', 15)
Font2 = pygame.font.Font('freesansbold.ttf', 15)

# Loading And Transforming Images For Display/Interface for Menu

SelectBoxImg = pygame.image.load(os.path.join('Assets/Menu', 'SelectBox.png'))
SelectBoxImg2 = pygame.image.load(os.path.join('Assets/Menu', 'SelectBox2.png'))
InputImg = pygame.image.load(os.path.join('Assets/Menu', 'InputSquare.png'))
InputNameImg =pygame.image.load(os.path.join('Assets/Menu', 'InputName.png'))
SelectedNameImg =pygame.image.load(os.path.join('Assets/Menu', 'Selected.png'))
PlayButtonImg = pygame.image.load(os.path.join('Assets/Menu', 'PlayButton.png'))
QuitButtonImg = pygame.image.load(os.path.join('Assets/Menu', 'QuitImg.png'))
DotImg = pygame.image.load(os.path.join('Assets/Menu', 'Dot.png'))
CrossImg = pygame.image.load(os.path.join('Assets/Menu', 'Cross.png'))

DotImg = pygame.transform.scale(DotImg, (10, 10))
CrossImg = pygame.transform.scale(CrossImg, (10, 10))
InputImg = pygame.transform.scale(InputImg, (40, 22))
InputNameImg = pygame.transform.scale(InputNameImg, (150, 25))
SelectedNameImg = pygame.transform.scale(SelectedNameImg, (150, 25))

# Loading And Transforming Images For Display/Interface for Game

EmptyImg = pygame.image.load(os.path.join('Assets/GameBoard', 'Empty.png'))
OneImg = pygame.image.load(os.path.join('Assets/GameBoard', 'one.jpg'))
TwoImg = pygame.image.load(os.path.join('Assets/GameBoard', 'two.jpg'))
ThreeImg = pygame.image.load(os.path.join('Assets/GameBoard', 'three.jpg'))
FourImg = pygame.image.load(os.path.join('Assets/GameBoard', 'four.jpg'))
FiveImg = pygame.image.load(os.path.join('Assets/GameBoard', 'five.jpg'))
SixImg = pygame.image.load(os.path.join('Assets/GameBoard', 'six.jpg'))
SevenImg = pygame.image.load(os.path.join('Assets/GameBoard', 'seven.jpg'))
EightImg = pygame.image.load(os.path.join('Assets/GameBoard', 'eight.jpg'))
BombImg = pygame.image.load(os.path.join('Assets/GameBoard', 'bomb.png'))
BombMenuImg = pygame.image.load(os.path.join('Assets/GameBoard', 'bombImage.png'))
TileImg = pygame.image.load(os.path.join('Assets/GameBoard', 'Tile.png'))
FlagImg = pygame.image.load(os.path.join('Assets/GameBoard', 'Flag.png'))
RestartImg = pygame.image.load(os.path.join('Assets/GameBoard', 'RestartButton.png'))
WinImg = pygame.image.load(os.path.join('Assets/GameBoard', 'Win.png'))
LooseImg = pygame.image.load(os.path.join('Assets/GameBoard', 'Loose.png'))

EmptyImg = pygame.transform.scale(EmptyImg, (TileX, TileY))
OneImg = pygame.transform.scale(OneImg, (TileX, TileY))
TwoImg = pygame.transform.scale(TwoImg, (TileX, TileY))
ThreeImg = pygame.transform.scale(ThreeImg, (TileX, TileY))
FourImg = pygame.transform.scale(FourImg, (TileX, TileY))
FiveImg = pygame.transform.scale(FiveImg, (TileX, TileY))
SixImg = pygame.transform.scale(SixImg, (TileX, TileY))
SevenImg = pygame.transform.scale(SevenImg, (TileX, TileY))
EightImg = pygame.transform.scale(EightImg, (TileX, TileY))
BombImg = pygame.transform.scale(BombImg, (TileX, TileY))
BombMenuImg = pygame.transform.scale(BombMenuImg, (TileX, TileY))
TileImg = pygame.transform.scale(TileImg, (TileX+1, TileY+1))
FlagImg = pygame.transform.scale(FlagImg, (TileX, TileY))
RestartImg = pygame.transform.scale(RestartImg, (TileX, TileY))
WinImg = pygame.transform.scale(WinImg, (60, 80))
LooseImg = pygame.transform.scale(LooseImg, (100, 80))



class Board():

    # Class that generates a Binary Bit Map Of a Minesweeper Board, Also stores Time

    def __init__(self, boardSize, Difficulty, Mines):

        self.boardSize = boardSize
        self.Difficulty = Difficulty
        self.Mines = int(Mines)
        self.Grid = []
        self.RecordedMinePositions = []
        self.Flags = []
        self.MaxScore = int(boardSize[1]) * int(boardSize[0]) * int(Mines)

        self.ScorePerTile = self.Mines
        
        self.miliseconds = 0
        self.secs = 0
        self.mins = 0
        self.name = 'Guest'
        self.Score = 1

        self.ScoreConstant = (int(self.Mines) / (int(self.boardSize[0]) * int(self.boardSize[1]))) * 100
        

    def createGrid(self):

        # Creates A Empty Binary Bit Map which will be Used to work with map, Reversed [DEPTH FROM 0, DISTANCE FROM 0]

        for row in range(self.boardSize[1]):

            list = []

            for unit in range(int(self.boardSize[0])):
                
                list.append('0')   # 0 on the Grid Symbolises an Empty Square, For now they all will All be Empty

            self.Grid.append(list)

    def placeMines(self):

        # Randomly Places Mines on the Grid

        MinePositions = []

        for i in range(self.Mines):

            MineNotPlaced = True
            while MineNotPlaced == True:

                x = random.randint(0, self.boardSize[0] - 1)
                y = random.randint(0, self.boardSize[1] - 1)

                position = [x, y]

                if position in MinePositions:
                    pass
                else:
                    MineNotPlaced = False
                    MinePositions.append(position)

        for i in range(self.Mines):
            MinePosition = MinePositions[i]
            MinePositionY = MinePosition[0]
            MinePositionX = MinePosition[1]

            self.Grid[MinePositionX][MinePositionY] = 'X'

        self.RecordedMinePositions = MinePositions

    def bombAlerts(self):

        # Adds/Increment Numbers on The Grid Depending on how Many Mines surround it

        for i in range(self.Mines):

            MinePosition = self.RecordedMinePositions[i]
            MinePositionY = MinePosition[1]
            MinePositionX = MinePosition[0]

            # Left

            if MinePositionX > 0:

                if self.Grid[MinePositionY][MinePositionX - 1] != 'X':
                    num = self.Grid[MinePositionY][MinePositionX - 1]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY][MinePositionX - 1] = newNum
                    newNum = 0

            # Right

            if MinePositionX < self.boardSize[0] - 1:

                if self.Grid[MinePositionY][MinePositionX + 1] != 'X':
                    num = self.Grid[MinePositionY][MinePositionX + 1]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY][MinePositionX + 1] = newNum
                    newNum = 0

            # Up

            if MinePositionY > 0:

                if self.Grid[MinePositionY - 1][MinePositionX] != 'X':
                    num = self.Grid[MinePositionY - 1][MinePositionX]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY - 1][MinePositionX] = newNum
                    newNum = 0

            # Down

            if MinePositionY < self.boardSize[1] - 1:

                if self.Grid[MinePositionY + 1][MinePositionX] != 'X':
                    num = self.Grid[MinePositionY + 1][MinePositionX]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY + 1][MinePositionX] = newNum
                    newNum = 0

            # Bottom Right

            if MinePositionX < self.boardSize[0] - 1 and MinePositionY < self.boardSize[1] - 1:

                if self.Grid[MinePositionY + 1][MinePositionX + 1] != 'X':
                    num = self.Grid[MinePositionY + 1][MinePositionX + 1]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY + 1][MinePositionX + 1] = newNum
                    newNum = 0

            # Bottom Left

            if MinePositionX > 0 and MinePositionY < self.boardSize[1] - 1:

                if self.Grid[MinePositionY + 1][MinePositionX - 1] != 'X':
                    num = self.Grid[MinePositionY + 1][MinePositionX - 1]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY + 1][MinePositionX - 1] = newNum
                    newNum = 0

            # Top Right

            if MinePositionY > 0 and MinePositionX < self.boardSize[0] - 1:

                if self.Grid[MinePositionY - 1][MinePositionX + 1] != 'X':
                    num = self.Grid[MinePositionY - 1][MinePositionX + 1]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY - 1][MinePositionX + 1] = newNum
                    newNum = 0

            # Top Left

            if MinePositionY > 0 and MinePositionX > 0:

                if self.Grid[MinePositionY - 1][MinePositionX - 1] != 'X':
                    num = self.Grid[MinePositionY - 1][MinePositionX - 1]
                    newNum = str(int(num) + 1)
                    self.Grid[MinePositionY - 1][MinePositionX - 1] = newNum
                    newNum = 0


    def DisplayClock(self):

        pygame.font.init()

        self.miliseconds += 1

        if self.miliseconds == 10:

            self.secs += 1
            self.miliseconds = 0
            self.ScorePerTile = self.ScorePerTile * 0.99     

        if self.secs == 60:

            self.mins += 1
            self.secs = 0

        text = str(self.mins) +':'+ str(self.secs)
        Font = pygame.font.Font('freesansbold.ttf', 15)
        Text = Font.render(text, True, (255, 0, 0))

        GameScreen.blit(Text, (ScreenWidth- 70, 25))


    def DisplayAmountOfFlagsandBombs(self):

        FlagNum = len(self.Flags)

        Font = pygame.font.Font('freesansbold.ttf', 15)
        FlagNum = Font.render(str(FlagNum), True, (255, 0, 0))
        MineNum = Font.render(str(self.Mines), True, (255, 0, 0))

        GameScreen.blit(FlagNum, (5, 25))
        GameScreen.blit(MineNum, (40, 25))

        GameScreen.blit(FlagImg, (18, 20))
        GameScreen.blit(BombMenuImg, (58, 20))
 

    def CalculateScore(self):

        # FInd Area/Mine Ratio and Divide By Time Taken`poiuyhg

        self.Score = self.Score + self.ScorePerTile

        # Round Score up

        self.Score = math.trunc(self.Score)



    def DisplayScore(self):

        score = str(self.Score)
        Font = pygame.font.Font('freesansbold.ttf', 15)
        score = Font.render(score, True, (255, 0, 0))

        GameScreen.blit(score, (ScreenWidth-37, 25))


    def RecordScore(self, WinOrLoss):

        Text = str(self.Score) + str(self.Name) + '/ WIN: '+ str(WinOrLoss) + str(self.Difficulty) + ' Time: '+ str(self.mins) + 'm '+ str(self.secs) +  's Amount of Mines: '+ str(self.Mines) + ' BoardSize: ' + str(self.boardSize)

        File = open('MineSweeperScores.txt', 'a')

        File.write(Text+'\n')

        File.close()
            
        


class Button():

    # Simple Button Class For Main Menus and Later Tiles

    def __init__(self, x, y, image, scale):

        self.scale = float(scale)
        self.y = y
        self.x = x
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def checkForClick(self):

        # Very Simple Method that checks if the user clicks it

        Clicked = False
        MousePosition = pygame.mouse.get_pos()
        if self.rect.collidepoint(MousePosition):
            if pygame.mouse.get_pressed()[0] == 1:
                Clicked = True
                
        return Clicked

    def Draw(self, Screen):

        Screen.blit(self.image, (self.rect.x, self.rect.y))



class Tile(Button):

        # A Tile Inherits from Button class and uses shared attributes

        def __init__(self, x, y, image, scale, TileNumber, Flag, TileOn):

            super().__init__(x, y, image, scale)

            # Each Tile Has Unique Identifier

            self.TileNumber = TileNumber
            self.Flag = Flag
            self.TileOn = TileOn


        def DisplayFlags(self):

            if self.Flag == True:

                GameScreen.blit(FlagImg, (self.x, self.y))


        def DisplayTiles(self):

            if self.TileOn == True:

                GameScreen.blit(self.image, (self.x, self.y))


# FUNCTIONS/SUBROUTINES

def BubbleSort(List):

    for i in range(len(List)):

        Sorted = False

        for j in range(len(List) - i - 1):

            if int(List[j]) < int(List[j+1]):

                List[j], List[j+1] = List[j+1], List[j]

                Sorted = True


        if Sorted == False:
        
            break

    return List

  

def DisplayAll(Grid):

    for i in range(0, Game.boardSize[0]):

        for j in range(0, Game.boardSize[1]):

            if Grid[j][i] == 'X':

                GameScreen.blit(BombImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '0':

                GameScreen.blit(EmptyImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '1':

                GameScreen.blit(OneImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '2':

                GameScreen.blit(TwoImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '3':

                GameScreen.blit(ThreeImg, ((24 * i)+5,  (24 * j)+5+50))

            elif Grid[j][i] == '4':

                GameScreen.blit(FourImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '5':

                GameScreen.blit(FiveImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '6':

                GameScreen.blit(SixImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '7':

                GameScreen.blit(SevenImg, ((24 * i)+5, (24 * j)+5+50))

            elif Grid[j][i] == '8':

                GameScreen.blit(EightImg, ((24 * i)+5, (24 * j)+5+50))
    

def RemoveTiles(AllTiles):

    MousePosition = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] == 1:


        for i in range(len(AllTiles)):

            if AllTiles[i].rect.collidepoint(MousePosition):

                if FlagLock == True and AllTiles[i].Flag == False:

                    Game.CalculateScore() # Calculates Score based of time and Mine/Area Ratio

                    AllTiles[i].TileOn = False

                    X = AllTiles[i].TileNumber[0]
                    Y = AllTiles[i].TileNumber[1]

                    TileNum = [X, Y]

                    if Grid[Y][X] == 'X':

                        return False, TileNum

                    return True, TileNum

                if FlagLock == False:

                    Game.CalculateScore() # Calculates Score based of time and Mine/Area Ratio

                    AllTiles[i].TileOn = False

                    X = AllTiles[i].TileNumber[0]
                    Y = AllTiles[i].TileNumber[1]

                    TileNum = [X, Y]

                    if Grid[Y][X] == 'X':

                        return False, TileNum

                    return True, TileNum

    TileNum = [-1, -1]

    return True, TileNum

def AddFlag(AllTiles):

    time.sleep(0.09)

    MousePosition = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[2] == 1:

        time.sleep(0.15) # Delay So it doesnt immediatly Turn it back off 

        for i in range(len(AllTiles)):

            if AllTiles[i].rect.collidepoint(MousePosition) and AllTiles[i].TileOn == True:

                if AllTiles[i].Flag == True:

                    AllTiles[i].Flag = False
                    Game.Flags.remove(AllTiles[i].TileNumber)

                else:

                    AllTiles[i].Flag = True
                    Game.Flags.append(AllTiles[i].TileNumber)


def RemoveAdjacentTiles(Grid, AllTiles, MousePos):

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

                            if AllTiles[i].TileNumber[0] == x and AllTiles[i].TileNumber[1] == y:

                                AllTiles[i].TileOn = False
                            
                        Checked.append([x, y])
                        EmptyTiles.append([x, y])
                        RecordedEmptyTiles.append([x, y])

        
                if x - 1 > -1:

                    if Grid[y][x-1] == '0' and [x-1, y] not in Checked:
                        
                        for i in range(len(AllTiles)-1):

                            if AllTiles[i].TileNumber[0] == x-1 and AllTiles[i].TileNumber[1] == y:

                                AllTiles[i].TileOn = False
                            

                            
                        Checked.append([x-1, y])
                        EmptyTiles.append([x-1, y])
                        RecordedEmptyTiles.append([x-1, y])
                        

                if x + 1 < boardSize[0]:


                    if Grid[y][x+1] == '0' and [x+1, y] not in Checked:

                        for i in range(len(AllTiles)-1):

                            if AllTiles[i].TileNumber[0] == x+1 and AllTiles[i].TileNumber[1] == y:

                                    AllTiles[i].TileOn = False

                        Checked.append([x+1, y])
                        EmptyTiles.append([x+1, y])
                        RecordedEmptyTiles.append([x+1, y])


                if y - 1 > -1:

                    if Grid[y-1][x] == '0' and [x, y-1] not in Checked:

                        for i in range(len(AllTiles)-1):

                            if AllTiles[i].TileNumber[0] == x and AllTiles[i].TileNumber[1] == y-1:

                                    AllTiles[i].TileOn = False

                        Checked.append([x, y-1])
                        EmptyTiles.append([x, y-1])
                        RecordedEmptyTiles.append([x, y-1])


                if y + 1 < boardSize[1]:

                    if Grid[y+1][x] == '0' and [x, y+1] not in Checked:

                        for i in range(len(AllTiles)-1):

                            if AllTiles[i].TileNumber[0] == x and AllTiles[i].TileNumber[1] == y+1:

                                    AllTiles[i].TileOn = False

                        Checked.append([x, y+1])
                        EmptyTiles.append([x, y+1])
                        RecordedEmptyTiles.append([x, y+1])
                        
                EmptyTiles.pop(0)

    for i in range(len(RecordedEmptyTiles)):

        Game.CalculateScore()

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

        if [AllTiles[i].TileNumber[0], AllTiles[i].TileNumber[1]] in ExtraNumberTiles:

            AllTiles[i].TileOn = False


def FetchInputText(InputType, MaxSize, POS, whichInput, Texts):

    Done = False

    Text = ''

    print(MaxSize)

    while Done == False and len(Text) < MaxSize:

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    if len(Text) > 0:

                        Text = Text.rstrip(Text[-1])


                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                
                    Done = True

                    

                if event.key == pygame.K_SPACE and InputType == 'Alpha':

                    Text = Text + ' '
                    

                else:

                    if InputType == 'Alpha':

                        if event.unicode.isalpha():
                    
                            Text = Text + event.unicode

                    else:

                        if event.unicode.isdigit():

                            Text = Text + event.unicode
                            

            TextDisplay = Font2.render(Text, True, (0, 0, 0))

            if whichInput == 'Name':

                MenuScreen.blit(SelectedNameImg, (20, 10))

            else:
                
                MenuScreen.blit(InputNameImg, (20, 10))
                
            MenuScreen.blit(InputImg, (70, 198))
            MenuScreen.blit(InputImg, (70, 175))
            MenuScreen.blit(InputImg, (205, 195))

            if whichInput == 'Name':

                

                MenuScreen.blit(Texts[0], (150, 200))
                MenuScreen.blit(Texts[1], (10, 180))
                MenuScreen.blit(Texts[2], (10, 200))

            if whichInput == 'Mines':

                MenuScreen.blit(Texts[1], (10, 180))
                MenuScreen.blit(Texts[2], (10, 200))
                MenuScreen.blit(Texts[3], (25, 15))

            if whichInput == 'Width':

                MenuScreen.blit(Texts[0], (150, 200))
                MenuScreen.blit(Texts[2], (10, 200))
                MenuScreen.blit(Texts[3], (25, 15))

            if whichInput == 'Height':

                MenuScreen.blit(Texts[0], (150, 200))
                MenuScreen.blit(Texts[1], (10, 180))
                MenuScreen.blit(Texts[3], (25, 15))
                

            MenuScreen.blit(TextDisplay, (POS[0], POS[1]))

            pygame.display.update()
                        

    return Text


    


def DisplayLeaderBoard():

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
            MenuScreen.blit(Text, (300, 150 + i*20))

            # Find Number in List Of Scores to fetch name at same Position, if duplicat Scores it doesnt matter

            Name = Names[NamePos]

            Font = pygame.font.Font('freesansbold.ttf', 15)
            Name = Font.render(Name, True, (0, 0, 0))
            MenuScreen.blit(Name, (360, 150 + i*20))

    

# Create Main Menu Objects (Buttons), Create Main Menu Display

MenuScreenSize = (450, 250)

MenuScreen = pygame.display.set_mode(MenuScreenSize)

BeginnerButton = Button(20, 50, SelectBoxImg, 0.08)
IntermediateButton = Button(20, 70, SelectBoxImg, 0.08)
ExpertButton = Button(20, 90, SelectBoxImg, 0.08)
CustomButton = Button(20, 110, SelectBoxImg, 0.08)

TileLockOnButton = Button(150, 50, SelectBoxImg2, 0.08)
SoundOnButton = Button(150, 70, SelectBoxImg2, 0.08)
SaveScoreButton = Button(150, 90, SelectBoxImg2, 0.08)

PlayButton = Button(300, 50, PlayButtonImg, 0.124)
QuitButton = Button(300, 100, QuitButtonImg, 0.124)

HeightInputButton = Button(70, 198, InputImg, 1)
WidthInputButton = Button(70, 175, InputImg, 1)
MineInputButton = Button(205, 195, InputImg, 1)
InputNameButton = Button(20, 10, InputNameImg, 1)


# Open Files

MainGameLoop = True

# MAIN PROGRAM


while MainGameLoop:

    MenuTick = 0

    MenuScreen = pygame.display.set_mode(MenuScreenSize)

    pygame.font.init()

    # Time
    
    Score = 0

    Mines = 25
    Difficulty = 2
    BoardWidth = 15
    BoardHeight = 20

    SaveButtonNum = 0
    SoundOnNum = 0
    TileLockOnNum = 0
    

    Beginner = False
    Intermediate = True
    Expert = False
    Custom = False

    SoundButtonOn = False
    TileLockOnButtonOn = True
    SaveScoreButtonOn = True

    FlagLock = True
    SaveScore = True

    Name = 'Guest'
    

    # Run Main Menu To Get the Difficulty or Custom Details

    MenuScreen = pygame.display.set_mode(MenuScreenSize)

    MainMenuLoop = True


    while MainMenuLoop:

        MenuScreen.fill((255, 255, 255))

        DisplayLeaderBoard()

        BeginnerButton.Draw(MenuScreen)
        IntermediateButton.Draw(MenuScreen)
        ExpertButton.Draw(MenuScreen)
        CustomButton.Draw(MenuScreen)
        TileLockOnButton.Draw(MenuScreen)
        SoundOnButton.Draw(MenuScreen)
        SaveScoreButton.Draw(MenuScreen)
        PlayButton.Draw(MenuScreen)
        QuitButton.Draw(MenuScreen)


        if PlayButton.checkForClick() == True:

            MainMenuLoop = False

        if QuitButton.checkForClick() == True:

            pygame.quit()
            sys.exit()

        if BeginnerButton.checkForClick() == True:

            Beginner = True
            Intermediate = False
            Expert = False
            Custom = False

            Mines = 10
            Difficulty = 1
            BoardWidth = 8
            BoardHeight = 10
            

        if IntermediateButton.checkForClick() == True:

            Beginner = False
            Intermediate = True
            Expert = False
            Custom = False

            Mines = 40
            BoardWidth = 14
            BoardHeight = 18
            Difficulty = 2

        if ExpertButton.checkForClick() == True:

            Beginner = False
            Intermediate = False
            Expert = True
            Custom = False

            Mines = 99
            Difficulty = 3
            BoardWidth = 20
            BoardHeight = 24

        if CustomButton.checkForClick() == True:

            Beginner = False
            Intermediate = False
            Expert = False
            Custom = True
            Difficulty = 0

            Mines = ''
            Difficulty = ''
            BoardWidth = ''
            BoardHeight = ''

            

        if SaveScoreButton.checkForClick() == True:

            time.sleep(0.25)      

            SaveButtonNum +=1



            if SaveButtonNum % 2 == 0:
                SaveScoreButtonOn = False
                SaveScore = False
            
            else:
                SaveScoreButtonOn = True
                SaveScore = True

        if TileLockOnButton.checkForClick() == True:

            time.sleep(0.25)

            TileLockOnNum +=1

            if TileLockOnNum % 2 == 0:
                
                TileLockOnButtonOn = False

                FlagLock = False
            
            else:
                TileLockOnButtonOn = True

                FlagLock = True

        if SoundOnButton.checkForClick() == True:

            time.sleep(0.25)

            SoundOnNum += 1

            if SoundOnNum % 2 == 0:
                SoundButtonOn = False

            else:

                SoundButtonOn = True
                

        if Beginner == True:

            MenuScreen.blit(DotImg, (20, 50))

        if Intermediate == True:

            MenuScreen.blit(DotImg, (20, 70))

        if Expert ==  True:

            MenuScreen.blit(DotImg, (20, 90))

        if Custom == True:

            MenuScreen.blit(DotImg, (20, 110))
            

        if SaveScoreButtonOn == True:

            MenuScreen.blit(CrossImg, (150, 90))

        if TileLockOnButtonOn == True:

            MenuScreen.blit(CrossImg, (150, 50))

        if SoundButtonOn == True:

            MenuScreen.blit(CrossImg, (150, 70))


        MenuScreen.blit(InputImg, (70, 198))
        MenuScreen.blit(InputImg, (70, 175))
        MenuScreen.blit(InputImg, (205, 195))


        Font2 = pygame.font.Font('freesansbold.ttf', 15)

        Text1 = Font2.render('Mines:     '+str(Mines), True, (0, 0, 0))
        Text2 = Font2.render('Width:     '+str(BoardWidth), True, (0, 0, 0))
        Text3 = Font2.render('Height:    '+str(BoardHeight), True, (0, 0, 0))

        Text4 = Font2.render('Beginner', True, (0, 0, 0))
        Text5 = Font2.render('Intermediate', True, (0, 0, 0))
        Text6 = Font2.render('Expert', True, (0, 0, 0))
        Text7 = Font2.render('Custom', True, (0, 0, 0))

        Text8 = Font2.render('Tile LOCK', True, (0, 0, 0))
        Text9 = Font2.render('Sound', True, (0, 0, 0))
        Text10 = Font2.render('Save Score', True, (0, 0, 0))


        MenuScreen.blit(Text1, (150, 200))
        MenuScreen.blit(Text2, (10, 180))
        MenuScreen.blit(Text3, (10, 200))

        MenuScreen.blit(Text4, (40, 50))
        MenuScreen.blit(Text5, (40, 70))
        MenuScreen.blit(Text6, (40, 90))
        MenuScreen.blit(Text7, (40, 110))

        MenuScreen.blit(Text8, (180, 50))
        MenuScreen.blit(Text9, (180, 70))
        MenuScreen.blit(Text10, (180, 90))

        NameDisplay = Font2.render(Name, True, (0, 0, 0))         

        Texts = [Text1, Text2, Text3, NameDisplay]

        MenuScreen.blit(InputNameImg, (20, 10))

        if InputNameButton.checkForClick() == True:

            Name = ''

            Done = False

            TypingImgIncrement = 0

            Name = FetchInputText('Alpha', 10, [25, 15], 'Name', Texts)
   
           

        MenuScreen.blit(NameDisplay, (25, 15))
        

        if Custom == True:


            InputPlace = ''

            if HeightInputButton.checkForClick() == True:

                InputPlace = 'Height'
                
            if WidthInputButton.checkForClick() == True:

                InputPlace = 'Width'

            if MineInputButton.checkForClick() == True:

                InputPlace = 'Mines'


            Done = False

            if len(InputPlace) > 0:

                if InputPlace == 'Mines':

                    Mines = FetchInputText('Digits', 3, [210, 200], InputPlace, Texts) 
                    if len(Mines) == 0:
                        Mines = 1


                if InputPlace == 'Width':

                    BoardWidth = int(FetchInputText('Digits', 2, [80, 179], InputPlace, Texts))

                    if len(str(BoardWidth)) == 0:

                        BoardWidth = 0
                    
                    if BoardWidth < 8 or BoardWidth > 25:

                        BoardWidth = 0

                    
                if InputPlace == 'Height':

                    BoardHeight = int(FetchInputText('Digits', 2, [80, 203], InputPlace, Texts)) 

                    if len(str(BoardHeight)) == 0:

                        BoardHeight = 0
                    
                    if BoardHeight < 8 or BoardHeight > 25:

                        BoardHeight = 0


        if len(str(Mines)) > 0 and len(str(BoardWidth)) > 0 and len(str(BoardHeight)) > 0:
                

            if int(Mines) >= int(BoardWidth)*int(BoardHeight):

                BoardWidth = ''
                BoardHeight = ''
                Mines = ''



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    pygame.quit()

    MenuTick = pygame.time.get_ticks()


    boardSize = [BoardWidth, BoardHeight]

    # Creating the GameBoard Map

    Game = Board(boardSize, Difficulty, Mines)
    Game.Name = Name
    Game.createGrid()
    Game.placeMines()
    Game.bombAlerts()

    # Setting up Game Screen Based of how many Tiles there are
    
    ScreenWidth = ((Game.boardSize[0]) * 24) + 10
    ScreenHeight = ((Game.boardSize[1]) * 24) + 55
    ScreenSize = (ScreenWidth, ScreenHeight)

    GameScreen = pygame.display.set_mode(ScreenSize)
    GameScreen.fill((168, 164, 164)) # Back Ground Colour of Tiles
    pygame.display.set_caption('MineSweeper!') # Window Caption

    # Create Necessary Objects

    RestartButton = Button((ScreenWidth/2)-18, 5, RestartImg, 1.85)

    GameLoop = True

    Clock = pygame.time.Clock()
    Grid = Game.Grid

    AllTiles = [] # Collection of Object Tiles


    for i in range(Game.boardSize[0]):

        for j in range(Game.boardSize[1]):
            
            AllTiles.append(Tile((24*i)+5, (24*j)+55, TileImg,1, (i, j), False, True))


    while GameLoop:

        # Check for WIN condition

        MinePos = Game.RecordedMinePositions

        RemainingTiles = []

        for i in range(len(AllTiles)):

            if AllTiles[i].TileOn == True:

                RemainingTiles.append([AllTiles[i].TileNumber[0], AllTiles[i].TileNumber[1]])


        # Order Both Arrays and Check if they are the same

        MinePos2 = (MinePos).sort(key=lambda x:x[1])
        RemainingTiles2 = (RemainingTiles).sort(key=lambda x:x[1])


        if MinePos == RemainingTiles:

            WinOrLoss = True

            if SaveScore == True:

                Game.RecordScore(WinOrLoss)
            
            DisplayAll(Grid)
            previousTick = pygame.time.get_ticks()
            GameScreen.blit(WinImg, ((ScreenWidth/2)-30, 0))
            pygame.display.update()
            while GameLoop:
                for event in pygame.event.get():      
                    if event.type == pygame.KEYDOWN:
                        GameLoop = False
                        MainMenuLoop = True
                        del Game
                        pygame.quit()
                        break
            break


        
        # ADD/REMOVE flags ( Does both )

        AddFlag(AllTiles)
        

        # Remove Flags If they NOT on Tile, # Not needed if FlagLock is on

        if FlagLock == False:

            for i in range(len(AllTiles)):

                if AllTiles[i].TileOn == False and AllTiles[i].Flag == True:

                    AllTiles[i].Flag = False

        # REMOVE Tiles
        
        Status, TileNum = RemoveTiles(AllTiles)

        if Status == False:  # Loose Condition

            WinOrLoss = False

            if SaveScore == True:
                Game.RecordScore(WinOrLoss)
                
            previousTick = pygame.time.get_ticks()
            DisplayAll(Grid)
            GameScreen.blit(LooseImg, ((ScreenWidth/2)-30, 0))          
            pygame.display.update()
            while GameLoop:
                for event in pygame.event.get():      
                    if event.type == pygame.KEYDOWN:
                        GameLoop = False
                        MainMenuLoop = True
                        del Game
                        pygame.quit()
                        break
            break

        # Remove All Adjacent Empty Tiles + Number Next to it

        RecordedEmptyTiles = RemoveAdjacentTiles(Grid, AllTiles, TileNum)

        AddExtraNumberTiles(AllTiles, RecordedEmptyTiles)

        # Display Grid

        DisplayAll(Grid)

        # Display Tiles

        for i in range(len(AllTiles)):

            AllTiles[i].DisplayTiles()
        

        # Display Flags

        for i in range(len(AllTiles)):

            AllTiles[i].DisplayFlags()


        # Check For Restart

        RestartButton.Draw(GameScreen)
        
        if RestartButton.checkForClick() == True:
            
            previousTick = pygame.time.get_ticks()
            GameLoop = False
            MainMenuLoop = True
            DisplayAll(Grid)
            pygame.display.update()
            time.sleep(1)
            del Game
            pygame.quit()
            break


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()


        # Update Score And Clock

        Game.DisplayClock()

        Game.DisplayAmountOfFlagsandBombs()

        Game.DisplayScore()

        pygame.display.update()
    
        GameScreen.fill((168, 164, 164))  # Refreshes Game Screen For Updates

        Clock.tick(100)
    
    
    
    

    




















