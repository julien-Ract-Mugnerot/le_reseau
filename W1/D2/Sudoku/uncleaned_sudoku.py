import regex as re
import numpy as np
import pandas as pd
import random as r
from itertools import combinations
from itertools import product
import itertools
import copy


class Sudoku:
    def __init__(self, grid, difficulty=0):
        self.starting_grid = grid.split('\n')
        # print(self.starting_grid)

        #dummy values
        self.grid=[]
        self.brute_grid = []
        self.possibilities = []
        self.full_possibilities_table = []
        self.final_board = []

        self.last_n=0
        # print("here we are")
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
        if not self.compleated():
            for y in range(9):
                for x in range(9):
                    if self.grid[y][x] == 0:
                        for n in range(1,10):
                            if self.validity_check(x, y, n):
                                self.grid[y][x] = n

                                self.backtracking()
                                self.grid[y][x]=0
                            self.loop += 1
                            print(self.loop)
                        return grid.final_board


    def fake_brute_force(self, x=0, y=0, n=0) :
        if not self.compleated():
            for y in range(9):
                for x in range(9):
                    if self.grid[y][x] == 0:
                        for n in range(self.last_n + 1, 10):
                            if self.validity_check(x, y, n):
                                self.grid[y][x] = n
                                self.fake_brute_force(x-1,y,n)
                                self.grid[y][x] = 0
                                self.last_n = n
                            else :
                                self.last_n = 0
                            self.loop += 1
                            # print(self.loop)
                        return grid.final_board

    # would be performing better if it tooks the index of possible numbers to not
    # retest validity for every single character in line
    def brute_force(self):
        self_bg = []
        for y in range(9) :
            temp_list = []
            poss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for n in self.viable_starting_grid[y]:
                # print(n)
                # print(poss)
                if n in poss:
                    temp_list.append(n)
                    poss.remove(n)

            # poss list of numbers that aren't in the each row of the start grid excluding 0
            # temp recover all numbers in each row of the starting grid excluding 0

            if 0 in temp_list :
                temp_list.remove(0)
            self_bg.append([poss, temp_list])

        #self.possibilities = [] at __init__
        for y in range(9):
            self.possibilities.append(
                list(itertools.permutations(self_bg[y][0],
                                            len(self_bg[y][0]))))
        # print(self_bg)
        # print(self.possibilities[0])
        #self.full_possibilities = [] at __init__

        for possibility in self.possibilities :
            combinations = list(product(*possibility))
            for comb in combinations :
                if len(comb == 9):
                    self.full_possibilities_table.append(comb)
        # for i in range(1,9):
        #     self.full_possibilities_table[i].sort()
        #     #need to check if it needs to be changed directly in self.full_possibilities_table[i] =
        #     list(self.full_possibilities_table[i]
        #          for self.full_possibilities_table[i], _ in itertools.groupby(
        #              self.full_possibilities_table[i]))


        # method return true or false for a number being valid at a certain position
        # could return the list of viable options instead
    def validity_check(self, x, y, n):
        # print(self.grid[x][y])
        # if self.grid[x][y] !=0:
        #     return False
        # print(self.viable_starting_grid[x][y])
        # if self.viable_starting_grid[x][y] == self.grid[x][y] \
        #                         and self.grid[x][y] != 0:
        #     return False
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
            # print(self.grid)
            print(self.grid[o])
            if 0 in self.grid[o]:
                return False

                # return item in case we can't break the full recursion
        return self.resolved()

    # def reversing_grid(self):
    #     #transform [['a','b'], into [['a','c'],
    #     #           ['c','d']]       ['b','d']] work with longer lists
    #     return [list(tup) for tup in zip(self.grid)]

    def resolved(self):
        # print(self.grid)
        self.final_board = copy.deepcopy(self.grid)
        print("Congrats")
        return self.grid
        # may add numbers of tries or time spent

# grid_test = """_729___3_
# __1__6_8_
# ____4__6_
# 96___41_8
# _487_5_96
# __56_8__3
# ___4_2_1_
# 85__6_327
# 1__85____"""

grid_test = """_________
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
# """__9_85_63
# _7_96____
# 5_1__4___
# __67_3__4
# _4_21_39_
# 8___9__57
# 9845__6__
# __7649_3_
# 61__2__4_"""
# [[4, 2, 9, 1, 8, 5, 7, 6, 3], [3, 7, 8, 9, 6, 2, 4, 1, 5],
#  [5, 6, 1, 3, 7, 4, 9, 2, 8], [1, 9, 6, 7, 5, 3, 2, 8, 4],
#  [7, 4, 5, 2, 1, 8, 3, 9, 6], [8, 3, 2, 4, 9, 6, 1, 5, 7],
#  [9, 8, 4, 5, 3, 1, 6, 7, 2], [2, 5, 7, 6, 4, 9, 8, 3, 1],
#  [6, 1, 3, 8, 2, 7, 0, 4, 9]]

grid = Sudoku(grid_test)
# print(np.eye(9))
# print(np.matrix([[6,2,3], [8,4,7]]))
# print(np.matrix(grid.grid))

# print(grid.validity_check(3,3,5))
# print(grid.validity_check(8,8,4))
# print(grid.backtracking())

print(grid.fake_brute_force())
# print(np.matrix(grid.final_board))
# print(grid.grid)




# print(grid.brute_force())
# print(grid.brute_force())
