import time, pygame, random, os, sys, math # Imports
# constants
TileX = 20
TileY = 20
backGroundColour = (212, 212, 212) # Sets background colour, will be used a lot

Rules = '''	
Rules:
The board is divided into cells, with mines randomly distributed. To win, you need to open all the cells.
The number on a cell shows the number of mines adjacent to it.
Using this information, you can determine cells that are safe, and cells that contain mines.
Cells suspected of being mines can be marked with a flag using the right mouse button.

Game Features:
The smiley face button is the restart button, this will bring you back to the main menu.
The blue number at the top is your score, this tells you what percentage of the board you have completed.
The red number below it is the time since you created the game.
If easy reset is on from the main menu settings, you can press middle mouse button to instantly restart with the same board settings

Menu Features:
You can create Custom games by pressing the custom difficulty and then entering in your values into the display buttons (press ENTER for each one after inputting).
The bar at the top allows you to sign in with your username then password.
The Create account buttons lets you create an account.
When you have signed into your account you can view your match history and your account statistics
'''

print(Rules) # Displays Rules to the User in case they need them

#load modules

os.chdir('Modules')


print(os.getcwd())

sys.path.append(os.getcwd())

from Load_Images import Load, Transform, loadHUDImage
###from Data_Base import AddToTable, SelectFromTable, clearAllFromTable, LogIn, CheckAvailability # Doesnt Work with newer python versions
from Menu_Procedures import setUpMenu, CreateButtons, FetchInputText#, LeaderBoard, CreateNewLogIn, AccountStatstics
from Game_Procedures import DisplayAll, RemoveTiles, AddFlag, RemoveAdjacentTiles, AddExtraNumberTiles
ListImages = Load() # Loads images
Images = Transform(ListImages, TileX, TileY) # Transforms Images to correct dimensions

class Board():
    # Class that generates a Binary Bit Map Of a Minesweeper Board, Also stores Time, Score and Name
    def __init__(self, boardSize, Mines):
        # Passed In Attributes
        self._boardSize = boardSize
        self._Mines = Mines
        self._startTile = []
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
        if self._Mines >= self._boardSize[0] * self._boardSize[1]: 
            self._Mines = (self._boardSize[0] * self._boardSize[1] ) - 1
        for i in range(self._Mines): # Loops for the amount of Mines Selected
            MineNotPlaced = True           
            while MineNotPlaced: # Continues Until Mine is Placed
                x = random.randint(0, self._boardSize[0] - 1) # Gets a Random Number between 0 and the BoardWidth
                y = random.randint(0, self._boardSize[1] - 1) # Gets a Random Number between 0 and the BoardHeight
                position = [x, y]
                if position in MinePositions or position == self._startTile: # Makes Sure Mines arent Placed in same Place Twice
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
    def __init__(self, boardSize, Mines, Difficulty, startingScore, ScreenSize):
        # Constants Attributes
        self._Difficulty = Difficulty
        self._TotalTiles = boardSize[0] * boardSize[1]
        self._EmptyTiles = 0
        self._Flags = []
        self._Mines = Mines
        # Static Attributes
        self._Score = float(startingScore)
        self._milliseconds = 0
        self._secs = 0
        self._mins = 0 
        self._ScreenWidth = ScreenSize[0]
        self._ScreenHeight = ScreenSize[1]

    def _DisplayClock(self, started, GameScreen, BackGroundImg):
        # Displays The Clock Digital (Minutes, Seconds)
        pygame.font.init() # Initalises Font
        if started == True:
            self._milliseconds += 1 # Increments Miliseconds Each time the clocks Ticks (100/s)
        if self._milliseconds == 100: # 10 Miliseconds in a Second
            self._secs += 1
            self._milliseconds = 0 # Resets
        if self._secs == 60: # Converts Seconds to Minutes
            self._mins += 1
            self._secs = 0
        text = str(self._mins) +':'+ str(self._secs)
        Font = pygame.font.Font('freesansbold.ttf', 25)
        Text = Font.render(text, True, (255, 0, 0)) # Renders Font
        GameScreen.blit(BackGroundImg, (self._ScreenWidth - 100, 70))
        GameScreen.blit(Text, (self._ScreenWidth - 95, 70)) # Displays The Text to the GameScreen
    def _DisplayAmountOfFlagsandBombs(self, GameScreen):
        # Displays the Amount of Mines left and Amount of Flags on the Board at the Top of the GameScreen
        Font = pygame.font.Font('freesansbold.ttf', 15)
        FlagNum = Font.render(str(len(self._Flags)), True, (255, 0, 0))
        MineNum = Font.render(str(self._Mines), True, (255, 0, 0))
        GameScreen.blit(FlagNum, (self._ScreenWidth-70, 105))
        GameScreen.blit(MineNum, (self._ScreenWidth-70, 130))
        GameScreen.blit(Images['FlagImg'], (self._ScreenWidth-100, 100)) # Displays Images of Flag
        GameScreen.blit(Images['BombMenuImg'], (self._ScreenWidth-100, 125))  # Displays Images of Bomb
    def _CalculateScore(self, Value):
        # Calculates Score, Called For each tile that is taken of the board, the Score resembles the percentage of the board complete, when it is 100% that means all the non-Mine tiles have been removed
        TilesRemoved = self._TotalTiles - Value # Value is the amount of remaning Tiles
        self._Score = round((TilesRemoved / (self._TotalTiles - int(self._Mines)))*100, 1)
    def _DisplayScore(self, GameScreen, BackGroundImg):
        # Displays Score on GameScreen, Had to be Seperate to Calculate Score otherwise each time its displayed it would Increment Score
        score = str(self._Score)
        Font = pygame.font.Font('freesansbold.ttf', 25)
        score = Font.render(score, True, (0, 0, 255))
        GameScreen.blit(BackGroundImg, (self._ScreenWidth - 100, 40))
        GameScreen.blit(score, (self._ScreenWidth-100, 40))
    def _RecordScore(self, MainMenu):
        # Called When game is Won
        Time = (self._mins * 60) + self._secs + self._milliseconds/100 # Calculates Time 
        if self._Difficulty != 'Custom':  
            AddToTable(self._Difficulty, MainMenu._PlayersID, Time, self._Score) # Adds to the Database Table Games 
