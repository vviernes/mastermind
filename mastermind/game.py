import pygame
import requests
from mastermind.constants import *


class Game():
    def __init__(self, difficulty, max_attempts):
        self.difficulty = difficulty
        self.max_attempts = max_attempts
        self.attempt = 1
        self.music_on = True
        self.board = [ [], [], [], [], [], [], [], [], [], [] ]
        self.secret_code_num = self.set_secret_code_num()
        self.secret_code_color = self.set_secret_code_color()
        self.current_guess = []

    def get_board(self):
        return self.board
    
    def get_board_at_index(self, index):
        return self.board[index]
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_attempt(self):
        return self.attempt
    
    def get_max_attempt(self):
        return self.max_attempts
    
    def get_music_on(self):
        return self.music_on

    def get_secret_code_num(self):
        return self.secret_code_num
    
    def get_secret_code_color(self):
        return self.secret_code_color
    
    def get_current_guess(self):
        return self.current_guess
    
    def set_music_on(self, music_on):
        self.music_on = music_on
    
    def set_secret_code_num(self):
        secret_code = []
        difficulty = self.get_difficulty()
        if difficulty == 'Easy':
            response = requests.get('https://www.random.org/integers/?num=4&min=0&max=3&col=1&base=10&format=plain&rnd=new')        # 4 digits
        elif difficulty == 'Normal':
            response = requests.get('https://www.random.org/integers/?num=4&min=0&max=5&col=1&base=10&format=plain&rnd=new')        # 6 digits
        elif difficulty == 'Hard':
            response = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')        # 8 digits
        random = response.text
        secret_code = []
        for char in random:
            if char != '\n':
                secret_code.append(int(char))
        return secret_code

    def set_secret_code_color(self):
        num_to_color_mapping = {
            0 : 'red',
            1 : 'yellow',   
            2 : 'blue',
            3 : 'purple',
            4 : 'orange',
            5 : 'green',
            6 : 'navy',
            7: 'pink'
        }
        secret_code_num = self.get_secret_code_num()
        secret_code_color = []
        for num in secret_code_num:
            secret_code_color.append(num_to_color_mapping[num])
        return secret_code_color
    
    def set_current_guess(self, guess):
        self.current_guess = guess

    def increment_attempt(self):
        self.attempt += 1
    
    def toggle_music(self):
        if self.get_music_on() is True:
            pygame.mixer.music.set_volume(0)
            self.set_music_on(False)
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.set_volume(1)
            self.set_music_on(True)
            pygame.mixer.music.unpause()

    def place_color(self, color):
        color_to_asset_mapping = {
            'red': piecered,
            'yellow': pieceyellow,   
            'blue': pieceblue,
            'purple': piecepurple,
            'orange': pieceorange,
            'green': piecegreen,
            'navy': piecenavy,
            'pink': piecepink 
        }
        asset = color_to_asset_mapping[color]
        attempt = self.get_attempt()
        row = attempt - 1
        board = self.get_board_at_index(row)
        col = len(board)
        if col <= 3:
            WINDOW.blit(asset, (175 + SQUARE_SIZE * col, 800 - SQUARE_SIZE * row))
            board.append(color)
        
    def redo_guess(self):
        attempt = self.get_attempt()
        row = attempt - 1
        self.get_board()[row] = []

        pygame.draw.rect(WINDOW, DGRAY, (100,800 - SQUARE_SIZE * (attempt - 1), 300, SQUARE_SIZE))              # redraw submit guess space
        WINDOW.blit(submitwaiting, (100, 800 - SQUARE_SIZE * (attempt - 1)))
 
        for col in range(4):                                                                                    # redraw guess holes
            WINDOW.blit(piecewhite, (175  + SQUARE_SIZE * col, 800 - SQUARE_SIZE * (attempt - 1)))

    def draw_submit_button(self):
        attempt = self.get_attempt()
        row = attempt - 1
        pygame.draw.rect(WINDOW, DGRAY, (100,800 - SQUARE_SIZE * (attempt - 1), SQUARE_SIZE, SQUARE_SIZE))
        WINDOW.blit(submitready, (100, 800 - SQUARE_SIZE * (row)))

    def submit_guess(self):
        attempt = self.get_attempt()
        row = attempt - 1
        pygame.draw.rect(WINDOW, DGRAY, (100,800 - SQUARE_SIZE * (row), SQUARE_SIZE, SQUARE_SIZE))
        WINDOW.blit(submitconfirm, (100, 800 - SQUARE_SIZE * (row)))

    def give_clue(self):
        attempt = self.get_attempt()
        secret_code_color = self.get_secret_code_color()
        current_guess_copy = []
        secret_copy = []
        clue_array = []

        for color in self.get_current_guess():
            current_guess_copy.append(color)
        for color in secret_code_color:
            secret_copy.append(color)

        for i in range(4):
            if current_guess_copy[i] == secret_code_color[i]:
                clue_array.append(cluepink)
                secret_copy[i] = None
                current_guess_copy[i] = None
        for i in range(4):
            if current_guess_copy[i] != None and current_guess_copy[i] in secret_copy:
                clue_array.append(clueblue)
                secret_copy.remove(current_guess_copy[i])

        for i in range(len(clue_array)):
            WINDOW.blit(clue_array[i], (400  + SQUARE_SIZE/2 * i, 800 - (SQUARE_SIZE * (attempt - 2))))
    
    def check_code_to_win(self):
        if self.get_current_guess() == self.get_secret_code_color():
            return True
        else:
            return False

    def show_answer(self):
        color_to_asset_mapping = {
            'red': piecered,
            'yellow': pieceyellow,   
            'blue': pieceblue,
            'purple': piecepurple,
            'orange': pieceorange,
            'green': piecegreen,
            'navy': piecenavy,
            'pink': piecepink 
        }
        pygame.draw.rect(WINDOW, DGRAY, (175,300, 200, SQUARE_SIZE))
        WINDOW.blit(answerleft, (85,275))
        WINDOW.blit(answerright, (365,275))
        
        secret_color_code = self.get_secret_code_color()
        for i in range(len(secret_color_code)):
            WINDOW.blit(color_to_asset_mapping[secret_color_code[i]], (175 + SQUARE_SIZE*i, 300))
        pygame.display.update()
    
    

