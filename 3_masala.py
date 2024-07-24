import os

def check_file(papkani_manzili, fayl_nomi):
    fayl_manzili = os.path.join(papkani_manzili, fayl_nomi)
    if os.path.exists(fayl_manzili):
        print(f"{fayl_nomi} fayl ko'rsatilgan papkada mavjud.")
    else:
        print(f"{fayl_nomi} fayl ko'rsatilgan papkada mavjud emas.")

