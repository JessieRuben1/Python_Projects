# school_scores = [[78, 85, 69, 89, 95], 
#                 [78, 56, 87, 89, 57], 
#                 [89, 98, 99, 90, 68], 
#                 [54, 56, 51, 48, 99]]

# row_index = 0

# for row in school_scores:
#     print(f'Term {row_index + 1 }: ')
#     row_index += 1
#     for col in row:
#         print(col, end = "% ")
    
#     print()
In_board = ["---##",

         "-#---",

         "--#--",

         "-##--",

         "-----"]

offs = [ (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1) ]

res  = [ [[0,"#"][c=="#"] for c in row] for row in In_board] # initialization of minesweeper

for r,s in enumerate(In_board):  # go through rows of minesweeper

    for c,m in enumerate(s):  # co through corresponding columns

        for dr,dc in [] if m=="#" else offs: # neighboring cells of "-" cells

            if r+dr in range(len(In_board)) and c+dc in range(len(s)):

                res[r][c] += In_board[r+dr][c+dc] == "#" # counting mines in array

                
for row in res:

    for c in row:

        print(c,end=" ")

    print()     #Printing a resulting array