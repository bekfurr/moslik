import tkinter as tk
from tkinter import messagebox

def qidirish():
    a = list(map(str, entry_massiv.get().split()))
    b = list(map(str, entry_qidirilayotgan_object.get().split()))
    hisobchi_index = []
    hisobchi = 0

    for i in range(len(a)):
        if a[i] in b:
            hisobchi_index.append(i)
            hisobchi += 1

    if hisobchi > 0:
        indices_message = ", ".join(map(str, hisobchi_index))
        messagebox.showinfo("Natija", f"Bir xil elementlar topildi! Indekslar: {indices_message}\nBir xil elementlar soni: {hisobchi}")
    else:
        messagebox.showinfo("Natija", "Bir xil element topilmadi")

root = tk.Tk()
root.title("Matnlarni Mosligini Tekshirish")
root.geometry("300x200")

label_massiv = tk.Label(root, text="Birinchi matnni kiriting (probel bilan ajratib):")
label_massiv.pack()

entry_massiv = tk.Entry(root, width=65)
entry_massiv.pack()

label_qidirilayotgan_object = tk.Label(root, text="Ikkinchi matnni kiriting:")
label_qidirilayotgan_object.pack()

entry_qidirilayotgan_object = tk.Entry(root, width=65)
entry_qidirilayotgan_object.pack()

button_qidirish = tk.Button(root, text="Tekshirish", command=qidirish)
button_qidirish.pack(pady=10)

root.mainloop()
