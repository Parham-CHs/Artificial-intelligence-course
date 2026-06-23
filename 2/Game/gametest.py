import numpy as np
import random
import pygame
import math
from time import sleep, time

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
PLAYER = 1
CPU = -1
EMPTY = 0
PLAYER_PIECE = 1
CPU_PIECE = -1
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WINDOW_LENGTH = 4
WINING_SCORE = 10000000000000

class Connect4UI:
    def __init__(self, width=COLUMN_COUNT*SQUARESIZE, height=(ROW_COUNT+1)*SQUARESIZE):
        pygame.init()
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont("monospace", 75)

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(self.screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), self.height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == CPU_PIECE:
                    pygame.draw.circle(self.screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), self.height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        pygame.display.update()
        sleep(0.2)
        

    def display_winner(self, winner):
        if winner == PLAYER:
            label = self.font.render("Player wins!!", 1, RED)
        elif winner == CPU:
            label = self.font.render("Computer wins!!", 1, YELLOW)
        else:
            label = self.font.render("It's a draw!!", 1, BLUE)
        self.screen.blit(label, (40, 10))
        pygame.display.update()
        sleep(5)


class Connect4Game:
    def __init__(self, ui, minimax_depth=1, prune=True):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        self.ui = Connect4UI() if ui else None
        self.minimax_depth = minimax_depth
        self.prune = prune
        self.current_turn = random.choice([1, -1])
        
    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def get_next_open_row(self, board,col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(self, board):
        print(np.flip(board, 0))

    def winning_move(self, board, piece):
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if all(board[r][c+i] == piece for i in range(WINDOW_LENGTH)):
                    return True

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if all(board[r+i][c] == piece for i in range(WINDOW_LENGTH)):
                    return True

        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if all(board[r+i][c+i] == piece for i in range(WINDOW_LENGTH)):
                    return True

        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if all(board[r-i][c+i] == piece for i in range(WINDOW_LENGTH)):
                    return True

        return False
    
    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opp_piece = CPU_PIECE
        
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2
        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4
        
        return score
    
    def score_position(self, board, piece):
        score = 0  
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3
    
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(COLUMN_COUNT-3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(ROW_COUNT-3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)
                
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)
    
        return score
    
    def is_terminal_node(self, board):
        return self.winning_move(board, PLAYER_PIECE) or self.winning_move(board, CPU_PIECE) or len(self.get_valid_locations(board)) == 0
    
    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if board[ROW_COUNT-1][col] == 0:
                valid_locations.append(col)
        return valid_locations
    
    def best_cpu_score(self, board, moves):
        move = None
        max_score = -math.inf
        for col in moves:
            row = self.get_next_open_row(board, col)
            b_copy = board.copy()
            self.drop_piece(b_copy, row, col, CPU_PIECE)
            score = self.heuristic(b_copy, CPU_PIECE)
            if score > max_score:
                max_score = score
                move = col
        return move
    
    def heuristic(self, board, piece):
        if(self.is_terminal_node(board)):
            if self.winning_move(board, piece):
                return WINING_SCORE
            elif self.winning_move(board, -piece):
                return -WINING_SCORE
            else:
                return 0
        else:
            return self.score_position(board, piece) - self.score_position(board, -piece)
        
    #TODO: Implement minimax algorithm with alpha-beta pruning and depth limiting
    #self.prune is a boolean that indicates whether to use alpha-beta pruning or not
    #Use the heuristic function as the evaluation function for non terminal nodes
    #Return the column and the score of the best move
    def minimax(self, board, depth, alpha, beta, player):
        if depth == 0 or self.is_terminal_node(board):
            return None, self.heuristic(board, player)

        # Set initial values and conditions based on player type
        maximizing = player == CPU
        best_score = -math.inf if maximizing else math.inf
        best_move = None

        for col in self.get_valid_locations(board):
            row = self.get_next_open_row(board, col)
            b_copy = board.copy()
            self.drop_piece(b_copy, row, col, CPU_PIECE if maximizing else PLAYER_PIECE)

            # Alternate the player for the next recursive call
            _, score = self.minimax(b_copy, depth - 1, alpha, beta, PLAYER if maximizing else CPU)

            # Update best score and move based on player type
            if maximizing:
                if score > best_score:
                    best_score = score
                    best_move = col
                alpha = max(alpha, best_score)
            else:
                if score < best_score:
                    best_score = score
                    best_move = col
                beta = min(beta, best_score)

            # Prune if conditions are met
            if self.prune and beta <= alpha:
                break

        return best_move, best_score

       
        
    def get_cpu_move(self, board, randomness_percent=30):
        moves = self.get_valid_locations(board)
        if len(moves) == 0:
            return None
        random_move = random.choice(moves)
        score_move = self.best_cpu_score(board, moves)
        move = random.choice([score_move] * (100 - randomness_percent) + [random_move] * randomness_percent)
        return move, self.get_next_open_row(board, move)


    def get_human_move(self, board, depth = 1):
        col = self.minimax(board, depth, -math.inf, math.inf, self.current_turn)[0]
        return col, self.get_next_open_row(board, col)

    def play(self):
        winner = None
        while not self.is_terminal_node(self.board):
            if self.ui:
                self.ui.draw_board(self.board)
            if self.current_turn == PLAYER:
                col, row = self.get_human_move(self.board, self.minimax_depth)
                if col is not None:
                    self.drop_piece(self.board, row, col, PLAYER_PIECE)
                    if self.winning_move(self.board, PLAYER_PIECE):
                        winner = PLAYER
                    self.current_turn = CPU
            else:
                col, row = self.get_cpu_move(self.board)
                if col is not None:
                    self.drop_piece(self.board, row, col, CPU_PIECE)
                    if self.winning_move(self.board, CPU_PIECE):
                        winner = CPU
                    self.current_turn = PLAYER
            
            if self.ui:
                self.ui.draw_board(self.board)
                if winner is not None:
                    self.ui.display_winner(winner)
                            
        if winner is None:
            winner = 0
        return winner
    

def print_results(results, depth, pruning, start, end):
    pruning_status = "Enabled" if pruning else "Disabled"
    print(
        f'Depth: {depth} | Pruning: {pruning_status} -> User Wins: {results[1]:3}, CPU Wins: {results[-1]:2}, Ties: {results[0]:2}, Time: {end - start:.2f}s'
    )




game = Connect4Game(True, 3, True)
game.play()




def check_results():
    for pruning in [True, False]:  
        for d in range(1, 4):
            results = {-1: 0, 0: 0, 1: 0}
            start = time()
            for _ in range(20):  
                game = Connect4Game(False, d, pruning)  
                results[game.play()] += 1
            end = time()
            print_results(results, d, pruning, start, end)

check_results()