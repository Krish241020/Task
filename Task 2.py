InputStr= input("Enter Input String : ")

symbol = input("Enter Symbol String : ")

InputStr = InputStr.lower()

temp =""

for i in InputStr:
    if(i in symbol):
        pass
    else:
        
        temp+=i

if(temp == temp[::-1]):
    print("true")
else:
    print("false")
