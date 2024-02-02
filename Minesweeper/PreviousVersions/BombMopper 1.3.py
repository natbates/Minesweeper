import math, time, pygame, random, os, sys

pygame.init()

        #for i in range(len(Grid)):

            #print(Grid[i])
            #print('/n')

        #print('----------------------')

        #for i in range(len(FilledTiles)):

            #print(FilledTiles[i])
            #print('/n')



# Difficulty = int(input('Please Enter Difficulty 1) Easy 2) Medium 3) Hard: '))


class gameBoard():

    def __init__(self, boardSize, Difficulty, Mines):

        self.boardSize = boardSize
        self.Difficulty = Difficulty
        self.Mines = Mines
        self.Grid = []
        self.RecordedMinePositions = []

    def createGrid(self):


        for row in range(self.boardSize[1]):

            list = []

            for unit in range(self.boardSize[0]):
                list.append('0')

            self.Grid.append(list)

    def PlaceMines(self):

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
        return MinePositions

    def bombAlerts(self):

        for i in range(Mines):

            MinePosition = self.RecordedMinePositions[i]
            MinePositionY = MinePosition[1]
            MinePositionX = MinePosition[0]

            # print('Mines: ', Mines, 'Run : ', i+1)

            # print('Working on (X,Y) ',MinePositionX, MinePositionY)

            # print(self.Grid[0][7])
            # print(self.Grid[7][0])

            # self.Grid[Y][X]

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


# MAIN MENU ( Pick Difficulty )

class Button():

    def __init__(self, x, y, image, scale):

        self.scale = float(scale)
        self.y = y
        self.x = x
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def checkForClick(self, screen):

        Clicked = False
        MousePosition = pygame.mouse.get_pos()
        if self.rect.collidepoint(MousePosition):
            if pygame.mouse.get_pressed()[0] == 1:
                Clicked = True


        screen.blit(self.image, (self.rect.x, self.rect.y))
        return Clicked


# TEMP
Difficulty = 0
BoardSize = [0, 0]
Mines = 0

MenuScreen = pygame.display.set_mode((250, 410))

EasyImg = pygame.image.load(os.path.join('Assets', 'EasyButton.png'))
MediumImg = pygame.image.load(os.path.join('Assets', 'MediumButton.png'))
HardImg = pygame.image.load(os.path.join('Assets', 'HardButton.png'))
QuitImg = pygame.image.load(os.path.join('Assets', 'QuitButton.png'))

EasyDifficultyButton = Button(10, 10, EasyImg, 0.33)
MediumDifficultyButton = Button(10, 110, MediumImg, 0.33)
HardDifficultyButton = Button(10, 210, HardImg, 0.33)
QuitButton = Button(10, 310, QuitImg, 0.33)

pygame.display.set_caption('Main Menu')

run = True
while run:

    for event in pygame.event.get():

        if EasyDifficultyButton.checkForClick(MenuScreen) == True:

            Difficulty = 1
            run = False

        elif MediumDifficultyButton.checkForClick(MenuScreen) == True:

            Difficulty = 2
            run = False

        elif HardDifficultyButton.checkForClick(MenuScreen) == True:

            Difficulty = 3
            run = False

        elif QuitButton.checkForClick(MenuScreen) == True:

            pygame.quit()
            sys.exit()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

if Difficulty == 1:
    Mines = 5
    BoardSize = [6, 8]

elif Difficulty == 2:
    Mines = 40
    BoardSize = [12, 18]

elif Difficulty == 3:
    Mines = 200
    BoardSize = [45, 25]

game = gameBoard(BoardSize, Difficulty, Mines)  # Create Object

game.createGrid()  # Create an Empty Grid
MinePositions = game.PlaceMines()  # Place Mines Randomly on the Grid
game.bombAlerts()  # Add the Alerts that tell you how many bombs are near a square

# Final Product = game.Grid


# MAIN GAME

ScreenWidth = (BoardSize[0] * 24) + 10
ScreenHeight = (BoardSize[1] * 24) + 55
ScreenSize = (ScreenWidth, ScreenHeight)
gameScreen = pygame.display.set_mode(ScreenSize)



# Getting Information On the Screen

