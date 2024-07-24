
def tekshir(parol):
    with open("password.txt", "r") as fayl:
        haqiqiy_parol = fayl.read().strip()
    if parol == haqiqiy_parol:
        print("true!")
    else:
        print("false!")
foydalanuvchi_paroli = input("Parolni kiriting: ")
tekshir(foydalanuvchi_paroli)
