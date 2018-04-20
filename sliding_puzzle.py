import random
def main():
    engine(starting_output())



#Creates a puzzle based on user input for width
def starting_output():
    width = int(input("Width: "))
    print("")
    numbers = []
    tiles = []
    [numbers.append(integer) for integer in range(0, width ** 2)]
    [tiles.append(numbers[i:i + width])\
    for i in range (0, width ** 2, width)]
    shuffled = shuffle_tiles(tiles)
    for i in range(0, len(shuffled)):
        [print("".join("[{0:2d}]".format(number)\
        for row in shuffled[i:i + 1] for number in row))]
    print("")
    return tiles



#Gets user inputs and calls other functions to
def engine(tiles):
    while get_manhattan_distance(tiles) != 0:
        letter = input("Move [W|A|S|D] | [Q]uit: ")
        if letter == "Q":
            print("Puzzle Complete!")
            return
        elif not (is_valid_move(copy_tiles(tiles), letter)):
            print("Invalid Move")
        else:
            print("")
            output = [i for i in move_tile(copy_tiles(tiles), letter)]
            for i in range(0, len(output)):
                [print("".join("[{0:2d}]".format(number)\
                for row in output[i:i + 1] for number in row))]
            print("")
        if get_manhattan_distance(tiles) == 0:
            print("Puzzle Complete!")
            return

        

#Extracts rows from the puzzle
def get_row(tiles, n):
    return [tiles.index(numbers) for numbers in tiles if n in numbers][0]


#Extracts columns from the puzzle
def get_col(tiles, n):
    return [numbers.index(n) for numbers in tiles if n in numbers][0]


#Checks if the move is valid per each user input
def is_valid_move(tiles, move):
    original = [get_col(tiles, 0), get_row(tiles, 0)]
    right = [original[0] + 1, get_row(tiles, 0)]
    left = [original[0] - 1, get_row(tiles, 0)]
    up = [get_col(tiles, 0), original[1] - 1]
    down = [get_col(tiles, 0), original[1] + 1]
    if move == "D" :
        return (right[0] < len(tiles[0]))
    elif move == "A" :
        return (left[0] > -1)
    elif move == "W" :
        return (up[1] > -1)
    if move == "S" :
        return (down[1] < len(tiles))


    
#Keeps each instance of tiles
def copy_tiles(tiles):
    return tiles[:]




#Replaces the current value with adjacent value and places 0 at position of adjacent value 
def move_tile(tiles, move):
    original = [get_col(tiles, 0), get_row(tiles, 0)]
    if move == "D":
        tiles[original[1]][original[0]] = tiles[original[1]][original[0] + 1]
        tiles[original[1]][original[0] + 1] = 0
    elif move == "A":
        tiles[original[1]][original[0]] = tiles[original[1]][original[0] - 1]
        tiles[original[1]][original[0] - 1] = 0
    elif move == "W":
        tiles[original[1]][original[0]] = tiles[original[1] - 1][original[0]]
        tiles[original[1] - 1][original[0]] = 0
    elif move == "S":
        tiles[original[1]][original[0]] = tiles[original[1] + 1][original[0]]
        tiles[original[1] + 1][original[0]] = 0
    return tiles



#Shuffles all tiles in the original puzzle according to a manhattan distance
def shuffle_tiles(tiles):
    while get_manhattan_distance(tiles) < len(tiles) ** 2:
        move = random.choice("WASD")
        if is_valid_move(copy_tiles(tiles), move):
            move_tile(copy_tiles(tiles), move)
    return tiles



#Calculates manhattan distance to determine the difficulty of the shuffled puzzle
def get_manhattan_distance(tiles):
    numbers = []
    final = []
    blank = []
    width = len(tiles)
    [numbers.append(number) for number in range(0, width ** 2)]
    [final.append(numbers[i:i + width]) for i in range(0, width ** 2, width)]
    for row in tiles:
        for number in row:
            if number != 0:
                blank.append(sum([abs(get_col(tiles, number) - \
                get_col(final, number)), abs(get_row(tiles, \
                number) - get_row(final, number))]))
    return sum(blank)



if __name__ == "__main__":
    main()