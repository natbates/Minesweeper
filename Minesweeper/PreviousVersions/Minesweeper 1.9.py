import time, pygame, random, os, sys, math  # Imports
sys.path.append('Modules')
from loadImages import load # Load Image Module
from MainMenu import DisplayText, DisplayButtonDots, CustomFetchText
from Procedures import BubbleSort, DisplayAll, RemoveTiles, AddFlag, RemoveAdjacentTiles, AddExtraNumberTiles, FetchInputText, DisplayLeaderBoard


pygame.init() # Initialise Pygame Libaries

SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg = load()

print('BombMopper Final Version')

# Constants/Fonts

TileX = 24
TileY = 2

previousTick = 0  # Resets Clock Using Ticks
MenuTick = 0

Font = pygame.font.Font('freesansbold.ttf', 15)
Font2 = pygame.font.Font('freesansbold.ttf', 15)


class Board():

    # Class that generates a Binary Bit Map Of a Minesweeper Board, Also stores Time, Score and Name

    def __init__(self, boardSize, Mines):

        # Passed In Attributes
        self._boardSize = boardSize
        self._Mines = Mines

        # Starting Empty List Attributes, Used to store information about the game: Mines, Flags, Bomb Alerts
        self._Grid = []
        self._RecordedMinePositions = []
        
        

    def _createGrid(self):

        # Creates A Empty Binary Bit Map which will be Used to work with map, Reversed [DEPTH FROM 0, DISTANCE FROM 0]

        for row in range(self._boardSize[1]):

            list = []

            for unit in range(self._boardSize[0]):
                
                list.append('0')   # 0 on the Grid Symbolises an Empty Square, For now they all will All be Empty

            self._Grid.append(list)

    def _placeMines(self):

        # Randomly Places Mines on the Grid

        MinePositions = [] # Records Positons of all Mines Created as a 2D Array

        for i in range(self._Mines): # Loops for the amount of Mines Selected

            MineNotPlaced = True
            
            while MineNotPlaced: # Continues Until Mine is Placed

                x = random.randint(0, self._boardSize[0] - 1) # Gets a Random Number between 0 and the BoardWidth
                y = random.randint(0, self._boardSize[1] - 1) # Gets a Random Number between 0 and the BoardHeight

                position = [x, y]

                if position in MinePositions: # Makes Sure Mines arent Placed in same Place Twice
                    pass
                else:
                    MineNotPlaced = False
                    MinePositions.append(position)

        for i in range(self._Mines): # Updates The Grid with each Mines Position
            
            MinePosition = MinePositions[i]
            MinePositionY = MinePosition[0]
            MinePositionX = MinePosition[1]

            self._Grid[MinePositionX][MinePositionY] = 'X' # Displays them on Grid as X, Graph of Grid X/Y is inverted (Grid[Y][X])

        self._RecordedMinePositions = MinePositions # Records them for Later Use


    def _bombAlerts(self):

        # Adds/Increment Numbers on The Grid Depending on how Many Mines surround it

        for i in range(len(self._RecordedMinePositions)): # Loops For the Amount Of Mines Created 

            MinePosition = self._RecordedMinePositions[i]
            MinePositionY = MinePosition[1]
            MinePositionX = MinePosition[0]

            if MinePositionX > 0: # Checks Tile to the Left

                if self._Grid[MinePositionY][MinePositionX - 1] != 'X': # If The left tile isnt a bomb
                    
                    num = self._Grid[MinePositionY][MinePositionX - 1] # Gets the Number, if its the first iteration it will be 0, otherwise it could be 1-7
                    
                    newNum = str(int(num) + 1) # Increments Number by 1
                    
                    self._Grid[MinePositionY][MinePositionX - 1] = newNum # Updates NewNumber to Grid
                    

            if MinePositionX < self._boardSize[0] - 1: # Same For Tile Right of Mine 

                if self._Grid[MinePositionY][MinePositionX + 1] != 'X':
                    num = self._Grid[MinePositionY][MinePositionX + 1]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY][MinePositionX + 1] = newNum

            if MinePositionY > 0: # Same For Tile Above Mine

                if self._Grid[MinePositionY - 1][MinePositionX] != 'X':
                    num = self._Grid[MinePositionY - 1][MinePositionX]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY - 1][MinePositionX] = newNum

            if MinePositionY < self._boardSize[1] - 1: # Same For Tile Below Mine

                if self._Grid[MinePositionY + 1][MinePositionX] != 'X':
                    num = self._Grid[MinePositionY + 1][MinePositionX]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY + 1][MinePositionX] = newNum

            if MinePositionX < self._boardSize[0] - 1 and MinePositionY < self._boardSize[1] - 1: # Same For Tile Bottom Right of Mine

                if self._Grid[MinePositionY + 1][MinePositionX + 1] != 'X':
                    num = self._Grid[MinePositionY + 1][MinePositionX + 1]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY + 1][MinePositionX + 1] = newNum

            if MinePositionX > 0 and MinePositionY < self._boardSize[1] - 1: # Same For Tile Bottom Left of Mine

                if self._Grid[MinePositionY + 1][MinePositionX - 1] != 'X':
                    num = self._Grid[MinePositionY + 1][MinePositionX - 1]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY + 1][MinePositionX - 1] = newNum

            if MinePositionY > 0 and MinePositionX < self._boardSize[0] - 1: # Same For Tile Top Right of Mine

                if self._Grid[MinePositionY - 1][MinePositionX + 1] != 'X':
                    num = self._Grid[MinePositionY - 1][MinePositionX + 1]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY - 1][MinePositionX + 1] = newNum

            if MinePositionY > 0 and MinePositionX > 0: # Same For Tile Top Left of Mine

                if self._Grid[MinePositionY - 1][MinePositionX - 1] != 'X':
                    num = self._Grid[MinePositionY - 1][MinePositionX - 1]
                    newNum = str(int(num) + 1)
                    self._Grid[MinePositionY - 1][MinePositionX - 1] = newNum


