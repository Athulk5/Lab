
text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

cipher = ""
k = 0

for  i in range(len(text)):
    p=ord(text[i])-65
    k=ord(key[k])-65
    cipher+=chr((p+k)%26+65)
    k=(k+1)%len(key)
print("Encrypted Text:", cipher)

plain=" "
k=0
for i in range(len(cipher)):
    c=ord(cipher[i])-65
    k=ord(key[k])-65

    plain+=chr((c-k)%26+65)

    k=(k+1)%len(key)
print("Decrypted Text:", plain)