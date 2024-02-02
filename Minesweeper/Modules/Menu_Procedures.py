import pygame, time, sys

#from Data_Base import CheckAvailability, AddPlayer, SelectFromPlayer, SelectFromGames

def setUpMenu():
    # Sets up the Menu
    MenuTick = 0 # Restarts the Menu Ticks
    MenuScreenSize = (450, 250) # Sets the Size
    MenuScreen = pygame.display.set_mode(MenuScreenSize) # Creates Screen
    pygame.display.set_caption('Menu') # Gives the Screen a Caption
    return MenuScreen # Returns the Screen

def CreateNewLogIn(Images, Button):
    CreateAccountMenu = pygame.display.set_mode((300, 200))
    CreateAccountLoop = True
    UsernameButton = Button(120, 10, Images['InputNameImg'], 1)
    PasswordButton = Button(120, 60, Images['InputNameImg'], 1)
    Password2Button = Button(120, 110, Images['InputNameImg'], 1)
    CreateAccount2Button = Button(205, 150, Images['CreateAccountImg'], 0.1)
    LogInButtons = [UsernameButton, PasswordButton, Password2Button, CreateAccount2Button]
    pygame.font.init()
    Font = pygame.font.Font('freesansbold.ttf', 15)
    UserNameText = Font.render('Username: ', True, (0, 0, 0))
    PasswordeText = Font.render('Password: ', True, (0, 0, 0))
    ReEnterPasswordText = Font.render('ReEnter Pass: ', True, (0, 0, 0))
    Username = ''
    Password = ''
    Password2 = ''
    while CreateAccountLoop:
        CreateAccountMenu.fill((255, 255, 255))
        CreateAccountMenu.blit(UserNameText, (20, 15))
        CreateAccountMenu.blit(PasswordeText, (20, 65))
        CreateAccountMenu.blit(ReEnterPasswordText, (20, 115))
        UsernameDisplay = Font.render(Username, True, (0, 0, 0))
        PasswordHidden = ''
        Password2Hidden = ''
        for i in range (len(Password)):
            PasswordHidden = PasswordHidden + '*'
        for i in range (len(Password2)):
            Password2Hidden = Password2Hidden + '*'
        PasswordDisplay = Font.render(PasswordHidden, True, (0, 0, 0))
        Password2Display = Font.render(Password2Hidden, True, (0, 0, 0))
        Texts = [UsernameDisplay, PasswordDisplay, Password2Display]
        for i in range(len(LogInButtons)):
            LogInButtons[i]._Draw(CreateAccountMenu)
        if UsernameButton._checkForClick():
            Username = FetchInputText('Both', 15, [120, 10], 'NewUsername', Texts, CreateAccountMenu, Images, '', LogInButtons)
            Available = CheckAvailability(Username)
            if Available == True:
                print('free')
            else:
                print('taken')
                time.sleep(0.1)
                CreateAccountMenu.fill((255, 0, 0))
                pygame.display.update()
                time.sleep(0.3)
                Username = ''
        if PasswordButton._checkForClick():
            Password = FetchInputText('Both', 15, [120, 60], 'NewPassword', Texts, CreateAccountMenu, Images, '', LogInButtons)
        if Password2Button._checkForClick():
            Password2 = FetchInputText('Both', 15, [120, 110], 'NewPassword2', Texts, CreateAccountMenu, Images, '', LogInButtons)
        if CreateAccount2Button._checkForClick():
            if len(Username) > 1 and len(Password) > 3:
                if Password == Password2:
                    AddPlayer(Username, Password)
                    time.sleep(0.1)
                    CreateAccountMenu.fill((0, 255, 0))
                    pygame.display.update()
                    time.sleep(0.3)
                    CreateAccountLoop = False
                    print('Account Created')
                    
                else:
                    print('Passwords do not match')
                    time.sleep(0.1)
                    CreateAccountMenu.fill((255, 0, 0))
                    pygame.display.update()
                    time.sleep(0.3)
                    Password = ''
                    Password2 = ''
            else:
                print('Username/password too short')
                time.sleep(0.1)
                CreateAccountMenu.fill((255, 0, 0))
                pygame.display.update()
                time.sleep(0.3)
                Password = ''
                Password2 = ''
        else:
            CreateAccountMenu.blit(UsernameDisplay, (125, 15))
            CreateAccountMenu.blit(PasswordDisplay, (125, 65))
            CreateAccountMenu.blit(Password2Display, (125, 115))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    CreateAccountLoop = False

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

                    elif InputType == 'Both':
                        if event.unicode.isalpha():
                            Text = Text + event.unicode
                        elif event.unicode.isdigit():
                            Text = Text + event.unicode
                    else:
                        if event.unicode.isdigit():
                            Text = Text + event.unicode
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Displays rest of import information on screen while in Loop
            if whichInput != 'NewUsername' and whichInput != 'NewPassword' and whichInput != 'NewPassword2':
                Buttons[9]._Draw(Screen)
                Buttons[10]._Draw(Screen)
                Buttons[11]._Draw(Screen)
                
                if whichInput == 'Name':
                    Screen.blit(Images['SelectedNameImg'], (20, 10))
                elif whichInput == 'Password':
                    Screen.blit(Images['SelectedNameImg2'], (20, 10))
                else:
                    Screen.blit(Images['InputNameImg'], (20, 10))
            else:
                Buttons[0]._Draw(Screen)
                Buttons[1]._Draw(Screen)
                Buttons[2]._Draw(Screen)
                Screen.blit(Images['SelectedNameImg'], (POS[0], POS[1]))
                    
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
            if whichInput == 'Password':
                Screen.blit(Texts[0], (150, 200))
                Screen.blit(Texts[1], (10, 180))
                Screen.blit(Texts[2], (10, 200))
            if whichInput == 'NewUsername':
                Screen.blit(Texts[1], (125, 65))
                Screen.blit(Texts[2], (125, 115))
            if whichInput == 'NewPassword':
                Screen.blit(Texts[0], (125, 15))
                Screen.blit(Texts[2], (125, 115))
            if whichInput == 'NewPassword2':
                Screen.blit(Texts[0], (125, 15))
                Screen.blit(Texts[1], (125, 65))
            # Constanlty Updates the Text to the screen so you can see what you are typing
            pygame.font.init()
            Font = pygame.font.Font('freesansbold.ttf', 15)
            if whichInput == 'Password' or whichInput == 'NewPassword2' or whichInput == 'NewPassword':
                Text2 = ''
                for i in range(len(Text)):
                    Text2 = Text2 + '*'
                TextDisplay = Font.render(Text2, True, (0, 0, 0))
            else:
                TextDisplay = Font.render(Text, True, (0, 0, 0))

            if whichInput == 'NewUsername' or whichInput == 'NewPassword' or whichInput == 'NewPassword2':
                Screen.blit(TextDisplay, (POS[0]+5, POS[1]+5))
            else:
                Screen.blit(TextDisplay, (POS[0], POS[1]))
            pygame.display.update() # Updates Display as is out of main Loop           
    return Text # Returns the User input

