import regex as re
import numpy as np
# import pandas as pd
# import random as r
# from itertools import combinations
# from itertools import product
# import itertools
import copy
import time

import pygame


class Sudoku:
    def __init__(self, grid, difficulty=0):
        self.starting_grid = grid.split('\n')
        #all what is under  the init method should probably be
        # into a new_grid(self) method

        #dummy values, some could be removed
        self.grid=[]
        self.brute_grid = []
        self.possibilities = []
        self.full_possibilities_table = []
        self.final_board = []

        self.start_time = time.time()
        self.elapsed_time = 0
        self.solved = False
        print(self.start_time)

        #Backtracking grid
        for line in self.starting_grid :
            self.grid.append(list(re.sub('_', '0', line)))
        # print(self.grid)
        # Brute Force Grid
        for line in self.starting_grid :
            self.brute_grid.append((re.sub('_', '0', line)))

        #Tunning Backtracking Grid
        temp_grid = []
        for i in range(9):
            temp_grid.append([int(j) for j in self.grid[i]])
        self.grid = temp_grid
        self.viable_starting_grid = copy.deepcopy(self.grid)


        self.loop = 0
        self.difficulty = difficulty

    def backtracking(self):
        if self.compleated():
            if self.solved == False:
                return self.final_board

        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1,10):
                        if self.validity_check(x, y, n):
                            self.grid[y][x] = n

                            self.backtracking()
                            self.grid[y][x]=0
                        self.loop += 1
                        # print(self.loop)
                    return


    def fake_brute_force(self, x=0, y=0, n=1) :
        #  is a brute force with back trackng

        if y == 9:
            return self.compleated()

        if self.grid[y][x] != 0:
            if x == 8:
                return self.fake_brute_force(0, y + 1)
            else:
                return self.fake_brute_force(x + 1, y)

        for n in range(n, 10):
            if self.validity_check(x, y, n):
                self.grid[y][x] = n
                if x == 8 :
                    if self.fake_brute_force(0, y + 1):
                        return True
                else :
                    if self.fake_brute_force(x+1, y) :
                        return True
                # print(f"y:{y} x:{x} n{n}")
                self.grid[y][x] = 0
        return False
    # would be performing better if it tooks the index of possible numbers to not
    # retest validity for every single character in line
    # def brute_force(self):
    #     self_bg = []
    #     for y in range(9) :
    #         temp_list = []
    #         poss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #         for n in self.viable_starting_grid[y]:
    #             if n in poss:
    #                 temp_list.append(n)
    #                 poss.remove(n)

    #         if 0 in temp_list :
    #             temp_list.remove(0)
    #         self_bg.append([poss, temp_list])

    #     for y in range(9):
    #         self.possibilities.append(
    #             list(itertools.permutations(self_bg[y][0],
    #                                         len(self_bg[y][0]))))
    ######RAM Kills Kernel
# for possibility in self.possibilities :
#             combinations = list(product(*possibility))
#             for comb in combinations :
#                 if len(comb == 9):
#                     self.full_possibilities_table.append(comb)

    def validity_check(self, x, y, n):
        if n > 9 or n < 1:
            print("number under 1 or over 9")
            return False
        for i in range(9):
            if self.grid[y][i] == n:
                # print("row fail")
                return False
        for j in range(9) :
            if self.grid[j][x] == n:
                # print("column fail")
                return False

        #block coordinates
        block_x = (x // 3)*3
        block_y = (y // 3)*3
        # print(f"x : {x} blkx {block_x}, y : {y} blky {block_y} n : {n}")
        block_content = []
        for h in range(3):
            for k in range(3):
                # print(self.grid[block_y + h][block_x + k])
                if self.grid[block_y + h][block_x + k] not in block_content :
                    block_content.append(self.grid[block_y+h][block_x+k])

        # print(block_content)
        if n in block_content:
            # print(np.matrix(block_content))
            # print("block fail")
            return False

        return True

    def compleate_valid_check(self) :
        false_count=0
        oplm=0
        for y in range(9):
            for x in range(9):
                for n in range(1,10):
                    if not self.validity_check(x,y,n):
                        return False
        return True

    def compleated(self):
        for o in range(9):
            # print(np.matrix(self.grid))
            # print(self.grid[o])
            if 0 in self.grid[o]:
                return False

                # return item in case we can't break the full recursion
        return self.resolved()

    def resolved(self):
        self.final_board = copy.deepcopy(self.grid)
        self.elapsed_time = time.time() - self.start_time
        # print("Congrats")
        self.solved = True
        return self.grid
        # may add numbers of tries or time spent

    def pygame(self):
        # initialise the pygame font
        pygame.font.init()
        # Total window
        screen = pygame.display.set_mode((500, 600))
        # Title
        pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
        font1 = pygame.font.SysFont("comicsans", 40)
        font2 = pygame.font.SysFont("comicsans", 20)
        x = 0
        y = 0
        dif = 500 / 9
        val = 0
        pygame.event.pump()
        screen.fill((255, 255, 255))

        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif),
                            (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif),
                            ((x + i) * dif, y * dif + dif), 7)

        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:

                    # Fill blue color in already numbered grid
                    pygame.draw.rect(screen, (0, 153, 153),
                                    (i * dif, j * dif, dif + 1, dif + 1))

                    # Fill grid with default numbers specified
                    text1 = font1.render(str(self.grid[i][j]), 1, (0, 0, 0))
                    screen.blit(text1, (i * dif + 15, j * dif + 15))
        # Draw lines horizontally and verticallyto form grid
        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif),
                            thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500),
                            thick)
        pygame.display.update()
        pygame.time.delay(20)




    def get_cord(self, pos):
        dif = 500 / 9
        global x
        x = self.pos[0] // dif
        global y
        y = self.pos[1] // dif



