text=input('enter text to test : ')
newtext=""
for i in text :
    text=newtext+i.lower()
text_without_spaces=text.replace(" ","")

if (text_without_spaces==text_without_spaces[::-1]):
    print(" it's palindrom")
else:
    print("it's not palindrom")