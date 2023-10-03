import regex as re
import numpy as np
import pandas as pd
import random as r
# ONE_TO_NINE=[1,2,3,4,5,6,7,8,9]
# loops = 0
# loops_break = 500000
POSSIBILITIES = [1,2,3,4,5,6,7,8,9]


class Sudoku:
    def __init__(self, grid, difficulty=0):

        self.starting_grid = grid.split('\n')
        self.grid=[]
        print("here we are")
        for line in self.starting_grid :
            self.grid.append(list(re.sub('_', '0', line)))
        temp_grid = []
        for i in range(9):
            temp_grid.append([int(j) for j in self.grid[i]])
        self.grid = temp_grid
        self.viable_starting_grid = self.grid


        self.loop = 0
        self.difficulty = difficulty


    def backtracking(self):
        for y in range(9):
            for x in range(9):
                # print(self.grid)
                if self.grid[y][x] == 0:
                    for n in range(1,10):
                        self.loop += 1
                        if self.validity_check(x, y, n):
                            # print("valid checked")
                            self.grid[y][x] = n
                            self.backtracking()

                            self.grid[y][x]=0
                            # print(self.grid)
                            if self.loop < 10:
                                print(np.matrix(self.grid))

                            # if self.loop % 4000 == 0:
                            print(f"{self.loop} x:{x}, y:{y}")
                            print(np.matrix(self.grid))
                    return
        # return
        # return resolved


        # if loops == 1:
        #     print(grid.grid)

        # if loops %4000 == 0:
        #     print(loops)
        #     print(grid.grid)


        # if loops > loops_break:
        #     print(f"process didn't convey after {loops_break} tries")
        #     break


        # for n in range(9):
        #     if self.validity_check(x, y, n):
        #         self.grid[x][y] = n
        #     else :
        #         pass
        #while True :
        # for x in range(9):
        #     # print(grid.grid)
        #     for y in range(9):
        #         numbers = ONE_TO_NINE
        #         r.shuffle(numbers)
        #         for n in numbers:
        #             if self.validity_check(x, y, n):
        #                 self.grid[x][y] = n
        # x_numbers = ONE_TO_NINE
        # r.shuffle(x_numbers)
        # for x in x_numbers:
        #     # print(grid.grid)
        #     y_numbers = ONE_TO_NINE
        #     r.shuffle(y_numbers)
        #     for y in y_numbers:
        #         n_numbers = ONE_TO_NINE
        #         r.shuffle(n_numbers)
        #         for n in n_numbers:
        #             if self.validity_check(x-1, y-1, n):
        #                 self.grid[x-1][y-1] = n



    def brute_force(self):
        # #         self.grid=self.starting_grid
        # for n1 in range(1,10):
        #     for y in range(9):
        #         for x in range(9):
        #                 #take x as first elem
        #                 if self.validity_check(x, y, n):
        #                     self.grid[y][x]=n
        #                 #isvalid

        if self.compleated() :
            return self.grid
        # convert each range to strings by using ''.join then create a list with [1-9] and eliminate
        # values not valid at said position from this list then make a loop around all those values, and this 9 time ...




        # method return true or false for a number being valid at a certain position
        # could return the list of viable options instead
    def validity_check(self, x, y, n):
        # n is the number we want to fill isn

        # 1st
        # check if n already existed in vertical (y) axis
        # if exists, return False (not possible)
        for i in range(9):
            if self.grid[y][i] == n:
                return False

        # 2nd
        # check horizontal (x) axis
        for i in range(9):
            if self.grid[i][x] == n:
                return False

        # 3rd
        # check the 3x3 local grid
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.grid[y0+i][x0+j] == n:
                    return False

        # return true if pass all 3 checks.
        return True


    def compleated(self):
        for o in range(9):
            # print(self.grid)
            if 0 in self.grid[o]:
                return False
        return True

    # def reversing_grid(self):
    #     #transform [['a','b'], into [['a','c'],
    #     #           ['c','d']]       ['b','d']] work with longer lists
    #     return [list(tup) for tup in zip(self.grid)]

    def resolved(self):
        print("Congrats")
        return self.grid
        # may add numbers of tries or time spent

