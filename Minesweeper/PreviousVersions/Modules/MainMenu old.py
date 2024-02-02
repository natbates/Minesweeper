import pygame, time

from Procedures import BubbleSort

def setUpMenu():
    # Sets up the Menu
    MenuTick = 0 # Restarts the Menu Ticks
    MenuScreenSize = (450, 250) # Sets the Size
    MenuScreen = pygame.display.set_mode(MenuScreenSize) # Creates Screen
    pygame.display.set_caption('Menu') # Gives the Screen a Caption
    return MenuScreen # Returns the Screen


def FetchInputText(InputType, MaxSize, POS, whichInput, Texts, Screen, Images, NameDisplay, Buttons):
    # Gets the users text input
    Done = False
    Text = '' # Empty Starting string
    while Done == False and len(Text) < MaxSize: # Limits the characters the user can enter
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: # 
                    if len(Text) > 0: # Makes sure there is text to get rid of
                        Text = Text.rstrip(Text[-1]) # Removes the last character of the string
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    Done = True # Finsihes Loop
                if event.key == pygame.K_SPACE and InputType == 'Alpha': # for the name, allows you to enter a space
                    Text = Text + ' '
                else:
                    if InputType == 'Alpha':
                        if event.unicode.isalpha(): # Returns True if they key pressed is an alphabetic character
                            Text = Text + event.unicode
                    else:
                        if event.unicode.isdigit():
                            Text = Text + event.unicode
            # Displays rest of import information on screen while in Loop
            Buttons[9]._Draw(Screen)
            Buttons[10]._Draw(Screen)
            Buttons[11]._Draw(Screen)    
            if whichInput == 'Name':
                Screen.blit(Images['SelectedNameImg'], (20, 10))
            else:
                Screen.blit(Images['InputNameImg'], (20, 10))
            if whichInput == 'Name':
                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[1], (10, 180))
                Screen.blit(Texts[2], (10, 200))
            if whichInput == 'Mines':
                Screen.blit(Texts[1], (10, 180))
                Screen.blit(Texts[2], (10, 200))
                Screen.blit(NameDisplay, (25, 15))
            if whichInput == 'Width':
                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[2], (10, 200))
                Screen.blit(NameDisplay, (25, 15))
            if whichInput == 'Height':
                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[1], (10, 180))
                Screen.blit(NameDisplay, (25, 15))
            # Constanlty Updates the Text to the screen so you can see what you are typing
            pygame.font.init()
            Font = pygame.font.Font('freesansbold.ttf', 15)
            TextDisplay = Font.render(Text, True, (0, 0, 0))
            Screen.blit(TextDisplay, (POS[0], POS[1]))            
            pygame.display.update() # Updates Display as is out of main Loop           
    return Text # Returns the User input

def CreateButtons(Images, Button):
    # Creates Buttons for the Main Menu, Only has to be run once
    BeginnerButton = Button(20, 50, Images['SelectBoxImg'], 0.08)
    IntermediateButton = Button(20, 70, Images['SelectBoxImg'], 0.08)
    ExpertButton = Button(20, 90, Images['SelectBoxImg'], 0.08)
    CustomButton = Button(20, 110, Images['SelectBoxImg'], 0.08)
    TileLockOnButton = Button(150, 50, Images['SelectBoxImg2'], 0.08)
    SaveScoreButton = Button(150, 90, Images['SelectBoxImg2'], 0.08)
    EasyResetButton = Button(150, 70, Images['SelectBoxImg2'], 0.08)
    PlayButton = Button(300, 60, Images['PlayButtonImg'], 1)
    QuitButton = Button(300, 160, Images['QuitButtonImg'], 1)
    BoardButton = Button(300, 110, Images['LeaderBoardImg'], 1)
    HeightInputButton = Button(70, 198, Images['InputImg'], 1)
    WidthInputButton = Button(70, 175, Images['InputImg'], 1)
    MineInputButton = Button(205, 195, Images['InputImg'], 1)
    InputNameButton = Button(20, 10, Images['InputNameImg'], 1)
    
    Buttons = [BeginnerButton, IntermediateButton, ExpertButton, CustomButton, TileLockOnButton, SaveScoreButton, EasyResetButton, PlayButton, QuitButton, HeightInputButton, WidthInputButton, MineInputButton, InputNameButton, BoardButton] 
    return Buttons


def LeaderBoard(whichDifficulty):
    # Fetches the top n results from
    File = open('MineSweeperScores.txt', 'r')

    data = File.readlines() # Reads every line in the text file

    ListOfScores = []
    # Sort Through Data and Finds the 25 Highest Times for each Difficulty
    for i in range(len(data)): # loops through every line
        if whichDifficulty in data[i]:
            j = 0
            Text = ''
            while data[i][j] != '/': # loops through all the characters until it finds a / which will resemble the end of the Players name and Time
                Text = Text + str(data[i][j])
                j = j + 1
            Text = Text + ' '
            ListOfScores.append(Text) # Adds the Name and Time to the List of Scores
    Times = []
    Names = []
    for i in range(len(ListOfScores)):# Seperates the score into Names and Times
        j = 0
        TempTime = ''
        TempName = ''
        while ListOfScores[i][j].isnumeric():
            TempTime = TempTime + str(ListOfScores[i][j])
            j = j + 1
        while ListOfScores[i][j].isalpha():
            TempName = TempName + str(ListOfScores[i][j])
            j = j + 1
        Times.append(TempTime) # All Scores
        Names.append(TempName) # All Names

    OriginalListOfTimes = Times.copy() # Deep Copy so they dont share the change

    # Bubble Sort Algorithm
    Times = BubbleSort(Times) # Sorts the Numbers from Lowest to highest
    TopResults = []
    # Get Top 25 Scores
    if len(Times) > 0: # Makes sure there is actually data in the file
        n = len(Times)
        if n > 25: # if there are more than 25 sets of data, only go for 25 times. This will mean that if there are less than 25 it doesnt create an error (error: for i in range(25) when not 25 lines of data)
            n = 25
        for i in range(n): 
            TopResults.append(Times[i] + ' '+Names[OriginalListOfTimes.index(Times[i])]) # Because Times have been Bubble sorted from lowest to highest, we shall use the index and copy to find the original name which the time corelates too, if two people got the same score it wont matter as it will return either name
            
    return TopResults
