
import os
i = 1
while i <= 10:
    file_name = f"file_{i}.txt"
    with open(file_name, "w") as file:
        file.write("Bu fayl {}-chi fayl".format(i))
    i += 1
print("10 ta fayl muvaffaqiyatli yaratildi.")
