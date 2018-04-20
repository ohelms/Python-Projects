# This program locates specified words in 10x10 puzzle created from random characters and outputs their locations. The input should read in the following:
    
#     - 100-character string puzzle
#     - Series of words to search vertically or horizontally 



def main():
    
    #Requests user input
    puzzle=str(input())
    words=str(input())

    

    #Iterates through create rows to create and print a puzzle
    print ("Puzzle:\n")
    for i in create_rows(puzzle):
        print (i)
    print("")

    #iteration to take word in words and input it into the find function
    for word in (words.split()):
        print (find_word((create_rows(puzzle)),
            (create_columns(puzzle)), word))


        
#Returns a list of 10-character strings representing individuals columns from an input 100-character string
def create_columns(puzzle):
    return ([puzzle[i::10] for i in range(0, 10)])



#Returns a list of 10-character strings representing individuals rows from an input 100-character string
def create_rows(puzzle):
    return ([puzzle[i:i + 10] for i in range(0, len(puzzle), 10)])


#Searches the input rows and columns for a given word and returns a formatted string
def find_word(rows, columns, word):
    reverse = 9
    for r in rows:
        if (r.find(word)) > -1:
            return (str(word) + ": (FORWARD) row: " + str(rows.index(r)) + 
            " column: " + str(r.find(word)))
        elif (r[::-1].find(word)) > -1:
            return (str(word) + ": (BACKWARD) row: " + str(rows.index(r)) 
            + " column: " + str(reverse - (r[::-1]).find(word)))
    for c in columns:
        if (c.find(word)) > -1:
            return (str(word) + ": (DOWN) row: " + str(c.find(word)) + 
            " column: " + str(columns.index(c)))
        elif (c[::-1].find(word)) > -1:
            return (str(word) + ": (UP) row: " + 
            str(reverse - (c[::-1]).find(word)) + " column: " + 
            str(columns.index(c)))
    for c in columns:
        if c.find(word) == -1:
            return str(word)+': word not found'



if __name__ == "__main__":
    main()