class HUD():

    def __init__(self, boardSize, Mines, startingScore, information):

        # Constants Attributes 
        self._MaxScore = int(boardSize[1]) * int(boardSize[0]) * (Mines*2)
        self._ScorePerTile = Mines*2
        self._Flags = []
        self._Mines = Mines

        # Static Attributes
        self._Score = startingScore
        self._milliseconds = 0
        self._secs = 0
        self._mins = 0

        self._information = information

    def _DisplayClock(self):

        # Displays The Clock Digital (Minutes, Seconds)

        pygame.font.init() # Initalises Font

        self._milliseconds += 1 # Increments Miliseconds Each time the clocks Ticks (100/s)

        if self._milliseconds == 10: # 10 Miliseconds in a Second

            self._secs += 1
            self._milliseconds = 0 # Resets
            self._ScorePerTile = self._ScorePerTile * 0.99 # After Each Second passes the Possible scorePerTile decreases by 1% ( Cant Reach 0 or -)

        if self._secs == 60:

            self._mins += 1
            self._secs = 0

        text = str(self._mins) +':'+ str(self._secs)
        Font = pygame.font.Font('freesansbold.ttf', 15)
        Text = Font.render(text, True, (255, 0, 0)) # Renders Font

        GameScreen.blit(Text, (ScreenWidth - 70, 25)) # Displays The Text to the GameScreen


    def _DisplayAmountOfFlagsandBombs(self):

        # Displays the Amount of Mines left and Amount of Flags on the Board at the Top of the GameScreen

        Font = pygame.font.Font('freesansbold.ttf', 15)
        FlagNum = Font.render(str(len(self._Flags)), True, (255, 0, 0))
        MineNum = Font.render(str(self._Mines), True, (255, 0, 0))

        GameScreen.blit(FlagNum, (5, 25))
        GameScreen.blit(MineNum, (40, 25))

        GameScreen.blit(FlagImg, (18, 20)) # Displays Images of Flag
        GameScreen.blit(BombMenuImg, (58, 20))  # Displays Images of Bomb
 

    def _CalculateScore(self):

        # Calculates Score, Called For each tile that is taken of the board

        self._Score = self._Score + self._ScorePerTile # Increments Score by ScorePerTile

        # Round Score up

        self._Score = math.trunc(self._Score) # Removes Decimal to avoid long string when Displaying

        if self._Score > self._MaxScore: # Not Needed but Just in Case The User manages to exploit the Score

            self._Score = self._MaxScore

    def _DisplayScore(self):

        # Displays Score on GameScreen, Had to be Seperate to Calculate Score otherwise each time its displayed it would Increment Score

        score = str(self._Score)
        Font = pygame.font.Font('freesansbold.ttf', 15)
        score = Font.render(score, True, (0, 0, 255))

        GameScreen.blit(score, (ScreenWidth-37, 25))


    def _RecordScore(self, WinOrLoss):

        # Called When game is Won or Lost

        Text = str(self._Score) + str(self._information[0]) + '/ STATUS: '+ str(WinOrLoss) + ' Time: '+ str(self._mins) + 'm '+ str(self._secs) +  's Amount of Mines: '+ str(self._Mines) + ' BoardSize: ' + str(self._information[1]) + ' Difficulty: ' + str(self._information[2])

        # A long String of all The Information about the game just played

        File = open('MineSweeperScores.txt', 'a') # Opens File in Append Mode

        File.write(Text+'\n') # \n Means it will write to a new Line Next time

        File.close()
            
        


