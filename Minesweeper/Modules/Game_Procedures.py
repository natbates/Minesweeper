
# Procedure Module
import pygame, time, sys
 
def DisplayAll(Game, Screen, Images, TileX, TileY):
    Grid = Game._Grid
    # When game is over AND during each iteration of maingame loop, shows everything under the tiles
    Tiles = [Images['EmptyImg'], Images['OneImg'], Images['TwoImg'], Images['ThreeImg'], Images['FourImg'], Images['FiveImg'], Images['SixImg'], Images['SevenImg'], Images['EightImg']] # list of images from dictionary
    for i in range(0, Game._boardSize[0]):
        for j in range(0, Game._boardSize[1]): # Loops through each value of 2Darray Grid 
            if Grid[j][i] == 'X': # Checks if its a Bomb
                Screen.blit(Images['BombImg'], ((TileX * i)+5, (TileY * j) + 10)) # If its a bomb it displays Bomb
            for x in range(9): # Loops through every possible number 1-8, if its equal to x ( 1-8 ) then it displays Xs position value of Images ( 1-8 )
                if Grid[j][i] == str(x):
                    Screen.blit(Tiles[x], ((TileX*i)+5, (TileY*j) + 10)) # Displays Number Image
 
def RemoveTiles(AllTiles, FlagLock, Hud, Game, clicks, Button):
    for i in range(len(AllTiles)):
        if AllTiles[i]._checkForClick() == True: # Checks What Remaining On Tiles Collides with Mouse Position using Button Method checkForClick  
            time.sleep(0.04) # Delay to stop user getting rid of every tile on accident
            if FlagLock == True: # If flag lock is on, the flag status must be FALSE in order for the user to click the Tile
                if AllTiles[i]._FlagOn == False:
                    if AllTiles[i]._TileOn == True:             
                        clicks = clicks + 1
                        AllTiles[i]._TileOn = False
                        X = AllTiles[i]._TileNumber[0]
                        Y = AllTiles[i]._TileNumber[1]
                        TileNum = [X, Y]
                        if Game._Grid[Y][X] == 'X': # If the tile removed has a Mine underneath it it returns False which tells the program you have lost the game
                            return False, TileNum, clicks, False
                        if clicks == 1: # If its the first initial click, Used for making sure the first click cannot be a Mine
                            return True, TileNum, clicks, True
                        else:
                            return True, TileNum, clicks, False
            elif FlagLock == False: # Repeat of code but for if flag lock is off, meaning it doesnt have to check if the flag is on or off              
                if AllTiles[i]._TileOn == True:
                    clicks = clicks + 1
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
    MousePosition = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[2] == 1: # If right mouse button is pressed
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
