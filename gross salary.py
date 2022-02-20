bp=float(input("Enter your basic pay")) 

N=input("Enter your name") 

HRA=bp*15/100
TA=bp*10/100
DA=bp*12/100
EPF=bp*18/100

GS=bp+HRA+TA+DA-EPF

print("Total HRA = ",HRA)
print("Gross Salary = ",GS)
