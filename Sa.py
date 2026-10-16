'''grade=int(input("aldigin qiymeti daxil et:"))
if  91<=grade<=100:
    print("A")
elif 81<=grade<=90:
    print("B")
elif 71<=grade<=80:
    print("C")
elif 61<=grade<=70:
    print("D")
elif 51<=grade<=60:
    print("E")
elif 0<=grade<=50:
    print("F")
else:
    print("Invalid score")'''
'''
a=int(input("birinci 3reqemli ededi daxil et:"))
b=int(input("ikinci 3reqemli ededi daxil et:"))
c=int(input("ucuncu 3reqemli ededi daxil et:"))
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)''' 
'''
a=int(input("boyuk ededi daxil et"))
b=int(input("kicik ededi daxil et"))
c=input("operatoru daxil et")
if c == "+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c == "%":
    print(a%b)
elif c=="**":
    print(a**b)
elif c=="//":
    print(a//b)
else:
    print("Invalid operation")
    '''
'''
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
elif age >=65:
    print("Senior")
else:
    print("Invalid age")
    '''
'''
amount = float(input("Enter purchase amount: "))
if amount < 100:
    discount_percent = 0
elif amount < 300:
    discount_percent = 10
elif amount < 500:
    discount_percent = 15
else:
    discount_percent = 20
discount_amount = amount * (discount_percent / 100)
final_price = amount - discount_amount
print()
print("Original Price:", amount, "AZN")
print("Discount:", discount_percent, "%")
print("Discount Amount:", discount_amount, "AZN")
print("Final Price:", final_price, "AZN")'''