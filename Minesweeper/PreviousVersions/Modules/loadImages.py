import pygame, os
TileX = 24
TileY = 24

os.chdir('/Users/sovie/Documents/BombMoppa')

def load():
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

    return SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg

def Transform(SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg):

    DotImg = pygame.transform.scale(DotImg, (10, 10))
    CrossImg = pygame.transform.scale(CrossImg, (10, 10))
    InputImg = pygame.transform.scale(InputImg, (40, 22))
    InputNameImg = pygame.transform.scale(InputNameImg, (150, 25))
    SelectedNameImg = pygame.transform.scale(SelectedNameImg, (150, 25))
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
    TileImg = pygame.transform.scale(TileImg, (TileX, TileY))
    FlagImg = pygame.transform.scale(FlagImg, (TileX, TileY))
    RestartImg = pygame.transform.scale(RestartImg, (TileX, TileY))

    WinImg = pygame.transform.scale(WinImg, (60, 80))
    LooseImg = pygame.transform.scale(LooseImg, (100, 80))


    return SelectBoxImg, SelectBoxImg2, InputImg, InputNameImg, SelectedNameImg, PlayButtonImg, QuitButtonImg, DotImg, CrossImg, EmptyImg, OneImg, TwoImg, ThreeImg, FourImg, FiveImg, SixImg, SevenImg, EightImg, BombImg, BombMenuImg, TileImg, FlagImg, RestartImg, WinImg, LooseImg

load()