class Menu():
    # Class for the Menu Screen
    def __init__(self, Settings, Images, Buttons, Screen):
        self._Difficulty = 'Intermediate' # Sets default starting Difficulty
        self._Settings = Settings
        self._Images = Images
        self._Buttons = Buttons
        self._Screen = Screen
        self._Name = 'Guest' # Sets Starting Default name as Guest
        self._PlayersID = -1
        pygame.font.init()
        Font = pygame.font.Font('freesansbold.ttf', 15)
        self._NameDisplay = Font.render(self._Name, True, (0, 0, 0)) # Renders Name
        self._Texts = []
        self._Mines = 40
        self._Width = 16
        self._Height = 16
    def _DifficultyToValues(self):
        # Gets values of Mines and Width and Height depending on the Difficulty
        if self._Difficulty == 'Beginner':
            self._Mines = 10
            self._Width = 10
            self._Height = 10
        if self._Difficulty == 'Intermediate':
            self._Mines = 40
            self._Width = 16
            self._Height = 16
        if self._Difficulty == 'Expert':
            self._Mines = 99
            self._Width = 16
            self._Height = 30
    def _CreateTexts(self):
        # Creates Texts to be Displayed on the Screen
        pygame.font.init()
        Font = pygame.font.Font('freesansbold.ttf', 15)
        Text1 = Font.render('Mines:     '+str(self._Mines), True, (0, 0, 0))
        Text2 = Font.render('Width:     '+str(self._Width), True, (0, 0, 0))
        Text3 = Font.render('Height:    '+str(self._Height), True, (0, 0, 0))
        Text4 = Font.render('Beginner', True, (0, 0, 0))
        Text5 = Font.render('Intermediate', True, (0, 0, 0))
        Text6 = Font.render('Expert', True, (0, 0, 0))
        Text7 = Font.render('Custom', True, (0, 0, 0))
        Text8 = Font.render('Tile LOCK', True, (0, 0, 0))
        Text9 = Font.render('Easy Reset', True, (0, 0, 0))
        Text10 = Font.render('Save Score', True, (0, 0, 0))
        self._NameDisplay = Font.render(self._Name, True, (0, 0, 0))
        self._Texts = [Text1, Text2, Text3, Text4, Text5, Text6, Text7, Text8, Text9, Text10] # Returns them as an Array for simplicity
    def _DisplayMenu(self):
        # Displays Images
        for i in range(len(self._Buttons)): # Draws all Buttons on Screen
            self._Buttons[i]._Draw(self._Screen)
        # Updates Dots on the Screen
        if self._Difficulty == 'Beginner':
            self._Screen.blit(self._Images['DotImg'], (20, 50))
        if self._Difficulty == 'Intermediate':
            self._Screen.blit(self._Images['DotImg'], (20, 70))
        if self._Difficulty == 'Expert':
            self._Screen.blit(self._Images['DotImg'], (20, 90))
        if self._Difficulty == 'Custom':
            self._Screen.blit(self._Images['DotImg'], (20, 110))
        # Displays All the Texts
        self._Screen.blit(self._Texts[0], (150, 200))
        self._Screen.blit(self._Texts[1], (10, 180))
        self._Screen.blit(self._Texts[2], (10, 200))
        j = 50
        for i in range(3, 7):
            self._Screen.blit(self._Texts[i], (40, j))
            j += 20
        j = 50
        for i in range(7, 10):
            self._Screen.blit(self._Texts[i], (180, j))
            j += 20
        self._Screen.blit(self._NameDisplay, (25, 15))
        j = 50
        for i in range(0, len(self._Settings)):
            if self._Settings[i] == True:
                self._Screen.blit(Images['CrossImg'], (150, j))
            j+=20
    def _CheckForClicks(self):
        # Checks which Buttons have been pressed       
        TileLock =  self._Settings[0]
        EasyReset = self._Settings[1]
        SaveScore = self._Settings[2]
        LeaderBoardDisplayOn = False
        Continue = True
        CreatedAccount = False
        for i in range(len(self._Buttons)):      
            if self._Buttons[i]._checkForClick() == True:
                time.sleep(0.2) # Delay so you dont instantly repress the button
                if i == 0:
                    self._Difficulty = 'Beginner' # If the Beginner Button is pressed it sets the Difficulty to Beginner
                if i == 1:
                    self._Difficulty = 'Intermediate'
                if i == 2:
                    self._Difficulty = 'Expert'
                if i == 3:
                    self._Difficulty = 'Custom'
                if i == 4:
                    if TileLock == True: # Makes it act as a Button, If its already on and it is clicked it turns it off
                        TileLock = False
                    else:
                        TileLock = True
                if i == 5:
                    if SaveScore == True:
                        SaveScore = False
                    else:
                        SaveScore = True
                if i == 6:
                    if EasyReset == True:
                        EasyReset = False
                    else:
                        EasyReset = True
                if i == 7: # Play Game
                    self._Screen.fill((255, 255, 255)) # Refreshes Screen
                    self._Screen.blit(self._Images['PlayButtonPressedImg'], (300, 60)) # Animation for button 
                    pygame.display.update()
                    time.sleep(0.5)
                    Continue = False
                if i == 8: # Quits Game
                    self._Screen.fill((255, 255, 255))
                    self._Screen.blit(self._Images['QuitButtonPressedImg'], (300, 160)) 
                    pygame.display.update()
                    time.sleep(0.2)
                    pygame.quit()
                    sys.exit()
                if i == 12:
                    NameDisplay = ''
                    # Name can only have 15 Characters
                    self._Name = FetchInputText('Both', 15, [25, 15], 'Name', self._Texts, self._Screen, self._Images, self._NameDisplay, self._Buttons) # Fetches User input for Name
                    Exists = CheckAvailability(self._Name)
                    if Exists == False: # If the name Exists then there is an account
                        Password = FetchInputText('Both', 20, [25, 18], 'Password', self._Texts, self._Screen, self._Images, self._NameDisplay, self._Buttons) # Fetches User input for Password
                        PlayerID, Username, CorrectDetails = LogIn(self._Name, Password) # trys to log into account
                        self._PlayersID = PlayerID
                        if CorrectDetails == False: # if they get the username and password wrong it resets the name back to guest
                            print('Password incorrect')
                            self._Name = 'Guest'
                    else:
                        print('Name doesnt exist') # if there is no account it resets the name
                        self._Name = 'Guest'
   
                if i == 13: # Opens up leaderboard if leaderboard button pressed
                    self._Screen.fill((255, 255, 255))
                    self._Screen.blit(self._Images['LeaderBoardPressedImg'], (300, 110))
                    pygame.display.update()
                    time.sleep(0.5)
                    LeaderBoardDisplayOn = True
                if i == 14:
                    CreateNewLogIn(Images, Button) # Opens new account menu
                    pygame.quit()
                    CreatedAccount = True
        self._Settings = [TileLock, EasyReset, SaveScore] # Simplifies all the Settings into one Array   
        return Continue, LeaderBoardDisplayOn, CreatedAccount
    def GetCustomSizes(self):
        # Gets Custom size for size for mines, height and width
        Values = [50, 10] # Sets max and min size for both Height and Width
        if self._Buttons[9]._checkForClick() == True: 
            self._Height = FetchInputText('Digits', 2, [80, 203], 'Height', self._Texts, self._Screen, self._Images, self._NameDisplay, self._Buttons)
            if len(self._Height) > 0: # If they have inputed something:
                if int(self._Height) > 50 or int(self._Height)  < 10:
                    self._Height = min(Values, key=lambda x:abs(x-int(self._Height))) # Rounds it to closest value, either max or min, if they enter a value that is not acceptapted within the bounds         
            else:
                self._Height = 10
        if self._Buttons[10]._checkForClick() == True:
            self._Width = FetchInputText('Digits', 2, [80, 179], 'Width', self._Texts, self._Screen, self._Images, self._NameDisplay, self._Buttons)
            if len(self._Width) > 0:
                if int(self._Width) > 50 or int(self._Width)  < 8:
                    self._Width = min(Values, key=lambda x:abs(x-int(self._Width)))
            else:
                self._Width = 8
        if self._Buttons[11]._checkForClick() == True:
            self._Mines = FetchInputText('Digits', 3, [210, 200], 'Mines', self._Texts, self._Screen, self._Images, self._NameDisplay, self._Buttons)
            if len(self._Mines) == 0: # if its empty make it 0
                self._Mines = 0
