def encryption(msg,key):
    result=" "
    for char in msg:
        if char.isalpha():
            char=char.upper()
            result+=chr((ord(char)-65+key)%26+65)
        else:
            result+=char
    return result

def decryption(msg,key):
    result=" "
    for char in msg:
        if char.isalpha():
            result+=chr( (ord(char)-65-key)%26  +65  ).lower()
        else:
            result+=char
    return result

txt=input("\nEnter Message : ")

a=encryption(txt,3)
b=decryption(a,3)
print("The encrypted test is :",a)
print("The Decrypted test is :",b,"\n")