# grid_test = """_729___3_
# __1__6_8_
# ____4__6_
# 96___41_8
# _487_5_96
# __56_8__3
# ___4_2_1_
# 85__6_327
# 1__85____"""

grid_test = """__9_85_63
_7_96____
5_1__4___
__67_3__4
_4_21_39_
8___9__57
9845__6__
__7649_3_
61__2__4_"""


"""_________
_________
_________
_________
_________
_________
_________
_________
_________"""

"""__9_85_63
_7_96____
5_1__4___
__67_3__4
_4_21_39_
8___9__57
9845__6__
__7649_3_
61__2__4_"""
# """429185763
# 378962415
# 561374928
# 196753284
# 745218396
# 832496157
# 984531672
# 257649831
# 61382754_"""
# [[4, 2, 9, 1, 8, 5, 7, 6, 3], [3, 7, 8, 9, 6, 2, 4, 1, 5],
#  [5, 6, 1, 3, 7, 4, 9, 2, 8], [1, 9, 6, 7, 5, 3, 2, 8, 4],
#  [7, 4, 5, 2, 1, 8, 3, 9, 6], [8, 3, 2, 4, 9, 6, 1, 5, 7],
#  [9, 8, 4, 5, 3, 1, 6, 7, 2], [2, 5, 7, 6, 4, 9, 8, 3, 1],
#  [6, 1, 3, 8, 2, 7, 0, 4, 9]]

brute_grid = Sudoku(grid_test)

# print(grid.backtracking())

brute_grid.fake_brute_force()
print(np.matrix(brute_grid.grid))
print(brute_grid.elapsed_time)


back_tracking_grid = Sudoku(grid_test)

# print(grid.backtracking())

back_tracking_grid.backtracking()
print(np.matrix(back_tracking_grid.grid))
print(back_tracking_grid.elapsed_time)

print(f"Brute_grid took {brute_grid.elapsed_time}s to solve the grid while")
print(
    f"back_tracking_grid took {back_tracking_grid.elapsed_time}s to solve it"
)
# brute_grid.pygame()

# print(np.matrix(grid.final_board))

# print(grid.brute_force())
brute_tab = []
back_tab = []
for i in range(100) :
    brute_grid = Sudoku(grid_test)
    brute_grid.fake_brute_force()
    brute_tab.append(brute_grid.elapsed_time)

    back_grid = Sudoku(grid_test)
    back_tracking_grid.backtracking()
    back_tab.append(back_tracking_grid.elapsed_time)
if len(back_tab) == 100 and len(brute_tab) == 100:
    print(f"\nback_tracking was on average : {(sum(back_tab))/len(back_tab)}s\
        \nwhile brute_forcing was on average :{sum(brute_tab)/len(brute_tab)}s\
        \nand total : {sum(brute_tab)}s  "                                                                                    )
else :
    print("didn't make it to 100 or something")
print(back_tab)

# print(((sum(back_tab) / len(back_tab)) /\
#     (sum(brute_tab)) / len(brute_tab))*100)
