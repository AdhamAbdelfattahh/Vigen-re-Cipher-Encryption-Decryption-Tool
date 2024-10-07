# Caesar Cipher Encryption and Decryption

# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabet characters unchanged
        else:
            result += char
    
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(cipher_text, shift):
    result = ""
    
    # Traverse the cipher_text
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        
        # Leave non-alphabet characters unchanged
        else:
            result += char
    
    return result

# Main program
if __name__ == "__main__":
    # Input from user
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift number (0-25): "))

    # Encrypt or Decrypt based on user choice
    if choice == 'encrypt':
        print("Encrypted message: ", encrypt(text, shift))
    elif choice == 'decrypt':
        print("Decrypted message: ", decrypt(text, shift))
    else:
        print("Invalid choice!")
