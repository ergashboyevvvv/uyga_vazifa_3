def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            data = source.read()
        with open(destination_file, 'w') as destination:
            destination.write(data)
        print(f"{source_file} fayli {destination_file} fayliga muvaffaqiyatli nusxalandi.")
    except FileNotFoundError:
        print(f"Fayl topilmadi: {source_file}")
    except PermissionError:
        print(f"Ruxsat berilmaganligi sababli faylni nusxalash muvaffaqiyatli amalga oshirilmadi.")
source_file = "sher.txt"
destination_file = "sher2.txt"
copy_file(source_file, destination_file)
