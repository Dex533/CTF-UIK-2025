def shifting_glyphs_encode(plaintext):
   
    
    # Apply Atbash cipher
    atbash_text = ""
    for char in plaintext:
        if char.isupper():
            # For uppercase: A(65) <-> Z(90), B(66) <-> Y(89), etc.
            atbash_text += chr(155 - ord(char))
        elif char.islower():
            # For lowercase: a(97) <-> z(122), b(98) <-> y(121), etc.
            atbash_text += chr(219 - ord(char))
        else:
            # Keep non-alphabetic characters unchanged
            atbash_text += char
    
    # Convert the Atbash result to ASCII decimal values
    final_cipher = ' '.join(str(ord(char)) for char in atbash_text)
    return final_cipher

# Example usage
plaintext = "Flag"
ciphertext = shifting_glyphs_encode(plaintext)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

