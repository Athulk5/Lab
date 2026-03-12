def create_matrix(key):
    used=[]
    matrix=[]
    key=key.upper()
    for ch in key:
        if ch not in used and ch!='J':
            used.append(ch)
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for i in alphabet:
        if i not in used:
            used.append(i)
    
    k=0
    for i in range(5):
        row=[]
        for j in range(5):
            row.append(used[k])
            k+=1
        matrix.append(row)
    return matrix

def find(matrix,a):
    a=a.upper()
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==a:
                return i,j

def encrypt(text,matrix):
    text=text.replace('J','I')
    cipher=" "

    i=0
    while i< len(text):
        a=text[i]

        if i+1 <len(text):
            b=text[i+1]
        else:
            b='X'
        
        if a==b:
            b='x'
            i+=1
        else:
            i+=2

        r1,c1=find(matrix,a)
        r2,c2=find(matrix,b)

        if r1==r2:
            cipher+= matrix[r1][(c1+1)%5]
            cipher+= matrix[r2][(c2+1)%5]
        elif c1==c2:
            cipher+= matrix[(r1+1)%5][c1]
            cipher+= matrix[(r2+1)%5][c2]
        else:
            cipher+= matrix[r1][c2]
            cipher+= matrix[r2][c1]
    return cipher

key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = create_matrix(key)

print("Playfair Matrix:")
for row in matrix:
    print(row)

cipher = encrypt(text, matrix)

print("Cipher Text:", cipher)

       