class Button():

    # Simple Button Class Needed for user input in User Interface using Pygame

    def __init__(self, Xpos, Ypos, image, scale):
        
        self._YPosition = Ypos
        self._XPosition = Xpos
        self._scale = float(scale)
        self._image = image

        
        width = image.get_width() # Gets Image Width
        height = image.get_height() # Gets Image Height
        self._image = pygame.transform.scale(self._image, (int(width * self._scale), int(height * self._scale))) # Transform Passed in Image to new Dimensions Based on the Scale, Doesnt Change Image Shape Only the Size on Screen
        self._rect = self._image.get_rect() # Defines the Rectangle (hitbox) of Image, Used in collisions with Mouse Position
        self._rect.topleft = (Xpos, Ypos) # When Displaying the Image it will Display from the Top left of the Rectangle where the coordinates specify
        

    def _checkForClick(self):

        # Very Simple Method that checks if the user clicks it

        Clicked = False
        MousePosition = pygame.mouse.get_pos() # Gets Position of Mouse
        if self._rect.collidepoint(MousePosition): # Checks if the Mouse collides with the Objects ( Button ) Rect ( Hitbox)
            if pygame.mouse.get_pressed()[0] == 1: # Checks that if the Left Mouse Button is pressed [0] = Left [1] = Middle [2] = Right
                Clicked = True
                
        return Clicked

    def _Draw(self, Screen):

        # Draws Button to Screen, Screen is passed in because there are Buttons need to appear on the main menu and on the gamescreen

        Screen.blit(self._image, (self._rect.x, self._rect.y))




class Tile(Button):

        # A Tile Inherits from Button class and uses shared attributes

        def __init__(self, x, y, image, scale, TileNumber, FlagOn, TileOn):

            super().__init__(x, y, image, scale)

            # Each Tile Has Unique Identifier

            self._TileNumber = TileNumber
            self._FlagOn = FlagOn
            self._TileOn = TileOn


        def _DisplayFlags(self):

            # If Flag is Set to True it means a Flag should be Displayed on the Tile

            if self._FlagOn == True:

                GameScreen.blit(FlagImg, (self._XPosition, self._YPosition))


        def _DisplayTiles(self):

            # If the tileOn is set to True it means the tile hasnt be clicked ( or adjacent empty tile hasnt been) so it should be displayed
            
            if self._TileOn == True:

                GameScreen.blit(self._image, (self._XPosition, self._YPosition))
                

# Create Main Menu Objects (Buttons), Create Main Menu Display


BeginnerButton = Button(20, 50, SelectBoxImg, 0.08)
IntermediateButton = Button(20, 70, SelectBoxImg, 0.08)
ExpertButton = Button(20, 90, SelectBoxImg, 0.08)
CustomButton = Button(20, 110, SelectBoxImg, 0.08)

TileLockOnButton = Button(150, 50, SelectBoxImg2, 0.08)
SaveScoreButton = Button(150, 90, SelectBoxImg2, 0.08)
StartTileButton = Button(150, 70, SelectBoxImg2, 0.08)

PlayButton = Button(300, 50, PlayButtonImg, 0.124)
QuitButton = Button(300, 100, QuitButtonImg, 0.124)

HeightInputButton = Button(70, 198, InputImg, 1)
WidthInputButton = Button(70, 175, InputImg, 1)
MineInputButton = Button(205, 195, InputImg, 1)
InputNameButton = Button(20, 10, InputNameImg, 1)

