class AI_Python_A6():
    def Subfields():
        print("Subfields in AI are:")
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech processing","Natural Language Processing"]
        for temp in lists:
            print(temp)
        return temp
    def OddEven():
        num=int(input("Enterthe Number:"))
        if((num%2)==0):
            print(num,"is Even Number")
            message='num'"is a Even Number"
        else:
            print(num,"is Odd Number")
            message='num'"is a Odd Number"
        return message
    def Eligible():
        Gen=input("Enter your Gender:")
        Age=int(input("Enter Your Age:"))
        if(Age>=21):
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        return message
    def percentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total=",Total)
        percentage=((sub1+sub2+sub3+sub4+sub5)/(5.0))
        print("Percentage=",percentage,"%")
        return percentage
    def triangle():
        height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area=(height*Breadth)/2
        print("Area =(height*Breadth)/2")
        print("Area of Triangle:",Area)
        Side1=int(input("Slanding_Height1:"))
        Side2=int(input("Slanding_Height2:"))
        Side3=int(input("Breadth:"))
        perimeter=Side1+Side2+Side3
        print("perimeter=Slanding_Height1+Slanding_Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)