# if __name__ == "__main__":
#     grid1 = Sudoku('''_729___3_
#                     __1__6_8_
#                     ____4__6_
#                     96___41_8
#                     _487_5_96
#                     __56_8__3
#                     ___4_2_1_
#                     85__6_327
#                     1__85____''')

# print(
#     np.matrix('''_729___3_,
#                     __1__6_8_,
#                     ____4__6_,
#                     96___41_8,
#                     _487_5_96,
#                     __56_8__3,
#                     ___4_2_1_,
#                     85__6_327,
#                     1__85____'''))
# grid_test = """_729___3_
# __1__6_8_
# ____4__6_
# 96___41_8
# _487_5_96
# __56_8__3
# ___4_2_1_
# 85__6_327
# 1__85____"""

# grid_test = """__9_85_63
# _7_96____
# 5_1__4___
# __67_3__4
# _4_21_39_
# 8___9__57
# 9845__6__
# __7649_3_
# 61__2__4_"""

# grid = Sudoku(grid_test)
# # print(np.eye(9))
# # print(np.matrix([[6,2,3], [8,4,7]]))
# print(np.matrix(grid.grid))

# # print(grid.validity_check(3,3,5))
# # print(grid.validity_check(8,8,4))

# print(grid.backtracking())



def possible(y, x, n):
    global grid
    # n is the number we want to fill in

    # 1st
    # check if n already existed in vertical (y) axis
    # if exists, return False (not possible)
    for i in range(9):
        if grid[y][i] == n:
            return False

    # 2nd
    # check horizontal (x) axis
    for i in range(9):
        if grid[i][x] == n:
            return False

    # 3rd
    # check the 3x3 local grid
    # x0 = (x // 3) * 3
    # y0 = (y // 3) * 3
    # for i in range(3):
    #     for j in range(3):
    #         if grid[y0 + i][x0 + j] == n:
    #             return False


    #         #block coordinates
    # x0 = (x // 3) * 3
    # y0 = (y // 3) * 3
    # # print(f"x : {x} blkx {block_x}, y : {y} blky {block_y} n : {n}")
    # block_content = []
    # for i in range(3):
    #     for j in range(3):
    #         # print(self.grid[block_y + h][block_x + k])
    #         if grid[y0 + i][x0 + j] not in block_content:
    #             block_content.append(grid[y0 + i][x0 + j])


    # if n in block_content:
    #     return False


    # return true if pass all 3 checks.
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            # Find blank positions in the grid (value = 0)
            if grid[y][x] == 0:
                # Loop n from 1-9
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()

                        # This is where backtracking happens
                        # Reset the latest position back to 0 and try with new n value
                        grid[y][x] = 0
                return
    print(np.matrix(grid))


# grid = grid_test
# grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
#         [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
#         [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
#         [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
#         [0, 0, 0, 0, 8, 0, 0, 0, 0]]
grid = [[0,0,9,0,8,5,0,6,3], [0,7,0,9,6,0,0,0,0],
        [5,0,1,0,0,4,0,0,0], [0,0,6,7,0,3,0,0,4],
        [0,4,0,2,1,0,3,9,0], [8,0,0,0,9,0,0,5,7],
        [9,8,4,5,0,0,6,0,0], [0,0,7,6,4,9,0,3,0],
        [6,1,0,0,2,0,0,4,0]]


solve()
print('rrr')



#
#        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#         [6, 0, 0, 1, 9, 5, 0, 0, 0],
#         [0, 9, 8, 0, 0, 0, 0, 6, 0],
#         [8, 0, 0, 0, 6, 0, 0, 0, 3],
#         [4, 0, 0, 8, 0, 3, 0, 0, 1],
#         [7, 0, 0, 0, 2, 0, 0, 0, 6],
#         [0, 6, 0, 0, 0, 0, 2, 8, 0],
#         [0, 0, 0, 4, 1, 9, 0, 0, 5],
#         [0, 0, 0, 0, 8, 0, 0, 0, 0]]
