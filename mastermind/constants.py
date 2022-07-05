import pygame


# Dimensions for Board components 
WIDTH = 600
HEIGHT = 1000
SQUARE_SIZE = 50

# Display settings
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
DGRAY = (43, 52, 55)
FPS = 30
DELAY_TIME = 5000

# Assets
menu = pygame.image.load('assets/menu.png')
win = pygame.image.load('assets/win_prompt.png')
lose = pygame.image.load('assets/lose_prompt.png')
background = pygame.image.load('assets/background.png')
gamesettings = pygame.image.load('assets/gamesettings.png')
buttonback = pygame.image.load('assets/buttonback.png')
buttonmusicon = pygame.image.load('assets/buttonmusicon.png')
buttonredo = pygame.image.load('assets/buttonredo.png')
piecered = pygame.image.load('assets/piecered.png')
pieceorange = pygame.image.load('assets/pieceorange.png')
pieceyellow = pygame.image.load('assets/pieceyellow.png')
piecegreen = pygame.image.load('assets/piecegreen.png')
pieceblue = pygame.image.load('assets/pieceblue.png')
piecenavy = pygame.image.load('assets/piecenavy.png')
piecepurple = pygame.image.load('assets/piecepurple.png')
piecepink = pygame.image.load('assets/piecepink.png')
piecewhite = pygame.image.load('assets/piecewhite.png') 
piecesecret = pygame.image.load('assets/piecesecret.png')
cluegray = pygame.image.load('assets/cluegray.png')
clueblue = pygame.image.load('assets/clueblue.png')
cluepink = pygame.image.load('assets/cluepink.png')
submitwaiting = pygame.image.load('assets/submitwaiting.png') 
submitready = pygame.image.load('assets/submitready.png') 
submitconfirm = pygame.image.load('assets/submitconfirm.png') 
answerleft = pygame.image.load('assets/answerleft.png')
answerright = pygame.image.load('assets/answerright.png')

# Collections of assets
easy_piece_collection = [piecered, pieceyellow, pieceblue, piecepurple] 
normal_piece_collection = [pieceorange, piecegreen]
hard_piece_collection = [piecenavy, piecepink]
button_collection = [buttonback, buttonmusicon, buttonredo]
