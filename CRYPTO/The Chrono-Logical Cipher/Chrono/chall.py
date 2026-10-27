from datetime import datetime

def chrono_encrypt_debug(plaintext, date_str):
    print(f"Input - Plaintext: '{plaintext}', Date: '{date_str}'")
    
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    key = date_obj.strftime("%B").upper()
    print(f"Key: '{key}'")
    
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = key[i % len(key)]
            shift = ord(key_char) - ord('A')
            print(f"Char: '{char}', Key char: '{key_char}', Shift: {shift}")
            
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            ciphertext += new_char
            print(f"Encrypted: '{char}' -> '{new_char}'")
        else:
            ciphertext += char
    
    print(f"Final ciphertext: '{ciphertext}'")
    return ciphertext

# Test
chrono_encrypt_debug("FLAG", "07/04/1776")