def CreateButtons(Images, Button):
    # Creates Buttons for the Main Menu, Only has to be run once
    CreateAccountButton = Button(200, 12, Images['CreateAccountImg'], 0.1)
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
    # Buttons for leaderboard
    ShowBeginnerButton = Button(20, 10, Images['LeaderboardBackgroundButton'], 0.06)
    ShowIntermediateButton = Button(100, 10, Images['LeaderboardBackgroundButton'], 0.06)
    ShowExpertButton = Button(180, 10, Images['LeaderboardBackgroundButton'], 0.06)
    ShowBeginnerButton2 = Button(160, 10, Images['LeaderboardBackgroundButton'], 0.06)
    ShowIntermediateButton2 = Button(240, 10, Images['LeaderboardBackgroundButton'], 0.06)
    ShowExpertButton2 = Button(320, 10, Images['LeaderboardBackgroundButton'], 0.06)
    OrderByTimeButton = Button(280, 10, Images['LeaderboardBackgroundButton'], 0.06)
    OrderByDateButton = Button(360, 10, Images['LeaderboardBackgroundButton'], 0.06)
    Buttons = [BeginnerButton, IntermediateButton, ExpertButton, CustomButton, TileLockOnButton, SaveScoreButton, EasyResetButton, PlayButton, QuitButton, HeightInputButton, WidthInputButton, MineInputButton, InputNameButton, BoardButton, CreateAccountButton] 
    LeaderBoardButtons = [ShowBeginnerButton, ShowIntermediateButton, ShowExpertButton, OrderByTimeButton, OrderByDateButton]
    AccountStatisticButtons = [ShowBeginnerButton2, ShowIntermediateButton2, ShowExpertButton2]
    return Buttons, LeaderBoardButtons, AccountStatisticButtons

def LeaderBoard(Settings, Data, Screen):
    # Organises and Displays the top 50 leaderboard results for each Difficulty
    pygame.font.init()
    Font = pygame.font.Font('freesansbold.ttf', 10)
    if len(Data) > 50:
        TopScores = 50 # Makes sure only 50 can be displayed but allows it to function if there arent more than 50 results
    else:
        TopScores = len(Data)
    j = 0
    i = 0
    count = 1
    while count < TopScores+1: # Loops through each results displaying it
        if j > 24 and i == 0: # When it reaches the bottom
            i = i + 1 # Makes it go to the next line
            j = 0 # AND Makes it go back to the top 
        # Organises the Text
        Text = str(Data[j])
        Text = Text.rstrip(")")
        Text = Text.replace("datetime.datetime(", " | ")
        Text = Text.replace("Decimal(", " ")
        Text = Text.replace("('", "")
        Text = Text.replace("'", "")
        Text = Text.replace(",", "")
        Text = Text.replace(")", "  ")
        Top = False
        if Settings[1] == 'Time': # If its in the Time order, the top 3 times get colourful titles
            if count == 1:
                Text = Font.render((str(count) +' '+ Text), True, (201, 176, 55)) # renders GOLD
                Top = True
            if count == 2:
                Text = Font.render((str(count) +' '+ Text), True, (215, 215, 215)) # renders SILVER
                Top = True
            if count == 3:
                Text = Font.render((str(count) +' '+ Text), True, (106, 56, 5)) # renders BRONZE
                Top = True
            if count > 3:
                Text = Font.render((str(count) +' '+ Text), True, (0, 0, 0)) # renders plain black
        else:
            Text = Font.render((str(count) +' '+ Text), True, (0, 0, 0)) # renders plain black
        Screen.blit(Text, ((i*200) + 20, (j * 17)+60))
        j = j + 1
        count = count + 1
    
def AccountStatstics(PlayerID, Difficulty):
    PlayerDateCreated = SelectFromPlayer(PlayerID)
    PlayerGamesWon, PlayerGamesLost, PlayerGamesPlayed, GameHistory, TotalGamesPlayed, TotalGamesWon = SelectFromGames(PlayerID, Difficulty)
    PlayerStats = [PlayerGamesWon, PlayerGamesLost, PlayerGamesPlayed, PlayerDateCreated, GameHistory]
    GlobalStats = [TotalGamesPlayed, TotalGamesWon]
    return GlobalStats, PlayerStats


