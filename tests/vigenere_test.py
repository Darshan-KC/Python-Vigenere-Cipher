import pytest
from vigenere import Vigenere

@pytest.fixture
def cipher():
    return Vigenere("KEY")  # Example keyword


# Test Encryption
def test_encrypt(cipher):
    assert cipher.encrypt("HELLO") == "RIJVS"
    assert cipher.encrypt("hello") == "rijvs"
    assert cipher.encrypt("Hello World!") == "Rijvs Uyvjn!"
    assert cipher.encrypt("Python 3.12") == "Zidexn 3.12"

# Test Decryption
def test_decrypt(cipher):
    assert cipher.decrypt("RIJVS") == "HELLO"
    assert cipher.decrypt("rijvs") == "hello"
    assert cipher.decrypt("Rijvs Uyvjn!") == "Hello World!"
    assert cipher.decrypt("Zidexn 3.12") == "Python 3.12"

# Test with special characters and numbers
def test_special_characters(cipher):
    assert cipher.encrypt("12345") == "12345"
    assert cipher.decrypt("12345") == "12345"
    assert cipher.encrypt("@!#$%") == "@!#$%"
    assert cipher.decrypt("@!#$%") == "@!#$%"