def ma_hoa_caesar(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            shift = 65 if char.isupper() else 97  
            ciphertext += chr((ord(char) - shift + k) % 26 + shift)
        else:
            ciphertext += char  
    return ciphertext

def giai_ma_caesar(ciphertext, k):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift - k) % 26 + shift)
        else:
            plaintext += char
    return plaintext


if __name__ == "__main__":
    k = 30   
    plaintext = "Truong Huynh Thao Ngan"

    ciphertext = ma_hoa_caesar(plaintext, k)
    print("Plaintext :", plaintext)
    print("STT (k)   :", k)
    print("Ciphertext:", ciphertext)

    giai_ma = giai_ma_caesar(ciphertext, k)
    print("Giải mã   :", giai_ma)
