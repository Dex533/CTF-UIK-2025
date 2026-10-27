def knights_tour_encrypt(plaintext):
    grid = [['' for _ in range(4)] for _ in range(4)]
    plaintext = plaintext + '_' * (16 - len(plaintext))  # Pad to 16 chars
    
    # Define knight's move pattern
    moves = [
        (0,0), (1,2), (3,3), (2,1), (0,2), (1,0), 
        (3,1), (2,3), (0,1), (1,3), (3,2), (2,0),
        (0,3), (1,1), (3,0), (2,2)
    ]
    
    # Fill grid with plaintext in normal order
    text_index = 0
    for i in range(4):
        for j in range(4):
            grid[i][j] = plaintext[text_index]
            text_index += 1
    
    # Read out following knight's moves
    ciphertext = ""
    for move in moves:
        ciphertext += grid[move[0]][move[1]]
    
    return ciphertext

result = knights_tour_encrypt("FLAG")
print(f"Ciphertext: {result}")
