from datetime import datetime

def create_polybius(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J removed
    key_square = ""
    for char in key.upper():
        if char not in key_square and char in alphabet:
            key_square += char
    for char in alphabet:
        if char not in key_square:
            key_square += char
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def bifid_encrypt(plaintext, key):
    square = create_polybius(key)
    plaintext = plaintext.upper().replace('J', 'I')
    
    # Get coordinates
    coords = []
    for char in plaintext:
        for row in range(5):
            for col in range(5):
                if square[row][col] == char:
                    coords.append((row, col))
    
    # Split and combine
    rows = [c[0] for c in coords]
    cols = [c[1] for c in coords]
    combined = rows + cols
    
    # Form new pairs and encrypt
    ciphertext = ""
    for i in range(0, len(combined), 2):
        row, col = combined[i], combined[i+1]
        ciphertext += square[row][col]
    
    return ciphertext

result = bifid_encrypt("FLAG", "CRYPTO")
print(f"Ciphertext: {result}") 