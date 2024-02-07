def encrypt(text, shift):
    cypher_text = ""
    for letter in text:
        if letter.isalpha():
            shift_amount = (ord(letter) + shift - ord('A')) % 26
            cypher_text += chr(ord('A') + shift_amount) if letter.isupper() else chr(ord('a') + shift_amount)
        else:
            cypher_text += letter
    return cypher_text

def decrypt(cypher_text, shift):
    return encrypt(cypher_text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encrypt or decrypt? ").lower()

    if choice == "encrypt":
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        result = encrypt(message, shift)
        print("Encrypted message:", result)

    elif choice == "decrypt":
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        result = decrypt(message, shift)
        print("Decrypted message:", result)

    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
