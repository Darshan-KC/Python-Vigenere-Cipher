class Vigenere:
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()

    def encrypt(self, message: str) -> str:
        return self._vigenere_transform(message, encrypt=True)

    def decrypt(self, message: str) -> str:
        return self._vigenere_transform(message, encrypt=False)

    def _vigenere_transform(self, message: str, encrypt: bool) -> str:
        result = []
        keystream_index = 0

        for char in message:
            if char.isalpha():
                # Get the current key character
                key_char = self.keyword[keystream_index % len(self.keyword)]
                
                # Get the appropriate base for case handling
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                
                # Calculate shift and apply encryption/decryption
                shift = ord(key_char) - ord('a')
                if not encrypt:
                    shift = -shift
                
                # Shift the character
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(shifted_char)
                
                # Only increment key index for alphabetic characters
                keystream_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                result.append(char)

        return ''.join(result)
