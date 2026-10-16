#1
'''
num1=int(input("input the first number:"))
num2=int(input("input the second number:"))
if a>b:
    print("the greater number is",num1)
elif b>a:
    print("the greater number is",num2)
else:
    print("numbers are equal")'''
#2
'''
number=int(input("input the number:"))
if number > 0:
    print(number,"- is positive")
elif number < 0:
    print(number,"- is negative")
else:
    print(number ,"- is equal 0")'''
#3
'''
number=int(input("input the number:"))
if number % 2 == 0:
    print(number,"is even")
else:
    print(number,"is odd")'''
#4
'''number = int(input("input the number:"))
if 91<=number<=100:
    print("A")
elif 81<=number<=90:
    print("B")
elif 71<=number<=80:
    print("C")
elif 61<=number<=70:
    print("D")
elif 51<=number<=60:
    print("E")
elif 0<=number<=50:
    print("F")
else:
    print("Invalid score")'''
#5
'''number1=int(input("input the first number :"))
number2=int(input("input the second number :"))
number3=int(input("input the third number :"))
if number1>number2 and number1>number3:
    print("the largest number is",number1)
elif  number2>number1 and number2>number3:
    print("the largest number is",number2)
else:
    print("the largest number is",number3)
'''
#6
'''
number1 = float(input("input the first number: "))
number2 = float(input("input the second number: "))
symbol = input("input an operation symbol: ")

if symbol == "+":
    print("The result of addition is", number1 + number2)
elif symbol == "-":
    print("The result of subtraction is", number1 - number2)
elif symbol == "*":
    print("The result of multiplication is", number1 * number2)
elif symbol == "**":
    if number1 == 0 and number2 < 0:
        print("Error: Zero cannot be raised to a negative power!")
    elif number1 < 0 and (number2 != int(number2)):
        print("Error: A negative base cannot be raised to a non-integer power!")
    else:
        print("The result of exponentiation operator is", number1 ** number2)
elif symbol == "/":
    if number2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print("The result of division is", number1 / number2)
elif symbol == "%":
    if number2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print("The result of division with remainder is", number1 % number2)
elif symbol == "//":
    if number2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print("The result of integer division is", number1 // number2)
else:
    print("Invalid operation")
    '''
#7
'''
age=int(input("input your age:"))
if age>=0:
    if 0<=age<=12:
        print("you are a child")
    elif 13<=age<=17:
        print("you are a teenager")
    elif 18<=age<=64:
        print("you are an adult")
    else:
        print("you are a senior")
else:
    print("Invalid age")'''
#8
'''
amount=float(input("input the purchase amount:"))
if amount >=0 :
    if amount<100:
        print("You have no discount.","The original price is",amount,"azn","The final price is",amount,"azn")
    elif 100<=amount<300:
        print("The original price is ",amount,"azn","Your discount amount is","10%","The final price is",(amount*90)/100,"azn")
    elif 300<=amount<500:
            print("The original price is ",amount,"azn","Your discount amount is","15%","The final price is",(amount*85)/100,"azn")
    else:
           print("The original price is ",amount,"azn","Your discount amount is","20%","The final price is",(amount*80)/100,"azn")
else:
    print("Invalid error")'''
#9
'''
a=int(input("input the first number:"))
b=int(input("input the second number:"))
c=int(input("input the third number:"))
if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>a and b>c:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
else:
    if a>b:
        print(b,a,c)
    else:
        print(a,b,c)
        '''
#10
'''
wamount=float(input("input the withdrawal amount:"))
if wamount<=0:
    print("Invalid amount")
elif wamount>1000:
    print("Insufficient balance") 
else:
    print("The remaining balance is",1000-wamount)
    '''
