def inverse(a,m):
    for i in range(1,m):
        if (a*i)%m==1:
            return i
    return None
def encryption(msg,a,b):
    result=""
    for char in msg:
        if char.isalpha():
            x=ord(char)-65
            result+=chr((a*x+b)%26 +65)
        else:
            result+=char
    return result
def decryption(msg,a,b):
    result=""
    a1=inverse(a,26)
    for char in msg:
        if char.isalpha():
            y=ord(char)-65
            result+=chr(a1*(y-b)%26 +65).lower()
        else:
            result+=char
    return result

msg = input("\nEnter Message : ")
a = int(input("Enter key a : "))
b = int(input("Enter key b : "))

enc = encryption(msg, a, b)
dec = decryption(enc, a, b)

print("\nEncrypted Text :", enc)
print("Decrypted Text :", dec, "\n")