print("ENTER THE MARKS OBTAINED IN 5 SUBJECTS!!!")

m1 = int(input())

m2 = int(input())

m3= int(input())

m4=int(input())

m5=int(input())

sum= m1 + m2 + m3+m4+m5
avg = sum/5

if avg>=91 and avg<=100:
    print("Congrats! Your grade is A1!")
elif avg>=81 and avg<91:
    print("Your grade is B1!")
elif avg>=61 and avg<71:
    print("Your grade is B2")
elif avg>=51 and avg<61:
    print("Your grade is C1!")
elif avg>=41 and avg<51:
    print("Your grade is C2!")
elif avg>=31 and avg<41:
    print("Your grade is D1!")
elif avg>=21 and avg<31:
    print("Your grade is D2!")
elif avg>=11 and avg<21:
    print("Your grade is E1!")
elif avg>=1 and avg<11:
    print("Your grade is B1!")
else:
    print("YOU HAVE AN INVALID INPUT")
#end
