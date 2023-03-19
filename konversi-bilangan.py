from os import replace, system

def menu():
    print("=======================================")
    print('Program Konversi Bilangan'.center(40))
    print('=======================================')
    print('| 1. Desimal                          |')
    print('| 2. Biner                            |')
    print('| 3. Oktal                            |')
    print('| 4. Hexadecimal                      |')
    print('| 5. String to ASCII                  |')
    print('| 0. Exit                             |')
    print('=======================================')
    choice = input('Pilih Menu : ')
    if choice == '1':
        desimal()
    elif choice == '2':
        biner()
    elif choice == '3':
        oktal()
    elif choice == '4':
        hexadecimal()
    elif choice == '5':
        string_to_ascii()
    elif choice == '0':
        print("Terima kasih telah menggunakan program ini.")
        exit()
    else:
        wrong()

def wrong():
    wrong = input("Menu Tidak Ada! tekan [ENTER] untuk kembali")
    menu()

def desimal():
    print("Konversi Bilangan Desimal")
    try:
        angka = int(input("Masukkan Bilangan Desimal : "))
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        desimal()
    bineri = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")
    
    print('Biner : ',bineri)
    print('Oktal : ',oktal)
    print('Hexa  : ',heks)
    while True:
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            desimal()
            break
        elif kembali == "t" or kembali == "T":
            menu()
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 't'.")

def biner():
    print("Konversi Bilangan Biner")
    try:
        angka = int(input("Masukkan Bilangan Biner : "),2)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        biner()
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")

    print('| Decimal : ',angka)
    print('| Oktal   : ',oktal)
    print('| Hexa    : ',heks)
    while True:
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            biner()
            break
        elif kembali == "t" or kembali == "T":
            menu()
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 't'.")

def oktal():
    print("Konversi Bilangan Oktal")
    try:
        angka = int(input("Masukkan Bilangan Oktal : "),8)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        oktal()
    biner = bin(angka).replace("0b","")
    heks = hex(angka).replace("0x","")

    print('| Decimal : ',angka)
    print('| biner   : ',biner)
    print('| Hexa    : ',heks)
    while True:
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            oktal()
            break
        elif kembali == "t" or kembali == "T":
            menu()
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 't'.")

def hexadecimal():
    print("Konversi Bilangan Hexadecimal")
    try:
        angka = int(input("Masukkan Bilangan Hexa : "),16)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        hexadecimal()
    biner = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    
    print('| Decimal : ',angka)
    print('| Biner   : ',biner)
    print('| Oktal   : ',oktal)
    while True:
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            hexadecimal()
            break
        elif kembali == "t" or kembali == "T":
            menu()
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 't'.")

def string_to_ascii():
    try:
        string = input("Masukkan huruf: ")
        ascii_list = [ord(char) for char in string]
        print("ASCII code:", ascii_list)
    except:
        print("Terjadi kesalahan saat memproses input.")
    while True:
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            string_to_ascii()
            break
        elif kembali == "t" or kembali == "T":
            menu()
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 't'.")

menu()