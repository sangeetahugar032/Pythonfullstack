distance = float(input("Enter delivery distance in km: "))
if distance <=5:
    print("Local")
elif distance <= 20:
    print("City")
else:
    print("Outstation")
