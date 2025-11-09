
def bmical(weight,height):
    bmi=weight/(height**2)
    return bmi
def findcatagory(bmi):
    if bmi<18.5:
        return "under weight"
    elif 18.5<=bmi<=24.9:
        return "your weight is normal"
    elif 25<= bmi<=29 :
        return "overweight"
    else:
        return "obesity"
def main():
    print("hello! i can calculate your bmi:")
    try:
        weight=float(input("enter your weight in kg:"))
        heighta=float(input("enter your height in cm:"))
        height=heighta/100
        bmi=bmical(weight,height)
        catagory = findcatagory(bmi)
        print(f" your bmi is:{bmi:.2f} kg/m^2")
        print(f" your catagory:{catagory}")

    except ValueError:
        print("please enter vaild inputs")
 
if __name__== "__main__":
    main()
   
