def chiffrement_cesar(message):
    decalage = 3
    message_chiffre = ""
    
    for char in message:
        if char.isalpha():
         
            if char.isupper():
                lettre_chiffree = chr((ord(char) - ord('A' ) + decalage) % 26 + ord('A'))
          
            else:
                lettre_chiffree = chr((ord(char) - ord('a' ) + decalage) % 26 + ord('a'))
            message_chiffre += lettre_chiffree
        else:
         
            message_chiffre += char

    return message_chiffre

def main():
    message_non_code = input("Entrez le message à coder : ")

    message_code = chiffrement_cesar(message_non_code)

    print(f"Message : {message_code}")

if __name__ == "__main__":
    main()
