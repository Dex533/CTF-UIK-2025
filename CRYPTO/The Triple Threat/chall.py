plaintext = "VICTORY"
key_word = "THREE"
ciphertext = ""

for i, char in enumerate(plaintext.replace(" ", "")):
    if char == " ":
        ciphertext += " "
        continue
    key_char = key_word[i % len(key_word)]
    shift = ord(key_char) - ord('A')
    # Caesar encryption
    new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    ciphertext += new_char
    # Add space for readability after 2 chars
    if i == 1:
        ciphertext += " "

print(f"Ciphertext: {ciphertext}")  # FX LTWJ


