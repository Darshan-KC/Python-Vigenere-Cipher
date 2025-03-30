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
        keyword = (self.keyword * (len(message) // len(self.keyword) + 1))[:len(message)]
        result = ''
        for i, char in enumerate(message):
            shift = ord(keyword[i].lower()) - ord('a')
            if 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif 'a' <= char <='z':
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += char
        return result