# The program below exhausts all possible solutions in each puzzle cell to satisfy the row, column and cage restrictions presented by the user input and outputs the complete version of the Calcudoku Puzzle. The descriptions for the puzzle need to be input in the following format:

# - Number of cages: Total number of cages in the puzzle
# - Cage number n: Sum of all cells in the cage, number of cells in a cage, cell positions

# In the puzzle, cell positions are numbered starting from 0 at the upper left cell and increase by 1 from left to right.

# Listed below is the code for Calcudoku Solver and some sample inputs that you can use.






def main():


#Forms cages according to the specifications in the puzzle files and creates empty grids for inputs
    cages = []
    for i in range(0, int(input("Number of cages: "))):
        cages.append((input("Cage number " + str(i) + ": ")).split())
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    backtrack = 0
    check = 0
    cellnum = 0
    
    
#Increments by 1 in each cell, while checking for restrictions in the cages. If restrictions fail, backtracks and subtracts 1.
    while cellnum < 25:
        grid[(cellnum // 5)][cellnum % 5] += 1
        while not (validate_all(grid, cages)):
            check += 1
            grid[(cellnum // 5)][cellnum % 5] += 1
            if grid[(cellnum // 5)][cellnum % 5] >= 5 and not validate_all(grid, cages):
                backtrack += 1
                grid[(cellnum // 5)][cellnum % 5] = 0
                cellnum -= 1
                grid[(cellnum // 5)][cellnum%5] += 1	
        if (validate_all(grid,cages)) and 		grid[(cellnum // 5)][cellnum % 5] <= 5:
            check += 1
            cellnum += 1
    (printer(grid, check, backtrack))


#Takes in a 2d list of inputs, and prints single list of combined strings.
def printer(grid, check, backtrack):
    print("\n---Solution---\n")
    jump = 5
    string = []
    for e in grid:
        for i in e:
            string.append(str(i))
    final = ([" ".join(string[i:i + 5]) for i in 		range(0, len(string) - 1, jump)])
    for lists in final:
        print (lists)
    print("\nchecks: " + str(check), "backtracks: " + str(backtrack))


#Validates if the entire grid meets restrictions from inputs
def validate_all(grid, cages):
    return ((validate_rows(grid)) and (validate_cols(grid)) 
        and validate_cages(grid, cages))


#Validates if the row meets restrictions from inputs
def validate_rows(grid):
    for row in grid:
        rows = []
        for r in row:
            if r != 0:
                rows.append(r)
        if len(rows) != len(set(rows)):
            return False
    return True


#Validates if the column meets restrictions from inputs
def validate_cols(grid):
    new = grid[0] + grid[1] + grid[2] + grid[3] + grid[4]
    newcolumns = ([new[i::5] for i in range(0, 5)])
    
    for column in newcolumns:
        columns = []
        for c in column:
            if c != 0:
                columns.append(c)
        if len(columns) != len(set(columns)):
            return False
    return True


#Makes cages according to requirements and checks if they meet the sum
def validate_cages(grid, cages):
    new = grid[0] + grid[1] + grid[2] + grid[3] + grid[4]
    positions = []
    cage = []
    for i in cages:
        positions.append(i[2:])
    for p in positions:
        cage.append([new[int(a)] for a in p])
    for c in cage:
        if (0 in c) and (int(sum(c))) >= (int(cages[cage.index(c)][0])):
            return (0 not in c)
        elif (0 not in c) and (int(sum(c))) != (int(cages[cage.index(c)][0])):
            return (0 in c)
    else:
        return (int(sum(c))) >= 0


if __name__ == "__main__":
    main()