#11
'''
elecusage=float(input("input the electricity usage in kWh:"))
if elecusage < 0:
    print("Negative usage is invalid")
elif elecusage in(0,100):
    print("The usage is",elecusage,"The applied rate is","0.08 AZN/kWh","The total bill is",elecusage*0.08,"AZN")
elif 100<elecusage<=300:
    print("The usage is",elecusage,"The applied rate is","0.12 AZN/kWh","The total bill is",elecusage*0.12,"AZN")
else:
    print("The usage is",elecusage,"The applied rate is","0.15 AZN/kWh","The total bill is",elecusage*0.15,"AZN")
'''
#12
'''
distance=float(input("Input the distance of the travel:"))
if distance<0:
    print("Negative distance is invalid")
elif 0<=distance<=5:
    print("starting fee is 2 AZN","distance fee is 0.70 AZN/km","total fee is", distance*0.7+2 ,"AZN")
elif 5<distance<=15:
    print("starting fee is 2 AZN","distance fee is 0.60 AZN/km","total fee is", distance*0.6+2 ,"AZN")
else:
    print("starting fee is 2 AZN","distance fee is 0.50 AZN/km","total fee is", distance*0.5+2 ,"AZN")
'''
#13
'''
age=int(input("input your age:"))
monthlysalary=int(input("input your salary:"))
loan=int(input("input the amount of the loan:"))
if age > 0 and monthlysalary > 0 and loan >0:
    if age < 18:
        print("Decision rejected") 
        print("Reason: Age below 18")
    elif monthlysalary < 500:
        print("Decision rejected")
        print("Reason: Salary below 500 AZN")
    elif loan > 10*monthlysalary:
        print("Decision rejected")
        print("Reason: Loan above 10 times the salary")
    else:
        print("Approved")
else:
    print("Invalid input")
'''
#14
'''
a=int(input("input the first side of the triangle:"))
b=int(input("input the second side of the triangle:"))
c=int(input("input the third side of the triangle:"))
if a>0 and b>0 and c>0:
    if a+b>c:
        if a+c>b:
            if b+c>a:
                if a==b and b==c :
                    print("Equalateral")
                elif a==b or a==c or b==c:
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Triangle cannot be created")
        else:
            print("Triangle cannot be created")
    else:
        print("triangle cannot be created")
else:
    print("All lengths must be positive")
'''
#15
'''
examscore=int(input("Input the exam score of yours :"))
schoolscore=int(input("Input the school score of yours :"))
age=int(input("Input the age of yours :"))
if examscore > 0 :
    if   schoolscore >= 0 :
        if age >= 0:
            if examscore<=700 :
                if schoolscore<=100:
                    if age < 16:
                        if 600<=examscore<=700:
                            print("Result: Scholarship")
                            print("Reason: The excellent exam score is between 600 and 700")
                        elif 450<=examscore<=599:
                            print("Result: Accepted")
                            print("Reason: Exam score is between 450 and 599")
                        elif 300<=examscore<449:
                            if schoolscore>=80:
                                print("Result: Accepted")
                                print("Reason: The exam score is between 300 and 449 ,and the school score is at least 80")
                            else:
                                print("Result: Rejected")
                                print("Reason: The exam score is between 300 and 400, however the school score is below 80")
                        else:
                            print("Result: Rejected")
                            print("Reason: The exam score is below 300")
                    else:
                        print("Result: Rejected")
                        print("Reason: Applicant must be younger than 16 years old")
                else:
                    print("Result: Rejected / Invalid input")
                    print("Reason: The school score is above 100")
            else:
                print("Result: Rejected / Invalid input")
                print("Reason: The exam score is above 700")
        else:
            print("Result: Rejected / Invalid input")
            print("Reason: The age is below 0")
    else:
        print("Result: Rejected / Invalid input")
        print("Reason: The school score is below 0")
else:
    print("Result: Rejected / Invalid input")
    print("Reason: The exam score is below 0")
'''
#16
'''
examscore=int(input("Input the exam score: "))
if examscore < 0 or examscore > 100 :
    print("Error: Score must be between 0 and 100.")
else:
    Result = "Pass" if examscore >= 51 else "Fail"
    print(Result)
'''
#17
'''
total = float(input("Input the order total with AZN: "))
member = input("Input the membership answer: ")

if total < 0:
    print("Invalid order total")
elif member not in ("yes", "no"):
    print("Invalid membership answer")
else:
    delivery_fee = 0 if (total >= 50 or member == "yes") else 5
    final_total = total + delivery_fee

    print("Delivery fee:", delivery_fee, "AZN")
    print("Final total:", final_total, "AZN")
'''
#18
'''
day = int(input("Input the day number: "))

match day:
    case 1:
        print("Monday")
        print("Study day")
    case 2:
        print("Tuesday")
        print("Study day")
    case 3:
        print("Wednesday")
        print("Study day")
    case 4:
        print("Thursday")
        print("Study day")
    case 5:
        print("Friday")
        print("Study day")
    case 6:
        print("Saturday")
        print("Study day")
    case 7:
        print("Sunday")
        print("Study day")
    case _:
        print("Invalid day")
'''
#19
'''
code = input("input the first letter of the drink you want: ")
quantity = int(input("input the quantity of the drink you want: "))

if quantity < 1 or quantity > 10:
    print("Invalid quantity")
else:
    match code:
        case "t":
            drink = "Tea"
            price = 2
        case "c":
            drink = "Coffee"
            price = 4
        case "j":
            drink = "Juice"
            price = 3
        case _:
            print("Invalid drink code")
            exit()

    total = price * quantity
    order_type = "Large order" if total >= 20 else "Regular order"

    print("Drink:", drink)
    print("Quantity:", quantity)
    print("Total:", total, "AZN")
    print(order_type)
'''
#20
'''
SID=input("Input the ID of yours: ")
if len(SID) != 8 and SID.icdecimal() == False:
    print("Invalid")
else:
    print("Student ID accepted")
'''
#21
'''
storedpin = "0427"
PIN=input("Input the PIN: ")
if len(PIN) != 4:
    print("PIN must have 4 digits")
elif PIN.isdigit() == False:
    print("Digits only")
elif PIN == storedpin:
    print("Access granted")
else:
    print("Incorrect PIN")
'''
#22
'''
phone_number=input("Enter local phone number: ")
if not phone_number:
    print("Empty input is invalid")
elif len(phone_number)!=10:
    print("Phone number must be exactly 10 character")
elif not phone_number.isdgit():
    print("Spaces, letters, +, hyphens, and brackets are not allowed")
elif not phone_number.startswith('0'):
    print("Must be begin with 0")
else:
    match phone_number[:3]:
        case "050" | "051" | "055" | "070" | "077" | "099" :
            print("Phone number accepted")
        case _:
            print("Invalid format")
'''
#23
'''
balance = 1000
storedpin = "0427"

inpin = input("Input student PIN: ")
inbalance = input("Input withdrawal balance: ")

if not (len(inpin) == 4 and inpin.isdigit() and inpin.isascii()):
    print("Invalid PIN format")

elif inpin != storedpin:
    print("Invalid PIN")

elif not (inbalance != "" and inbalance.isdigit() and inbalance.isascii()):
    print("Invalid amount format")

else:
    amount = int(inbalance)

    if amount < 10 or amount > 500:
        print("Amount out of range")

    elif amount % 10 != 0:
        print("Amount must be divisible by 10")

    else:
        fee = 0 if amount <= 200 else 2

        if amount + fee > balance:
            print("Insufficient funds")
        elif amount + fee <= balance:
            new_balance = balance - amount - fee
            print("Withdrawal:", amount)
            print("Fee:", fee)
            print("New balance:", new_balance)
        else:
            print("Transaction error")
'''
#24
'''
product_code = input("Input the product code: ")
quantity_str = input("Input the quantity: ")
coupon_code = input("Input the coupon code: ")
delivery_code = input("Input the delivery code: ")

match product_code:
    case "K":
        product = "Keyboard"
        price = 40
    case "M":
        product = "Mouse"
        price = 20
    case "H":
        product = "Headphones"
        price = 60
    case _:
        print("Invalid product code")
        exit()

if quantity_str == "" or not quantity_str.isascii() or not quantity_str.isdigit():
    print("Invalid quantity format")
    exit()

quantity = int(quantity_str)

if quantity < 1 or quantity > 5:
    print("Quantity out of range")
    exit()

if coupon_code not in ("NONE", "SAVE10"):
    print("Invalid coupon code")
    exit()

subtotal = price * quantity
if coupon_code == "SAVE10" and subtotal < 100:
    print("Coupon not eligible")
    exit()

discount = subtotal * 0.10 if coupon_code == "SAVE10" else 0
discounted_subtotal = subtotal - discount

match delivery_code:
    case "P":
        delivery_fee = 0
    case "S":
        delivery_fee = 0 if discounted_subtotal >= 80 else 5
    case _:
        print("Invalid delivery code")
        exit()

final_total = discounted_subtotal + delivery_fee

print("Product:", product)
print("Quantity:", quantity)
print("Subtotal:", subtotal, "AZN")
print("Discount:", discount, "AZN")
print("Delivery fee:", delivery_fee, "AZN")
print("Final total:", final_total, "AZN")'''
