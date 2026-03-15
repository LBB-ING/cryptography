def caesar_decrypt(ciphertext, shift):
    """凯撒密码解密函数"""
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext):
    """暴力破解所有可能偏移量"""
    print("暴力破解结果：")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"偏移量 {shift}: {decrypted}")

if __name__ == "__main__":
    cipher = input("请输入凯撒密码密文：")
    brute_force_caesar(cipher)
