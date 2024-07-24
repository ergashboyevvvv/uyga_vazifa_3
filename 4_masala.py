import os

def delete_file(papkani_manzili, fayl_nomi):
    fayl_manzili = os.path.join(papkani_manzili, fayl_nomi)
    try:
        os.remove(fayl_manzili)
        print(f"{fayl_nomi} fayl muvaffaqiyatli o'chirildi.")
    except FileNotFoundError:
        print(f"{fayl_nomi} fayl topilmadi.")
    except PermissionError:
        print(f"Ruxsat berilmaganligi sababli {fayl_nomi} faylni o'chirib bo'lmadi.")