class Button():
    # Simple Button Class Needed for user input in User Interface using Pygame
    def __init__(self, Xpos, Ypos, image, scale):
        self._YPosition = Ypos
        self._XPosition = Xpos
        self._scale = float(scale)
        self._Unscaledimage = image
        width = image.get_width() # Gets Image Width
        height = image.get_height() # Gets Image Height
        self._image = pygame.transform.scale(self._Unscaledimage, (int(width * self._scale), int(height * self._scale))) # Transform Passed in Image to new Dimensions Based on the Scale, Doesnt Change Image Shape Only the Size on Screen
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
        def _DisplayFlags(self, GameScreen):
            # If Flag is Set to True it means a Flag should be Displayed on the Tile
            if self._FlagOn == True:
                GameScreen.blit(Images['FlagImg'], (self._XPosition, self._YPosition))
        def _DisplayTiles(self, GameScreen):
            # If the tileOn is set to True it means the tile hasnt be clicked ( or adjacent empty tile hasnt been) so it should be displayed
            if self._TileOn == True:
                GameScreen.blit(self._image, (self._XPosition, self._YPosition))
            else: # If the Tile is off, the flag must also be off
                self._FlagOn = False


def AccountStatsTextDisplay(GlobalStats, PlayerStats, AcountStatisticsMenu, PlayerName, Difficulty):
    pygame.font.init()
    Font = pygame.font.Font('freesansbold.ttf', 9)
    # Prints Texts in different colours to show which option is selected
    if Difficulty == 'Beginner':
        BeginnerText = Font.render('Beginner', True, (0, 200, 0))
    else:
        BeginnerText = Font.render('Beginner', True, (0, 0, 0))
    if Difficulty == 'Intermediate':
        IntermediateText = Font.render('Intermediate', True, (0, 200, 0))
    else:
        IntermediateText = Font.render('Intermediate', True, (0, 0, 0))
        
    if Difficulty == 'Expert':
        ExpertText = Font.render('Expert', True, (0, 200, 0))
    else:
        ExpertText = Font.render('Expert', True, (0, 0, 0))

    AcountStatisticsMenu.blit(BeginnerText, (165, 15))
    AcountStatisticsMenu.blit(IntermediateText, (245, 15))
    AcountStatisticsMenu.blit(ExpertText, (325, 15))

    # Organises Data for Player and Global stats
    GlobalTotalGamesPlayed = Font.render('Global Games Played '+str(GlobalStats[0]), True, (0, 0, 0))
    GlobalTotalGamesWon = Font.render('Global Games Won: '+str(GlobalStats[1]), True, (0, 0, 0))
    GlobalTotalGamesLost = Font.render('Global Games Lost: '+str(GlobalStats[0] - GlobalStats[1]), True, (0, 0, 0))
    Font = pygame.font.Font('freesansbold.ttf', 15)
    PlayerName = Font.render('PlayerName: '+PlayerName, True, (0, 0, 0))
    AcountStatisticsMenu.blit(GlobalTotalGamesPlayed, (395, 5))
    AcountStatisticsMenu.blit(GlobalTotalGamesWon, (395, 15))
    AcountStatisticsMenu.blit(GlobalTotalGamesLost, (395, 25))
    AcountStatisticsMenu.blit(PlayerName, (20, 10))

    Font = pygame.font.Font('freesansbold.ttf', 12)
    PlayerTotalGamesPlayed = Font.render('Total Games Played: '+str(PlayerStats[2]), True, (0, 0, 0))
    PlayerTotalGamesWon = Font.render('Games Won: '+str(PlayerStats[0]), True, (0, 0, 0))
    PlayerTotalGamesLost = Font.render('Games Lost: '+str(PlayerStats[1]), True, (0, 0, 0))
    AccountCreated = str(PlayerStats[3])
    AccountCreated = AccountCreated.replace('(datetime.datetime(', '')
    AccountCreated = AccountCreated.replace('),)', '')
    PlayerAccountCreated = Font.render('Account Created: '+str(AccountCreated), True, (0, 0, 0))
    if PlayerStats[2] > 0 and PlayerStats[1] > 0:
        Ratio = round((PlayerStats[0]/PlayerStats[2]*100), 1)
        PlayerWinRatio = Font.render('Win:Loss Ratio: '+str(Ratio), True, (0, 0, 0))
        AcountStatisticsMenu.blit(PlayerWinRatio, (20, 210))

    # Displays info on screen
    AcountStatisticsMenu.blit(PlayerTotalGamesPlayed, (20, 50))
    AcountStatisticsMenu.blit(PlayerTotalGamesWon, (20, 90))
    AcountStatisticsMenu.blit(PlayerTotalGamesLost, (20, 130))
    AcountStatisticsMenu.blit(PlayerAccountCreated, (20, 170))

    # Draw a pie chart of Wins and Losses

    if PlayerStats[2] > 0 and PlayerStats[1] > 0:

        CentreX, CentreY, Radius = 390, 190, 75 # sets raidus and centre of pi chart
        pygame.draw.circle(AcountStatisticsMenu, (255, 0, 0), (CentreX, CentreY), Radius) # draws RED circle at centre coorddinates
        Ratio = Ratio / 100 
        angle = int(round(360 * Ratio, 0)) # calculates angle, How much of the circle represents the win/loss percentage ( circle = 360 degrees)
        p = [(CentreX, CentreY)] # sets centre
        for n in range(0, angle):
            x = CentreX + int(Radius*math.cos(n*math.pi/180)) # figures out X coordinate
            y = CentreY + int(Radius*math.sin(n*math.pi/180)) # figures out X coordinate
            p.append((x, y))
        p.append((CentreX, CentreY))
        if len(p) > 2: # points argument must contain more than 2 points
            pygame.draw.polygon(AcountStatisticsMenu, (0, 255, 0), p) # draws several polynomials FROM centre so it looks like a Sector
    