EmptyImg = pygame.image.load(os.path.join('Assets', 'Empty.png'))
OneImg = pygame.image.load(os.path.join('Assets', 'one.jpg'))
TwoImg = pygame.image.load(os.path.join('Assets', 'two.png'))
ThreeImg = pygame.image.load(os.path.join('Assets', 'three.jpg'))
FourImg = pygame.image.load(os.path.join('Assets', 'four.jpg'))
FiveImg = pygame.image.load(os.path.join('Assets', 'five.jpg'))
BombImg = pygame.image.load(os.path.join('Assets', 'bomb.png'))

TileX = 25
TileY = 25



EmptyImg = pygame.transform.scale(EmptyImg, (TileX, TileY))
OneImg = pygame.transform.scale(OneImg, (TileX, TileY))
TwoImg = pygame.transform.scale(TwoImg, (TileX, TileY))
ThreeImg = pygame.transform.scale(ThreeImg, (TileX, TileY))
FourImg = pygame.transform.scale(FourImg, (TileX, TileY))
FiveImg = pygame.transform.scale(FiveImg, (TileX, TileY))
BombImg = pygame.transform.scale(BombImg, (TileX, TileY))

PixelsPerLength = ScreenWidth / BoardSize[0]  # Both = 24
PixelsPerHeight = ScreenHeight / BoardSize[1]


gameScreen.fill((168, 164, 164))

    
Grid = game.Grid


clock = pygame.time.Clock()
pygame.display.set_caption('MineSweeper!')

TilesDeleted = []


