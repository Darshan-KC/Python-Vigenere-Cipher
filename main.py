class Vigenere:
    def __init__(self, keyword:str) -> None:
        self.keyword = keyword
        
    def encrypt(self, message) -> str:
        keyword = (self.keyword * (len(message) // len(self.keyword) + 1))[:len(message)]
        result = ''
        for i, char in enumerate(message):
            shift = ord(keyword[i].lower()) - ord('a')
            if 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif 'a' <= char <='z':
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += char
        return result
    
    def decrypt(self, message) ->str:
        pass
    
def main():
    # try:
        vigenere = Vigenere("ram") # you can use shift value from user also
        choice = int(input("Choose mode: \n1. Encrypt \n2. Decrypt\n: "))
        if choice == 1:
            message = input("Enter the message to encrypt: ")
            result = vigenere.encrypt(message)
            print(f"Encryption of '{message}' is '{result}'")
            
        elif choice == 2:
            message = input("Enter the encypted message to decrypt: ")
            result = vigenere.decrypt(message)
            print(f"Decryption of '{message}' is '{result}'")
        else:
            print("Invalid choice")
        
    # except:
    #     print("Exception occurs")

if __name__ == "__main__":
    main()