def LeaderBoardTextDisplay(LeaderBoardButtons, LeaderBoardSettings, LeaderBoardDisplay):
    # Displays Info on the LeaderBoard
    for i in range(len(LeaderBoardButtons)):
        LeaderBoardButtons[i]._Draw(LeaderBoardDisplay) # Draws all leader board buttons
    if LeaderBoardButtons[0]._checkForClick() == True: # Checks for clicks for each of the buttons and then carries out function
        LeaderBoardSettings[0] = 'Beginner'
    if LeaderBoardButtons[1]._checkForClick() == True:
        LeaderBoardSettings[0] = 'Intermediate'
    if LeaderBoardButtons[2]._checkForClick() == True:
        LeaderBoardSettings[0] = 'Expert'
    if LeaderBoardButtons[3]._checkForClick() == True:
        LeaderBoardSettings[1] = 'Time'
    if LeaderBoardButtons[4]._checkForClick() == True:
        LeaderBoardSettings[1] = 'Date' 
    Font = pygame.font.Font('freesansbold.ttf', 10)   # This chunck of code makes the text green if the button has been clicked or is default button 
    if LeaderBoardSettings[0] == 'Beginner':
        BeginnerText = Font.render('Beginner', True, (0, 200, 0))
    else:
        BeginnerText = Font.render('Beginner', True, (0, 0, 0))
    if LeaderBoardSettings[0] == 'Intermediate':
        IntermediateText = Font.render('Intermediate', True, (0, 200, 0))
    else:
        IntermediateText = Font.render('Intermediate', True, (0, 0, 0))
    if LeaderBoardSettings[0] == 'Expert':
        ExpertText = Font.render('Expert', True, (0, 200, 0))
    else:
        ExpertText = Font.render('Expert', True, (0, 0, 0))

    if LeaderBoardSettings[1] == 'Time':
        TimeText = Font.render('Time', True, (0, 200, 0))
    else:
        TimeText = Font.render('Time', True, (0, 0, 0))

    if LeaderBoardSettings[1] == 'Date':
        DateText = Font.render('Date', True, (0, 200, 0))
    else:
        DateText = Font.render('Date', True, (0, 0, 0))  
    LeaderBoardDisplay.blit(TimeText, (283, 15)) # Displays all Texts
    LeaderBoardDisplay.blit(DateText, (363, 15))
    LeaderBoardDisplay.blit(BeginnerText, (25, 15))
    LeaderBoardDisplay.blit(IntermediateText, (103, 15))
    LeaderBoardDisplay.blit(ExpertText, (190, 15))
    
