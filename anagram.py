text1=input("enter first text :")
text2=input("enter second  text :")
anagram=False
if len(text1)==len(text2):
    for i in text1:
        if i in text2:
            anagram=True
        else:
            anagram=False
if anagram:
    print("it's anagram")
else:
    print("it's not anagram")