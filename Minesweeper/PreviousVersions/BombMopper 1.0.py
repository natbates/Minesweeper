import math, time, pygame, random, os, sys

pygame.init()




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
    Mines = 10
    BoardSize = [10, 10]

elif Difficulty == 2:
    Mines = 40
    BoardSize = [12, 18]

elif Difficulty == 3:
    Mines = 1000
    BoardSize = [100, 100]

game = gameBoard(BoardSize, Difficulty, Mines)  # Create Object

game.createGrid()  # Create an Empty Grid
game.PlaceMines()  # Place Mines Randomly on the Grid
game.bombAlerts()  # Add the Alerts that tell you how many bombs are near a square

# Final Product = game.Grid


# MAIN GAME

ScreenWidth = (BoardSize[0] * 24) + 10
ScreenHeight = (BoardSize[1] * 24) + 10
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


    def RemoveFlagTile(self):

        pass


    def RemoveNearTiles(self, ClickedTile, FilledTiles, Grid):

        x = ClickedTile[0]
        y = ClickedTile[1]

        if x == -1 and y == -1:

            pass

        else:


            # Compare Graphs GRID and FilledTiles

            #for i in range(len(Grid)):

                #print(str(Grid[i]) + '\n')


            Show = []

            for i in range(len(FilledTiles)):

                Inverted = []

                for j in range(len(FilledTiles[0])):

                
                    Inverted.append(str(FilledTiles[j][i]))

                Show.append(Inverted)

            for i in range(len(Show)):

                #print(str(Show[i]) + '\n')
                pass



            #NearbyTiles = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]

            i = 0                

            # Grid[y][x]

            z = x
            x = y
            y = z

            NextTile = []

            NextTile.append([x, y]) #STARTING PANE;

            complete = False
            continues = False

            n = 0

            while complete == False:

                try:

                    x = NextTile[n][0]
                    y = NextTile[n][1]

                except:

                    continues = False
                

                try:
        
                    if Grid[x+1][y] == '0':

                        if (x + 1) > -1 and y > -1:

                            i = i + 1
                            continues = True
                            NextTile.append([x+1, y])

                except:
                    pass

                try:

                    if Grid[x-1][y] == '0':

                        if (x - 1) > -1 and y > -1:

                            continues = True
                            i = i + 1
                            NextTile.append([x-1, y])
                except:
                    pass
                    

                try:

                    if Grid[x][y+1] == '0':

                        if x > -1 and (y + 1) > -1:

                            continues = True
                            i = i + 1
                            NextTile.append([x, y+1])

                except:
                    pass

                try:

                    if Grid[x][y-1] == '0':

                        if x > -1 and (y - 1) > -1:

                            i = i + 1
                            continues = True
                            NextTile.append([x, y-1])
                except:
                    pass


                if n == 10000: # Changes for each map size

                    # Add +1 to all values xs and ys individual to show possible number pos

                    result = []

                    for x in NextTile:

                        if x not in result:

                            result.append(x)

                    NextTile.clear()
                    NextTile = result

                    print('Updated( no Dupes): ',NextTile)



                    for i in range(len(NextTile)):

                        x = NextTile[i][0]
                        y = NextTile[i][1]



                        
                        NextTile.append([x, y+1])
                        NextTile.append([x+1, y])
                        NextTile.append([x-1, y])
                        NextTile.append([x, y-1])



                    print('After(+/-1) ',NextTile)
                    
                    # REMOVE ALL NEGATIVES FROM LIST

                    copy = []

                    for i in range(len(NextTile)):

                        if NextTile[i][0] > -1 and NextTile[i][1] > -1:

                            copy.append([NextTile[i][0], NextTile[i][1]])

                    print('Updated No Negatives: ',copy)

                    NextTile.clear()

                    NextTile = copy

                    # REMOVE ALL DUPES

                    result = []

                    for x in NextTile:

                        if x not in result:

                            result.append(x)

                    NextTile.clear()
                    NextTile = result

                    print('Updated( no Dupes): ',NextTile)


                    # Remove all Joint Tiles from Board by updating Filled Tile Map


                    for i in range(len(NextTile)):

                        x = NextTile[i][0]
                        y = NextTile[i][1]

                    
                        FilledTiles[y][x] = '0'


                    return FilledTiles


                else:

                    # Remove Duplicates

                                   
                    
                    n = n + 1

                # Repeat for each value of NextTiles, Continue until it doesnt change


    def DisplayTiles(self, FilledTiles, Grid):

        for i in range(0, BoardSize[0]):

            for j in range(0, BoardSize[1]):

                try:

                    if FilledTiles[i][j] == '1':

                        gameScreen.blit(TileImg, ((24 * i)+5, (24 * j)+5))

                except:

                    pass


                    # FIND ALL CONNECTING EMPTY ONEs

            
    def DisplayAll(self):

        for i in range(0, BoardSize[0]):

            for j in range(0, BoardSize[1]):

                if game.Grid[j][i] == 'X':

                    gameScreen.blit(BombImg, ((24 * i)+5, (24 * j)+5))

                elif game.Grid[j][i] == '0':

                    gameScreen.blit(EmptyImg, ((24 * i)+5, (24 * j)+5))

                elif game.Grid[j][i] == '1':

                    gameScreen.blit(OneImg, ((24 * i)+5, (24 * j)+5))

                elif game.Grid[j][i] == '2':

                    gameScreen.blit(TwoImg, ((24 * i)+5, (24 * j)+5))

                elif game.Grid[j][i] == '3':

                    gameScreen.blit(ThreeImg, ((24 * i)+5,  (24 * j)+5))

                elif game.Grid[j][i] == '4':

                    gameScreen.blit(FourImg, ((24 * i)+5, (24 * j)+5))

                elif game.Grid[j][i] == '5':

                    gameScreen.blit(FiveImg, ((24 * i)+5, (24 * j)+5))

    def CheckCollisions(self, TilePositions, Tiles):

        Mouse_Pos = pygame.mouse.get_pos()


        # Rule for Tilles is 24n + 5

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

                    return TilePositionXY

        else:

            TilePositionXY = [-1, -1]

            return TilePositionXY


TileImg = pygame.image.load(os.path.join('Assets', 'Tile.png'))
TileImg = pygame.transform.scale(TileImg, (TileX, TileY))

Tiles = list()

TotalTiles = BoardSize[0]*BoardSize[1]

for i in range(BoardSize[0]):

    for j in range(BoardSize[1]):

        name = [i, j]

        Tiles.append(Tile((24*i)+5, (24*j)+5, TileImg, 1, False, name, TotalTiles))


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
clickedTiles = [-1, -1]



for i in range(BoardSize[0]):

    OneList = []

    for j in range(BoardSize[1]):

        

        OneList.append('1')

    FilledTiles.append(OneList)


Panel.DisplayTiles(FilledTiles, Grid)

time.sleep(0.2)

FirstRun = 0

while run:

    #print('Tile Pattern : ',FilledTiles)

    if FirstRun > 0:

        
        TilePositionXY = Panel.CheckCollisions(TilePositions, Tiles)
        ClickedBox = TilePositionXY

        if -1 in ClickedBox:

            pass
        else:
            x = ClickedBox[0]
            y = ClickedBox[1]
            try:
                FilledTiles[x][y] = '0'
                FilledTiles = Panel.RemoveNearTiles(ClickedBox, FilledTiles, Grid)
            except:
                pass

        
        # Only changes Filled Tiles
        Panel.DisplayAll()
        Panel.DisplayTiles(FilledTiles, Grid)

    FirstRun += 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    pygame.display.update()
    clock.tick(30)
