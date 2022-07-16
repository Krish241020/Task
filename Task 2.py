
InputString= input("InputString : ")

trash=input("TrashSymbolsString : ")

InputString = InputString.lower()

temp =""


for i in InputString:
    if(i in trash):
        pass
    else:
        
        temp+=i

if(temp == temp[::-1]):
    print("true")
else:
    print("false")
