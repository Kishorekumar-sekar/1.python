class MultipleFunctions():
    def oddEven():
        num=int(input("Enter the Number:"))
        if((num%2)==1):
            print(num,"Odd Number")
            message= "Odd Number"
        else:
            print(num,"Even Number")
            message= "Even Number"
        return message
    def Agecategory():
        Age=int(input("Enter the Age:"))
        if(Age<18):
            print("Children")
            cate= "Children"
        elif(Age<35):
            print("Adult")
            cate= "Adult"
        elif(Age<59):
            print("Citizen")
            cate= "Citizen"
        else:
            print("Senior citizen")
            cate= "Senior Citizen"
        return cate
    def BMI():
        Index=int(input("Enter the BMI Index : "))
        if(Index<=18):
            print("Under Weight")
            message="Under Weight"
        elif(Index<=24.9):
            print("Normal Range")
            message="Normal Range"
        elif(Index<=29.9):
            print("Over Weight")
            message="Over Weight"
        elif(Index<=34.9):
            print("Very Over Weight")
            message="Very Over Weight"
        else:
            print("Extreme Obase")
            message="Extreme Obase"
        return message
    def Subfields():
        print("Subfields in AI are:")
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech processing","Natural Language Processing"]
        for temp in lists:
            print(temp)
        return temp