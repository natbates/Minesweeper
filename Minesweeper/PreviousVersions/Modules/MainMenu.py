import pygame.font
pygame.font.init()
Font2 = pygame.font.Font('freesansbold.ttf', 15)

def DisplayText(InputImg, Screen, Mines, BoardWidth, BoardHeight):

        Screen.blit(InputImg, (70, 198))
        Screen.blit(InputImg, (70, 175))
        Screen.blit(InputImg, (205, 195))


        Font2 = pygame.font.Font('freesansbold.ttf', 15)

        Text1 = Font2.render('Mines:     '+str(Mines), True, (0, 0, 0))
        Text2 = Font2.render('Width:     '+str(BoardWidth), True, (0, 0, 0))
        Text3 = Font2.render('Height:    '+str(BoardHeight), True, (0, 0, 0))

        Text4 = Font2.render('Beginner', True, (0, 0, 0))
        Text5 = Font2.render('Intermediate', True, (0, 0, 0))
        Text6 = Font2.render('Expert', True, (0, 0, 0))
        Text7 = Font2.render('Custom', True, (0, 0, 0))

        Text8 = Font2.render('Tile LOCK', True, (0, 0, 0))
        Text9 = Font2.render('StartTile', True, (0, 0, 0))
        Text10 = Font2.render('Save Score', True, (0, 0, 0))


        Screen.blit(Text1, (150, 200))
        Screen.blit(Text2, (10, 180))
        Screen.blit(Text3, (10, 200))

        Screen.blit(Text4, (40, 50))
        Screen.blit(Text5, (40, 70))
        Screen.blit(Text6, (40, 90))
        Screen.blit(Text7, (40, 110))

        Screen.blit(Text8, (180, 50))
        Screen.blit(Text9, (180, 70))
        Screen.blit(Text10, (180, 90))

        return Text1, Text2, Text3, Text4


def DisplayButtonDots(Screen, DotImg, CrossImg, Beginner, Intermediate, Expert, Custom, SaveScoreButtonOn, TileLockOnButtonOn, StartTileButtonOn):

    if Beginner == True:

        Screen.blit(DotImg, (20, 50))

    if Intermediate == True:

        Screen.blit(DotImg, (20, 70))

    if Expert ==  True:

        Screen.blit(DotImg, (20, 90))

    if Custom == True:

        Screen.blit(DotImg, (20, 110))
        
    if SaveScoreButtonOn == True:

        Screen.blit(CrossImg, (150, 90))

    if TileLockOnButtonOn == True:

        Screen.blit(CrossImg, (150, 50))

    if StartTileButtonOn == True:

        Screen.blit(CrossImg, (150, 70))


def CustomFetchText(InputPlace, Mines, BoardWidth, BoardHeight, FetchInputText, Texts, Screen):

    Done = False

    if len(InputPlace) > 0:

        if InputPlace == 'Mines':

            Mines = FetchInputText('Digits', 3, [210, 200], InputPlace, Texts, Screen) 
            if len(Mines) == 0:
                Mines = 1


        if InputPlace == 'Width':

            BoardWidth = int(FetchInputText('Digits', 2, [80, 179], InputPlace, Texts, Screen))

            if len(str(BoardWidth)) == 0:

                BoardWidth = 0
            
            if BoardWidth < 8 or BoardWidth > 25:

                BoardWidth = 0

            
        if InputPlace == 'Height':

            BoardHeight = int(FetchInputText('Digits', 2, [80, 203], InputPlace, Texts, Screen)) 

            if len(str(BoardHeight)) == 0:

                BoardHeight = 0
            
            if BoardHeight < 8 or BoardHeight > 25:

                BoardHeight = 0


    return Mines, BoardWidth, BoardHeight