MenuScreenSize = (450, 250)
MainGameLoop = True

# MAIN PROGRAM

Name = 'Guest'


while MainGameLoop:

    MenuTick = 0
    MenuScreen = pygame.display.set_mode(MenuScreenSize)
    pygame.display.set_caption('Menu')

    pygame.font.init()
    
    Score = 0
    Mines = 25
    Difficulty = 2
    BoardWidth = 15
    BoardHeight = 20
    SaveButtonNum = 1
    TileLockOnNum = 1
    StartTileOnNum = 1
    Beginner = False
    Intermediate = True
    Expert = False
    Custom = False
    SaveScoreButtonOn = True
    TileLockOnButtonOn = True
    StartTileButtonOn = True
    FlagLock = True
    StartTile = True
    SaveScore = True

    # Run Main Menu To Get the Difficulty or Custom Details

    MainMenuLoop = True

    pygame.font.init()

    while MainMenuLoop:

        MenuScreen.fill((255, 255, 255))

        DisplayLeaderBoard(MenuScreen)

        Buttons = [PlayButton, QuitButton, BeginnerButton, IntermediateButton, ExpertButton, CustomButton, SaveScoreButton, StartTileButton, TileLockOnButton]

        for i in range(len(Buttons)):

            Buttons[i]._Draw(MenuScreen)
            
            if Buttons[i]._checkForClick() == True:
                if i == 0:
                    MainMenuLoop = False
                elif i == 1:
                    pygame.quit()
                    sys.exit()
                elif i == 2:
                    Beginner = True
                    Intermediate = False
                    Expert = False
                    Custom = False
                    Mines = 10
                    Difficulty = 1
                    BoardWidth = 8
                    BoardHeight = 10
                elif i == 3:
                    Beginner = False
                    Intermediate = True
                    Expert = False
                    Custom = False
                    Mines = 40
                    BoardWidth = 14
                    BoardHeight = 18
                    Difficulty = 2
                elif i == 4:
                    Beginner = False
                    Intermediate = False
                    Expert = True
                    Custom = False
                    Mines = 99
                    Difficulty = 3
                    BoardWidth = 20
                    BoardHeight = 24
                elif i == 5:
                    Beginner = False
                    Intermediate = False
                    Expert = False
                    Custom = True
                    Difficulty = 0
                    Mines = ''
                    Difficulty = ''
                    BoardWidth = ''
                    BoardHeight = ''
                elif i == 6:
                    time.sleep(0.25)      
                    SaveButtonNum +=1
                    if SaveButtonNum % 2 == 0:
                        SaveScoreButtonOn = False
                        SaveScore = False
                        
                    else:
                        SaveScoreButtonOn = True
                        SaveScore = True    
                elif i == 7:
                    time.sleep(0.25)
                    StartTileOnNum += 1
                    if StartTileOnNum % 2 == 0:
                        StartTileButtonOn = False
                        StartTile = False
                    else:
                        StartTileButtonOn = True
                        StartTile = True
                elif i == 8:
                    time.sleep(0.25)      
                    TileLockOnNum +=1
                    if TileLockOnNum % 2 == 0:
                        TileLockOnButtonOn = False
                        FlagLock = False
                    else:
                        TileLockOnButtonOn = True
                        FlagLock = True

        DisplayButtonDots(MenuScreen, DotImg, CrossImg, Beginner, Intermediate, Expert, Custom, SaveScoreButtonOn, TileLockOnButtonOn, StartTileButtonOn)

        Text1, Text2, Text3, Text4 = DisplayText(InputImg, MenuScreen, Mines, BoardWidth, BoardHeight)

        pygame.font.init()
        Font2 = pygame.font.Font('freesansbold.ttf', 15)

        NameDisplay = Font2.render(Name, True, (0, 0, 0))         

        Texts = [Text1, Text2, Text3, NameDisplay]

        MenuScreen.blit(InputNameImg, (20, 10))

        if InputNameButton._checkForClick() == True:

            Name = ''

            Done = False

            TypingImgIncrement = 0

            Name = FetchInputText('Alpha', 10, [25, 15], 'Name', Texts, MenuScreen)
   
        MenuScreen.blit(NameDisplay, (25, 15))

        if Custom == True:

            InputPlace = ''

            if HeightInputButton._checkForClick() == True:

                InputPlace = 'Height'
                
            if WidthInputButton._checkForClick() == True:

                InputPlace = 'Width'

            if MineInputButton._checkForClick() == True:

                InputPlace = 'Mines'
                
            Mines, BoardWidth, BoardHeight = CustomFetchText(InputPlace, Mines, BoardWidth, BoardHeight, FetchInputText, Texts, MenuScreen)
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

    Game = Board(boardSize, int(Mines))
    information = [Name, boardSize, Difficulty]
    Hud = HUD(boardSize, int(Mines), 0, information)
    Game._Name = Name
    Game._createGrid()
    Game._placeMines()
    Game._bombAlerts()

    # Setting up Game Screen Based of how many Tiles there are
    
    ScreenWidth = ((Game._boardSize[0]) * 24) + 10
    ScreenHeight = ((Game._boardSize[1]) * 24) + 55
    ScreenSize = (ScreenWidth, ScreenHeight)

    GameScreen = pygame.display.set_mode(ScreenSize)
    GameScreen.fill((168, 164, 164)) # Back Ground Colour of Tiles
    pygame.display.set_caption('Bomb Mopper!') # Window Caption

    # Create Necessary Objects

    RestartButton = Button((ScreenWidth/2)-18, 5, RestartImg, 1.85)

    GameLoop = True

    Clock = pygame.time.Clock()

    AllTiles = [] # Collection of Object Tiles


    for i in range(Game._boardSize[0]):

        for j in range(Game._boardSize[1]):
            
            AllTiles.append(Tile((24*i)+5, (24*j)+55, TileImg,1, (i, j), False, True))


    while GameLoop:

        # Check for WIN condition

        MinePos = Game._RecordedMinePositions

        RemainingTiles = []

        for i in range(len(AllTiles)):

            if AllTiles[i]._TileOn == True:

                RemainingTiles.append([AllTiles[i]._TileNumber[0], AllTiles[i]._TileNumber[1]])


        # Order Both Arrays and Check if they are the same

        MinePos2 = (MinePos).sort(key=lambda x:x[1])
        RemainingTiles2 = (RemainingTiles).sort(key=lambda x:x[1])


        if MinePos == RemainingTiles:

            WinOrLoss = True

            if SaveScore == True:

                Hud._RecordScore(WinOrLoss)
            
            DisplayAll(Game, GameScreen)
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

        AddFlag(AllTiles, Hud)
        
        # Remove Flags If they NOT on Tile, # Not needed if FlagLock is on

        if FlagLock == False:

            for i in range(len(AllTiles)):

                if AllTiles[i]._TileOn == False and AllTiles[i]._FlagOn == True:

                    AllTiles[i]._FlagOn = False

        # REMOVE Tiles
        
        Status, TileNum = RemoveTiles(AllTiles, FlagLock, Hud, Game)

        if Status == False:  # Loose Condition

            WinOrLoss = False

            if SaveScore == True:
                Hud._RecordScore(WinOrLoss)
                
            previousTick = pygame.time.get_ticks()
            DisplayAll(Game, GameScreen)
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

        RecordedEmptyTiles = RemoveAdjacentTiles(Game._Grid, AllTiles, TileNum, Game, Hud)

        AddExtraNumberTiles(AllTiles, RecordedEmptyTiles)

        # Display Grid

        DisplayAll(Game, GameScreen)

        # Display Tiles

        for i in range(len(AllTiles)):

            AllTiles[i]._DisplayTiles()
        

        # Display Flags

        for i in range(len(AllTiles)):

            AllTiles[i]._DisplayFlags()


        # Check For Restart

        RestartButton._Draw(GameScreen)
        
        if RestartButton._checkForClick() == True:
            
            previousTick = pygame.time.get_ticks()
            GameLoop = False
            MainMenuLoop = True
            DisplayAll(Game, GameScreen)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            del Game
            break


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()


        # Update Score And Clock, Display Score and Clock and Num of Flags and Bombs

        Hud._DisplayClock()
        Hud._DisplayScore()
        Hud._DisplayAmountOfFlagsandBombs()
        
        pygame.display.update() # Updates Display
    
        GameScreen.fill((168, 164, 164))  # Refreshes Game Screen For Display Updates

        Clock.tick(100) # Clock Tick
    




