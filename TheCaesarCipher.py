text=input("write the line to encrypt :")
while True:
    shift=input("enter shift value  :")
    if shift.isdigit():
        shift=int(shift)
        break
crypted=""
for i in text :
    if i.isalpha():
        newl=ord(i)+shift
        if i.islower():
            if newl>ord("z"):
                newl=ord("a")+newl-(ord("z")+1)
            crypted+=chr(newl)
        if i.isupper():
            if  newl>ord("Z"):
                newl=ord("A")+newl-(ord("Z")+1)
            crypted+=chr(newl)
    else:
        crypted+=i
print(crypted)