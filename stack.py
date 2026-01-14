from collections import deque
import random

stack = deque()

def tampilkan_stack():
    print("Isi Stack:", list(stack))

while True:
    print("\n=== MENU STACK ===")
    print("1. Append (Tambah Kanan)")
    print("2. AppendLeft (Tambah Kiri)")
    print("3. Pop (Hapus Kanan)")
    print("4. PopLeft (Hapus Kiri)")
    print("5. Clear")
    print("6. Generate & Acak List 1-10")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ").strip()

    if pilihan == "1":
        data = input("Masukkan data: ")
        stack.append(data)
        tampilkan_stack()

    elif pilihan == "2":
        data = input("Masukkan data: ")
        stack.appendleft(data)
        tampilkan_stack()

    elif pilihan == "3":
        if stack:
            stack.pop()
        else:
            print("Stack kosong")
        tampilkan_stack()

    elif pilihan == "4":
        if stack:
            stack.popleft()
        else:
            print("Stack kosong")
        tampilkan_stack()

    elif pilihan == "5":
        stack.clear()
        print("Stack dikosongkan")

    elif pilihan == "6":
        angka = list(range(1,2,3,4,5,6,7,8,9,10))  
        random.shuffle(angka)
        stack.append(angka)
        print("List angka 1–10 berhasil diacak dan dimasukkan ke stack")
        tampilkan_stack()

    elif pilihan == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-7")
