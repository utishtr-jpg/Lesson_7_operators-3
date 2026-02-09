print("Please enter a number for the numerator")
numn = int(input())
print("Enter a number for the denominator")
numd=int(input())

if numn%numd==0:
    print("\n" + str(numn) + " Is divisible by " +str(numd))
else: print("\n" + str(numn) + " Is not divisible by " +str(numd))