class Tile(Button):

    def __init__(self, x, y, image, scale, Flag, name, BoardTotalTiles):

        self.name = name
        self.Flag = Flag

        self.BoardTotalTiles = BoardTotalTiles
        super().__init__(x, y, image, scale)


    def FlagTiles(self, FlaggedTiles):

        # Turn Flags On


        Mouse_Pos = pygame.mouse.get_pos()

        FlagsOn = []



        for i in range(len(FlaggedTiles)):

            for j in range(len(FlaggedTiles[0])):

                if FlaggedTiles[i][j] == '1':

                    FlagsOn.append([i, j])

            

        if pygame.mouse.get_pressed()[2] == 1:

            time.sleep(0.08)


            # Need To find What tile Mouse is in based of coordinates

            MouseXPosition = Mouse_Pos[0]
            MouseYPosition = Mouse_Pos[1]



            for i in range(len(Tiles)-1):


                
                if Tiles[i].rect.collidepoint(Mouse_Pos):


                    x = int(Tiles[i].name[0])
                    y = int(Tiles[i].name[1])

                    if [x, y] in FlagsOn:

                        FlaggedTiles[x][y] = '0'

                    else:

                        if FilledTiles[x][y] == '1':

                            FlaggedTiles[x][y] = '1'

                
                    return FlaggedTiles

    
            return FlaggedTiles

        else:

            return FlaggedTiles
        

    def RemoveFlags(self, FlaggedTiles, FilledTiles):

        
        FlagsOn = []

        EmptyTiles = []


        for i in range(len(FlaggedTiles)):

            for j in range(len(FlaggedTiles[0])):

                if FlaggedTiles[i][j] == '1':

                    FlagsOn.append([i, j])

                if FilledTiles[i][j] == '0':

                    EmptyTiles.append([i, j])


        Temp = []      

        for i in range(len(FlagsOn)):

            if FlagsOn[i] in EmptyTiles:

                x = FlagsOn[i][0]
                y = FlagsOn[i][1]

                FlaggedTiles[x][y] = '0'
                
        # Remove Flag Positions if they are on a Displayed Tile

        return FlaggedTiles

        

    def DisplayFlags(self, FlaggedTiles):


        for i in range(BoardSize[0]):

            
            for j in range(BoardSize[1]):
                    
                        
                if FlaggedTiles[i][j] == '1':


                    gameScreen.blit(FlagImg, ((i*24)+5, (j*24)+53))




    def DisplayNearNumbers(self, FilledTiles, EmptyTiles):


        for i in range(len(EmptyTiles)):

            x = EmptyTiles[i][0]
            y = EmptyTiles[i][1]

           # print('Start: ',x, y)

            if x - 1 > 0:

                #print('Left: ',x-1, y)

                FilledTiles[x-1][y] = '0'
  

            if x + 1 < BoardSize[0]:

                #print('Right: ',x+1, y)
                    
                FilledTiles[x+1][y] = '0'
            
                

            if y + 1 < BoardSize[1]:

                #print('Above: ',x, y+1)
                    
                FilledTiles[x][y+1] = '0'


            if y - 1 > 0:

                #print('Below: ',x, y-1)
                
                FilledTiles[x][y-1] = '0'

           

        return FilledTiles


    def RemoveNearTiles(self, ClickedTile, FilledTiles, Grid):

        

        x = ClickedTile[0]
        y = ClickedTile[1]

        NextTile = []
        Checked = []
        NextTile.append([x, y])

        
        while len(NextTile) > 0:

            x = NextTile[0][0]
            y = NextTile[0][1]

            print(NextTile)

            if x - 1 > 0:

                if Grid[y][x-1] == '0' and [x-1, y] not in Checked:

                    FilledTiles[x-1][y] = '0'
                    Checked.append([x-1, y])
                    NextTile.append([x-1, y])

            print('1')

            if x + 1 < BoardSize[0]:


                if Grid[y][x+1] == '0' and [x+1, y] not in Checked:

                    FilledTiles[x+1][y] = '0'
                    Checked.append([x+1, y])
                    NextTile.append([x+1, y])

            print('2')


            if y - 1 > 0:

                if Grid[y-1][x] == '0' and [x, y-1] not in Checked:

                    FilledTiles[x][y-1] = '0'
                    Checked.append([x, y-1])
                    NextTile.append([x, y-1])

            print('3')


            if y + 1 > BoardSize[1]:

                if Grid[y+1][x] == '0' and [x, y+1] not in Checked:

                    FilledTiles[x][y+1] = '0'
                    Checked.append([x, y+1])
                    NextTile.append([x, y+1])
                
            NextTile.pop(0)
                

        return FilledTiles

        
    def DisplayTiles(self, FilledTiles, Grid):

        for i in range(0, BoardSize[0]):

            for j in range(0, BoardSize[1]):

                try:

                    if FilledTiles[i][j] == '1':

                        gameScreen.blit(TileImg, ((24 * i)+5, (24 * j)+5+50))

                except:

                    pass

            
    def DisplayAll(self):

        for i in range(0, BoardSize[0]):

            for j in range(0, BoardSize[1]):

                if game.Grid[j][i] == 'X':

                    gameScreen.blit(BombImg, ((24 * i)+5, (24 * j)+5+50))

                elif game.Grid[j][i] == '0':

                    gameScreen.blit(EmptyImg, ((24 * i)+5, (24 * j)+5+50))

                elif game.Grid[j][i] == '1':

                    gameScreen.blit(OneImg, ((24 * i)+5, (24 * j)+5+50))

                elif game.Grid[j][i] == '2':

                    gameScreen.blit(TwoImg, ((24 * i)+5, (24 * j)+5+50))

                elif game.Grid[j][i] == '3':

                    gameScreen.blit(ThreeImg, ((24 * i)+5,  (24 * j)+5+50))

                elif game.Grid[j][i] == '4':

                    gameScreen.blit(FourImg, ((24 * i)+5, (24 * j)+5+50))

                elif game.Grid[j][i] == '5':

                    gameScreen.blit(FiveImg, ((24 * i)+5, (24 * j)+5+50))
                    

    def CheckCollisions(self, TilePositions, Tiles, FilledTiles):

        Mouse_Pos = pygame.mouse.get_pos()


        # Rule for Tilles is 24n + 5


        # Need to only allow user to click Tiles that are on!

        # Define TILES that are ON

        TilesOn = []


        for i in range(BoardSize[0]):

    
            for j in range(BoardSize[1]):
            
                
                if FilledTiles[i][j] == '1':


                    TilesOn.append([i, j])

        Continue = True


        if Mouse_Pos[0] <  5 or Mouse_Pos[0] > ScreenWidth- 5:

            Continue = False
            TilePositionXY = [-1, -1]
            return TilePositionXY

        if Mouse_Pos[1] <  5 or Mouse_Pos[1] > ScreenHeight- 5:

            Continue = False
            TilePositionXY = [-1, -1]
            return TilePositionXY
            

        if pygame.mouse.get_pressed()[0] == 1 and Continue == True:

            # Need To find What tile Mouse is in based of coordinates

            MouseXPosition = Mouse_Pos[0]
            MouseYPosition = Mouse_Pos[1]

            for i in range(len(TilePositions)):
                if Tiles[i].rect.collidepoint(Mouse_Pos):
                    
                    if pygame.mouse.get_pressed()[0] == 1:
                        TilePositions[i] = [-10, -10]

                    x = int(Tiles[i].name[0])
                    y = int(Tiles[i].name[1])


                    TilePositionXY = [x, y]

                    for i in range(len(TilesOn)):

                        if TilesOn[i] == TilePositionXY:

                             return TilePositionXY
                        
                    TilePositionXY = [-1, -1]
                    return TilePositionXY


        else:

            TilePositionXY = [-1, -1]

            return TilePositionXY