def Main(Images, ListImages, TileX, TileY):
    Games = []
    x = -1
    MainGameLoop = True
    QuickReset = False
    MainMenuLoop = True
    Buttons, LeaderBoardButtons, AccountStatisticButtons = CreateButtons(Images, Button) # Creates Main Menu Button objects, only needs to be done once
    Settings = [True, True, True] # Sets the default settings outside the Menu Loop so it doesnt saves the changed settings each time you restart the game
    Continue = True
    MenuScreen = setUpMenu()
    MainMenu = Menu(Settings, Images, Buttons, MenuScreen)
    AcountStatisticsButton = Button(300, 12, Images['AccountStatsImg'], 0.1) # Cant be in create Buttons procedure as that displays all the buttons as well
    GameHistoryButton = Button(20, 250, Images['GameHistroyImg'], 0.14)
    while MainGameLoop: # Main game Loop
        x = x + 1
        pygame.quit()
        MenuScreen = setUpMenu()
        MainMenu._Screen = MenuScreen
        if QuickReset == True: # Resets the Quick Reset
            MainMenuLoop = False # Skips main menu
            QuickReset = False
        else:
            MainMenuLoop = True
        while MainMenuLoop: # Main Menu Loop
            MainMenu._DifficultyToValues() # Converts the Difficulty into Values ( Mines, Height and Width )
            MainMenu._CreateTexts() # Creates/Updates Texts
            MenuScreen.fill((255, 255, 255)) # Refreshes Screen
            MainMenu._DisplayMenu() # Displays Things on the Menu
            Continue, LeaderBoardDisplayOn, CreatedAccount  = MainMenu._CheckForClicks()
            if CreatedAccount == True:
                MenuScreen = setUpMenu()
                MainMenu._Screen = MenuScreen # Redefines Menu
            if MainMenu._Difficulty == 'Custom':
                 MainMenu.GetCustomSizes() # if the difficulty is custom, it calls this procedure which checks if any custom buttons are pressed
            if MainMenu._Name != 'Guest':
                AcountStatisticsButton._Draw(MainMenu._Screen)
                if AcountStatisticsButton._checkForClick():
                    AcountStatisticsMenu = pygame.display.set_mode((550, 300))
                    AcountStatisticsLoop = True
                    AccountStatisticSetting = 'Beginner'
                    while AcountStatisticsLoop:
                        AcountStatisticsMenu.fill((255, 255, 255)) # refreshes screen
                        for i in range(len(AccountStatisticButtons)): # Draws all Statistic menu buttons
                            AccountStatisticButtons[i]._Draw(AcountStatisticsMenu) # Draws all leader board buttons
                        if AccountStatisticButtons[0]._checkForClick() == True: # Checks for clicks for each of the buttons and then carries out function
                            AccountStatisticSetting = 'Beginner'
                        if AccountStatisticButtons[1]._checkForClick() == True:
                            AccountStatisticSetting = 'Intermediate'
                        if AccountStatisticButtons[2]._checkForClick() == True:
                            AccountStatisticSetting = 'Expert'
                        pygame.display.set_caption('Account Statistics') # Window Caption
                        GameHistoryLoop = False
                        GameHistoryButton._Draw(AcountStatisticsMenu)
                        GlobalStats, PlayerStats = AccountStatstics(MainMenu._PlayersID, AccountStatisticSetting)
                        AccountStatsTextDisplay(GlobalStats, PlayerStats, AcountStatisticsMenu, MainMenu._Name, AccountStatisticSetting)
                        if GameHistoryButton._checkForClick() == True:
                            GameHistoryLoop = True
                            pygame.display.set_caption('GameHistory') # Changes Window Caption
                        while GameHistoryLoop:
                            AcountStatisticsMenu.fill((255, 255, 255))
                            pygame.font.init()
                            Font = pygame.font.Font('freesansbold.ttf', 12)
                            done = False
                            GameHistory = PlayerStats[4]
                            GameHistory = GameHistory.replace("')", "")
                            # Organise One long string into List
                            Data = []
                            i = 0
                            Loops = GameHistory.count("datetime.datetime(") # there is 1 of these per row
                            if Loops > 0:
                                for j in range(Loops+1):
                                    Temp = ''
                                    i = i + 2
                                    while GameHistory[i] != ')' and GameHistory[i+1] != ')': # loops through the long singular string and seperates it when it finds '))'
                                        Temp = Temp + str(GameHistory[i])
                                        i = i + 1
                                    Temp = Temp.replace("Decimal('", "")
                                    Temp = Temp.replace("datetime.datetime", "") # Clears unneeded text
                                    Temp = Temp.replace("(", "")
                                    Data.append(Temp)
                                filter(None, Data)
                                filter(None, Data)
                                for i in range(len(Data)):
                                    Text = Font.render(str(Data[i]), True, (0, 0, 0)) 
                                    AcountStatisticsMenu.blit(Text, (10, (20*i)+10)) # displays data on new lines on display
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT: # if the player quits the menu via the top right cross
                                    GameHistoryLoop = False
                            pygame.display.update()
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: # if the player quits the menu via the top right cross
                                AcountStatisticsLoop = False
                                pygame.quit() # Closes the window
                                MenuScreen = setUpMenu() # Sets up Menu again
                                MainMenu._Screen = MenuScreen # Redefines Menu
            if LeaderBoardDisplayOn == True:
                LeaderBoardDisplay = pygame.display.set_mode((450, 600)) # sets up leaderboard display
                LeaderBoardSettings = ['Beginner', 'Time'] # Default starting Settings
                pygame.display.set_caption('LeaderBoard') # Window Caption
            while LeaderBoardDisplayOn == True: # leaderboard Loop
                LeaderBoardDisplay.fill((255, 255, 255))
                LeaderBoardTextDisplay(LeaderBoardButtons, LeaderBoardSettings, LeaderBoardDisplay) # Deals with buttons and Text, also displays them on the menu
                Data = SelectFromTable(LeaderBoardSettings[0], LeaderBoardSettings[1]) # Which Difficulty and what to Order them by ( time or Date played )
                LeaderBoard(LeaderBoardSettings, Data, LeaderBoardDisplay) # Displays The leaderboard on the Leaderboard Display, Allows them to order by last played or how fast the player won (main/default) and which Difficulty
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # if the player quits the menu via the top right cross
                        LeaderBoardDisplayOn = False
                        pygame.quit() # Closes the window
                        MenuScreen = setUpMenu() # Sets up Menu again
                        MainMenu._Screen = MenuScreen # Redefines Menu
            if Continue == False:
                MainMenuLoop = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        MainMenu._DifficultyToValues() # Converts back from the settings Array into the individual variables
        FlagLock = MainMenu._Settings[0]
        EasyReset = MainMenu._Settings[1]
        SaveScore = MainMenu._Settings[2]
        pygame.quit() # Closes Menu Screen
        MenuTick = pygame.time.get_ticks() # Gets how long you spent in the Menu to make the clock work 
        boardSize = (int(MainMenu._Width), int(MainMenu._Height))
        Game = Board(boardSize, int(MainMenu._Mines)) # creates Game object, this will be used for creating and setting up the game
        Games.append(Game)
        Games[x]._createGrid() # creates the empty grid for the board
        # Setting up Game Screen Based of how many Tiles there are
        ScreenWidth = ((Games[x]._boardSize[0]) * 24) + 80
        ScreenHeight = ((Games[x]._boardSize[1]) * 21) + 5
        ScreenSize = (ScreenWidth, ScreenHeight)
        HUDImg, BackGroundImg = loadHUDImage(ScreenWidth, ScreenHeight, MainMenu._Difficulty) # Loads images for the HUD
        GameScreen = pygame.display.set_mode(ScreenSize) # Defines the GameScreen
        if MainMenu._Difficulty == 'Beginner':
            ScreenWidth = ScreenWidth + 10
        GameHud = HUD(boardSize, MainMenu._Mines, MainMenu._Difficulty, 0, (ScreenWidth, ScreenHeight)) # Creates the HUD, this is used for display things on the GameScreen to the player e.g clock, score
        RestartButton = Button((ScreenWidth-100), 150, Images['RestartImg'], 0.05) # Creates Restart Button
        GameScreen.fill(backGroundColour) # Back Ground Colour
        pygame.display.set_caption('Minesweeper!') # Window Caption
        AllTiles = []
        for i in range(Games[x]._boardSize[0]):
            for j in range(Games[x]._boardSize[1]):
                AllTiles.append(Tile((TileX*i)+5, (TileY*j)+10,Images['TileImg'],1, (i, j), False, True)) # Creates and adds Tile objects (which act as buttons) to a list
        Clock = pygame.time.Clock() # Creates Clock
        GameLoop = True
        started = False # Doesnt start timer until first click
        Clicks = 0 # Sets amount of clicks to 0, this will be used to create the mine positions after the first click to avoid the first click being a mine
        while GameLoop:
            GameScreen.blit(HUDImg, ((boardSize[0]*21), 10)) # Displays HUD background
            AddFlag(AllTiles, GameHud) # Checks if the player adds/removes a Flag
            Status, TileNum, Clicks, FirstClick = RemoveTiles(AllTiles, FlagLock, GameHud, Games[x], Clicks, Button) # Removes a Tile based of where the user clicks
            if FirstClick == True: # if the its the users first click it generates the mines avoiding the starting tile
                Games[x]._startTile = TileNum
                Games[x]._placeMines() # places the mines on the grid
                Games[x]._bombAlerts() # increments the numbers around every mine on the grid#
                started = True # starts clock
            if Status == False: # if the user clicked a Tile with a bomb under it
                # Loose Condition
                if SaveScore == True:
                    GameHud._RecordScore(MainMenu)
                GameScreen.fill((255, 0, 0)) # Flashes Red
                pygame.display.update()
                time.sleep(0.3)
                GameScreen.fill(backGroundColour) # Back Ground Colour
                GameScreen.blit(HUDImg, ((boardSize[0]*21), 10))
                GameScreen.blit(Images['LooseImg'], ((boardSize[0]*21)+15, 150)) # Displays Loose Image on the HUD
                DisplayAll(Game, GameScreen, Images, TileX, TileY) # Displays the grid under the Tiles
                GameHud._DisplayClock(started, GameScreen, BackGroundImg) # shows the player the time they got
                GameHud._DisplayScore(GameScreen, BackGroundImg) # shows the player the score they got
                GameHud._DisplayAmountOfFlagsandBombs(GameScreen) # shows the player how many flags they had placed and how many bombs there were
                pygame.display.update()
                GameLoop = False
                NextGameLoop = True
                while NextGameLoop:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: # if they press a button on the keyboard it restarts
                            NextGameLoop = False
                        elif pygame.mouse.get_pressed()[1] == True: # if they press the middle mouse button it restarts without going to the main menu and keeps the same settings
                            NextGameLoop = False
                            QuickReset = True
                        elif event.type == pygame.QUIT: # if they press the red cross it closes the program
                            pygame.quit()
                            quit() # quits whole program
                break
            else:
                RecordedEmptyTiles = RemoveAdjacentTiles(Game._Grid, AllTiles, TileNum, Games[x], GameHud) # Removes adjacent empty Tiles
            RemainingTiles = []
            for i in range(len(AllTiles)):
                if AllTiles[i]._TileOn == True:
                    RemainingTiles.append([AllTiles[i]._TileNumber[0], AllTiles[i]._TileNumber[1]]) # Adds all Tiles that are on into an array 
            Value = len(RemainingTiles)
            GameHud._CalculateScore(Value) # calculates score (percent completed) based on how many tiles are left to click
            # Order Both Arrays and Check if they are the same

            Games[x]._RecordedMinePositions = sorted(Game._RecordedMinePositions)
            RemainingTiles = sorted(RemainingTiles)
            
            if Game._RecordedMinePositions == RemainingTiles: # if they are the same, it means the only remaining tiles that are on are the Mines so the player wins
                # Win Condition
                if SaveScore == True:
                    GameHud._RecordScore(MainMenu)
                GameScreen.fill((0, 255, 0)) # Flashes Green
                pygame.display.update()
                time.sleep(0.3)
                GameScreen.fill(backGroundColour) # Back Ground Colour
                GameScreen.blit(HUDImg, ((boardSize[0]*21), 10))
                GameScreen.blit(Images['WinImg'], ((boardSize[0]*21)+5, 150)) # Displays Win Image on the HUD
                DisplayAll(Game, GameScreen, Images, TileX, TileY)
                GameHud._DisplayClock(started, GameScreen, BackGroundImg)
                GameHud._DisplayScore(GameScreen, BackGroundImg)
                GameHud._DisplayAmountOfFlagsandBombs(GameScreen)
                GameLoop = False
                pygame.display.update()
                GameLoop = False
                NextGameLoop = True
                while NextGameLoop:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            NextGameLoop = False
                        elif pygame.mouse.get_pressed()[1] == True:
                            NextGameLoop = False
                            QuickReset = True
                        elif event.type == pygame.QUIT:
                            NextGameLoop = False
                            
                break       
            AddExtraNumberTiles(AllTiles, RecordedEmptyTiles) # Displays the Tiles above, below, right and left of each empty tile to show the number tile
            RestartButton._Draw(GameScreen) # draws the restart button
            # Display Grid then overlaps the tiles that are ON above it so you can see gaps in it
            DisplayAll(Games[x], GameScreen, Images, TileX, TileY)
            for i in range(len(AllTiles)):
                AllTiles[i]._DisplayTiles(GameScreen) # Display Tiles
                AllTiles[i]._DisplayFlags(GameScreen) # Display Flags
            GameHud._DisplayClock(started, GameScreen, BackGroundImg) # Display clock
            GameHud._DisplayScore(GameScreen, BackGroundImg) # Display Score
            GameHud._DisplayAmountOfFlagsandBombs(GameScreen) # Displays Flags placed and Amount of bombs in grid
            pygame.display.update() # Updates Display
            Clock.tick(100) # Clock Tick
            for event in pygame.event.get():
                if Clicks >= 0:
                    if pygame.mouse.get_pressed()[1] == True: # Checks that if the Left Mouse Button is pressed [0] = Left [1] = Middle [2] = Right
                        if EasyReset == True:
                            if Clicks > 0 : # if they restart the game and havent clicked anything, there wont be any mines under the tiles as the grid is only created after the first click to avoid the first click being a mine
                                DisplayAll(Games[x], GameScreen, Images, TileX, TileY) # Displays all as game is over so you can see where the mines were
                                pygame.display.update()
                                time.sleep(2)
                            GameLoop = False
                            QuickReset = True # Sets QuickReset to TRUE meaning you skip the Menu selection part and all your chosen settings remain the same and you are start a new game right away
                    if RestartButton._checkForClick() == True:
                        if Clicks > 0:
                            DisplayAll(Games[x], GameScreen, Images, TileX, TileY) # Displays all as game is over so you can see where the mines were
                            pygame.display.update()
                            time.sleep(1)
                        GameLoop = False
                    if event.type == pygame.QUIT: # Closes Program
                        GameLoop = False
                        pygame.quit()
                        sys.exit
                        
if __name__ == '__main__':
    Main(Images, ListImages, TileX, TileY) # Passes in Images 
