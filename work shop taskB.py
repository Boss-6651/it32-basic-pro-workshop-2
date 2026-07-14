Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Height = int(input("Enter your height: "))
power = int(input("Enter your power: "))
Starter_Pack_Dolollar = int(input("Enter your money: "))

if Age > 18 and Height > 175 and power > 7 and Starter_Pack_Dolollar > 10000000:
    print("ผ่านในตำแหน่งผู้สืบทอดผลมังกร")
elif Age > 18 and 170 < Height < 175 and power < 7 and Starter_Pack_Dolollar < 10000:
    print("ผ่านตำแหน่งนักดาบอันดับ4")
elif Age < 18:
    print("อด")
else:
    print("ไม่รับไม่ชอบ")