TileImg = pygame.image.load(os.path.join('Assets', 'Tile.png'))
TileImg = pygame.transform.scale(TileImg, (TileX, TileY))

FlagImg = pygame.image.load(os.path.join('Assets', 'Flag.png'))
FlagImg = pygame.transform.scale(FlagImg, (TileX, TileY))

Tiles = list()

TotalTiles = BoardSize[0]*BoardSize[1]

for i in range(BoardSize[0]):

    for j in range(BoardSize[1]):

        name = [i, j]

        Tiles.append(Tile((24*i)+5, (24*j)+55, TileImg, 1, False, name, TotalTiles))


# Display Tiles


run = True

Panel = Tile(-10, -10, TileImg,0.5,  False, 'GamePanel', TotalTiles)


TilePositions = []

for i in range(len(Tiles)):

    TilePositionX = Tiles[i].x
    TilePositionY = Tiles[i].y
    TilePosition = [TilePositionX, TilePositionY]
    TilePositions.append(TilePosition)


FilledTiles = []
FlaggedTiles = []
clickedTiles = [-1, -1]



for i in range(BoardSize[0]):

    OneList = []
    TwoList = []

    for j in range(BoardSize[1]):

        

        OneList.append('1')
        TwoList.append('0')

    FilledTiles.append(OneList)
    FlaggedTiles.append(TwoList)


Panel.DisplayTiles(FilledTiles, Grid)


FirstRun = 0

while run:

    #print('Tile Pattern : ',FilledTiles)

    if FirstRun > 0:

        # Check/Update Flags
        
        FlaggedTiles = Panel.FlagTiles(FlaggedTiles)
        FlaggedTiles = Panel.RemoveFlags(FlaggedTiles, FilledTiles)
        
        TilePositionXY = Panel.CheckCollisions(TilePositions, Tiles, FilledTiles)
        ClickedBox = TilePositionXY

        if len(ClickedBox)>0:

            if -1 in ClickedBox:
                pass
            else:
                x = ClickedBox[0]
                y = ClickedBox[1]
                try:
                    FilledTiles[x][y] = '0'

                    if [x, y] in MinePositions:

                        print('boom')
                        #gameScreen.blit(BombImg, ((x*24)+5.5, (y*24)+55))
                        #pygame.display.update()
                        #time.sleep(1)
                        #Panel.DisplayAll()
                        #pygame.display.update()
                        #time.sleep(5)
                        #pygame.quit()
                        #exit()
                        
                                            

                    if Grid[y][x] == '0':    
                        FilledTiles = Panel.RemoveNearTiles(ClickedBox, FilledTiles, Grid)
                    FilledTiles = Panel.DisplayNearNumbers(FilledTiles, EmptyTiles)

                except:
                    
                    pass

        
        # Only changes Filled Tiles
            
        Panel.DisplayAll()
        Panel.DisplayTiles(FilledTiles, Grid)
        Panel.DisplayFlags(FlaggedTiles)
            


    FirstRun += 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    pygame.display.update()
    clock.tick(30)
