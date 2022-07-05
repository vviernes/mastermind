import pygame
from mastermind.constants import *


class Board():
    def __init__(self, difficulty, max_attempts):
        self.pieces = []
        self.difficulty = difficulty
        self.max_attempts = max_attempts

        self.set_pieces()

    def draw_board(self, window):
        WINDOW.blit(background, (0, 0))

        for i in range(len(button_collection)):                                                     # draw game option buttons
            self.draw_item(window, button_collection[i], 50 + 225*i, 200)
        
        for i in range(len(easy_piece_collection)):                                                 # draw pieces of Easy difficulty
            self.draw_item(window, easy_piece_collection[i], 200 + SQUARE_SIZE*i, 925)
        
        difficulty = self.get_difficulty()                                  
        if difficulty != 'Easy':                                                                    # draw pieces of Normal/Hard difficulty
            for i in range(len(normal_piece_collection)):
                self.draw_item(window, normal_piece_collection[i], 150 + SQUARE_SIZE*5*i, 925)
            if difficulty == 'Hard':
                for i in range(len(normal_piece_collection)):
                    self.draw_item(window, hard_piece_collection[i], 100 + SQUARE_SIZE*7*i, 925)

        for i in range(4):                                                                          # draw secret code 
            self.draw_item(window, piecesecret, 175 + SQUARE_SIZE*i, 300)

        max_attempts = self.get_max_attempts()
        for i in range(max_attempts):                                                               # draw submit code section
            self.draw_item(window, submitwaiting, 100, 800 - SQUARE_SIZE*i)

        for row in range(max_attempts):                                                             # draw guess section
            for col in range(4):
                self.draw_item(window, piecewhite, 175  + SQUARE_SIZE*col, 800 - SQUARE_SIZE*row)
        
        for row in range(max_attempts):                                                             # draw clue section
            for col in range(4):
                self.draw_item(window, cluegray, 400  + SQUARE_SIZE/2*col, 800 - SQUARE_SIZE*row)

    def draw_item(self, window, asset, x_pos, y_pos):
        window.blit(asset, (x_pos, y_pos))

    def get_pieces(self):
        return self.pieces

    def get_difficulty(self):
        return self.difficulty
    
    def get_max_attempts(self):
        return self.max_attempts
    
    def set_pieces(self):
        difficulty = self.get_difficulty()
        if difficulty == 'Easy':
            self.pieces = easy_piece_collection
        elif difficulty == 'Normal':
            self.pieces = normal_piece_collection
        elif difficulty == 'Hard':
            self.pieces = hard_piece_collection
        
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music.mp3")    
        pygame.mixer.music.play(-1)                         # play music; argument of -1 loops music


        
