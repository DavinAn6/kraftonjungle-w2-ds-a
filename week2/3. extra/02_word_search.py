
""" 
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


def exist(board, word):
    """ 
    TRIAL1:
        - Look for first alphabet in the 2D array
            - Easiest way is nested for loop
            - Can't use index on a 2D array
                - Flatten the array > find the index > mod by board width to find actual location
                - Problem because list.index(val) only returns first occurrance
        - Use Backtracking
            - Start from the indices of the first letter
            - Assume there would be 4 branches from each letter (left, right, up, down)
            - Unless break condition is met : no element for one of the four
            - Recursion with going down 4 branches

    PERFORMANCE: 1857ms (Beats 92.64%)
        - Straightforward backtracking. Not much room to improve efficiency.
    """
    
    width = len(board[0])
    flattened_board = sum(board, [])
    success = False
    
    
    # board_index = point to start search from
    # letter_index = what we are searching for. next letter in the word
    def search_adjacent(board_index, letter_index):
        nonlocal success
        
        if (letter_index >= len(word)):
            success = True
            return
        
        # print("search(" + str(board_index) + ", " + str(letter_index) + ")")
        # Left
        if (board_index%width != 0):    # Element exists
            if (flattened_board[board_index-1] == word[letter_index]):  # Element matches next letter
                # print("found word index " + str(letter_index) + " in left cell with index " + str(board_index-1))
                flattened_board[board_index-1] = 0                      # Letter is used. Remove from board for now
                search_adjacent(board_index-1, letter_index+1)          # Recursion
                flattened_board[board_index-1] = word[letter_index]     # Didn't pan out. Add letter back in.
        
        # Right
        if (board_index%width != (width-1)):
            if (flattened_board[board_index+1] == word[letter_index]):
                # print("found word index " + str(letter_index) + " in right cell with index " + str(board_index+1))
                flattened_board[board_index+1] = 0    
                search_adjacent(board_index+1, letter_index+1)
                flattened_board[board_index+1] = word[letter_index]
        
        # Up
        if (board_index >= width):
            if (flattened_board[board_index-width] == word[letter_index]):
                # print("found word index " + str(letter_index) + " in up cell with index " + str(board_index-width))
                flattened_board[board_index-width] = 0    
                search_adjacent(board_index-width, letter_index+1)
                flattened_board[board_index-width] = word[letter_index]
        
        # Down
        if (len(flattened_board)-board_index > width):
            if (flattened_board[board_index+width] == word[letter_index]):
                # print("found word index " + str(letter_index) + " in down cell with index " + str(board_index+width))
                flattened_board[board_index+width] = 0    
                search_adjacent(board_index+width, letter_index+1)
                flattened_board[board_index+width] = word[letter_index]
        
        # print("search(" + str(board_index) + ", " + str(letter_index) + ") unsuccessful") 
        # print(flattened_board)
        return # No more adjacent elements to check
    
    index = [i for i, val in enumerate(flattened_board) if val == word[0]]
    for i in index:
        flattened_board[i] = 0
        search_adjacent(i, 1)
        flattened_board[i] = word[0]
    
    return success





board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]    # True
word1 = "ABCCED"
print(exist(board1, word1))

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]    # True
word2 = "SEE"
print(exist(board2, word2))

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]    # False
word3 = "ABCB"
print(exist(board3, word3))

board4 = [["a","a"]]
word4 = "aaa"
print(exist(board4, word4))

