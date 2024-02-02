# This Module Loads Images
import pygame, os, glob

os.chdir('/Users/nathanielbates/Documents/Coding Projects/Minesweeper')
print(os.getcwd())


print('cferfefeferfergjhekrfherkhnherf')

def Load():
    # Loads Images from Asset Folder
    SelectBoxImg = pygame.image.load(os.path.join('Assets/Menu', 'SelectBox.png'))
    SelectBoxImg2 = pygame.image.load(os.path.join('Assets/Menu', 'SelectBox2.png'))
    InputImg = pygame.image.load(os.path.join('Assets/Menu', 'InputSquare.png'))
    InputNameImg =pygame.image.load(os.path.join('Assets/Menu', 'InputName.png'))
    SelectedNameImg =pygame.image.load(os.path.join('Assets/Menu', 'Selected.png'))
    SelectedNameImg2 =pygame.image.load(os.path.join('Assets/Menu', 'Selected2.png'))
    PlayButtonImg = pygame.image.load(os.path.join('Assets/Menu', 'PlayButton.png'))
    QuitButtonImg = pygame.image.load(os.path.join('Assets/Menu', 'QuitButton.png'))
    LeaderBoardImg = pygame.image.load(os.path.join('Assets/Menu', 'LeaderBoardButton.png'))
    PlayButtonPressedImg = pygame.image.load(os.path.join('Assets/Menu', 'PlayButtonPressed.png'))
    QuitButtonPressedImg = pygame.image.load(os.path.join('Assets/Menu', 'QuitButtonPressed.png'))
    LeaderBoardPressedImg = pygame.image.load(os.path.join('Assets/Menu', 'LeaderBoardButtonPressed.png'))
    CreateAccountImg = pygame.image.load(os.path.join('Assets/Menu', 'CreateAccount.png'))
    AccountStatsImg = pygame.image.load(os.path.join('Assets/Menu', 'AccountStatsImg.png'))
    GameHistroyImg = pygame.image.load(os.path.join('Assets/Menu', 'GameHistory.png'))
    DotImg = pygame.image.load(os.path.join('Assets/Menu', 'Dot.png'))
    CrossImg = pygame.image.load(os.path.join('Assets/Menu', 'Cross.png'))
    LeaderboardBackgroundButton = pygame.image.load(os.path.join('Assets/Menu', 'LeaderboardBackgroundButton.png'))
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
    HUDImg = pygame.image.load(os.path.join('Assets/GameBoard', 'HUD.png'))
    Images = [SelectBoxImg, SelectBoxImg2, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, InputImg, InputNameImg, SelectedNameImg,  EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg, LeaderBoardImg, PlayButtonPressedImg, QuitButtonPressedImg, LeaderBoardPressedImg, LeaderboardBackgroundButton, SelectedNameImg2, CreateAccountImg, AccountStatsImg, GameHistroyImg]
    return Images # Returns as a List

def Transform(Images, TileX, TileY):
    # Transforms Images to correct Dimensions
    Images[4] = pygame.transform.scale(Images[4], (10, 10))
    Images[5] = pygame.transform.scale(Images[5], (10, 10))
    Images[6] = pygame.transform.scale(Images[6], (40, 22))
    Images[7] = pygame.transform.scale(Images[7], (150, 25))
    Images[8] = pygame.transform.scale(Images[8], (150, 25))
    Images[30] = pygame.transform.scale(Images[30], (150, 25))
    for i in range(9, 22):
        Images[i] = pygame.transform.scale(Images[i], (TileX, TileY)) 
    Images[23] = pygame.transform.scale(Images[23], (60, 50))
    Images[24] = pygame.transform.scale(Images[24], (60, 50))
    
    NewImages = {'SelectBoxImg':Images[0], 'SelectBoxImg2':Images[1], 'PlayButtonImg':Images[2], 'QuitButtonImg':Images[3], 'DotImg': Images[4], 'CrossImg': Images[5], 'InputImg':Images[6], 'InputNameImg':Images[7], 'SelectedNameImg':Images[8], 'EmptyImg':Images[9],'OneImg': Images[10], 'TwoImg':Images[11], 'ThreeImg':Images[12], 'FourImg':Images[13], 'FiveImg':Images[14], 'SixImg':Images[15], 'SevenImg':Images[16], 'EightImg':Images[17], 'BombImg':Images[18], 'BombMenuImg':Images[19], 'TileImg':Images[20], 'FlagImg':Images[21], 'RestartImg':Images[22], 'WinImg':Images[23], 'LooseImg':Images[24], 'LeaderBoardImg':Images[25], 'PlayButtonPressedImg': Images[26], 'QuitButtonPressedImg': Images[27], 'LeaderBoardPressedImg': Images[28], 'LeaderboardBackgroundButton': Images[29], 'SelectedNameImg2': Images[30], 'CreateAccountImg': Images[31], 'AccountStatsImg': Images[32], 'GameHistroyImg': Images[33]}
    return NewImages # Returns as a Dictionary

def loadHUDImage(ScreenWidth, ScreenHeight, Difficulty):
    # Loads images for the game display 
    HUDImg = pygame.image.load(os.path.join('Assets/GameBoard', 'HUD.png'))
    BackGroundImg = pygame.image.load(os.path.join('Assets/GameBoard', 'BackgroundImage.png'))
    if Difficulty == 'Beginner':
        HudImg = pygame.transform.scale(HUDImg, (100, ScreenHeight-18))
    else:
        HudImg = pygame.transform.scale(HUDImg, (ScreenWidth/4, ScreenHeight-18))
    BackGroundImg = pygame.transform.scale(BackGroundImg, (70, 25))
    return HudImg, BackGroundImg

