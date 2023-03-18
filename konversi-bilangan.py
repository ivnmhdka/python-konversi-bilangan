from os import replace, system

def menu():
    print('Program Konversi Bilangan')
    print('1. Desimal')
    print('2. Biner')
    print('3. Oktal')
    print('4. Hexadecimal')
    print('5. String to ASCII')
    print('6. Exit')
    choose = input('Pilih Menu : ')
    if choose == '1':
        desimal()
    elif choose == '2':
        biner()
    elif choose == '3':
        oktal()
    elif choose == '4':
        hexadecimal()
    elif choose == '5':
        string_to_ascii()
    elif choose == '6':
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
    asking()

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
    asking()

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
    asking()

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
    asking()
    
def string_to_ascii():
    try:
        string = input("Masukkan huruf: ")
        ascii_list = [ord(char) for char in string]
        print("ASCII code:", ascii_list)
    except:
        print("Terjadi kesalahan saat memproses input.")

def asking():
    ask = input('Ingin mengonversi bilangan lain? ( y / t ) :')
    if ask == "y" or ask == "Y":
        menu()
    elif ask == "t" or ask == "T":
        exit()
    else:
        answrong()
        
def answrong():
    ask = input('Mohon pilih y/Y untuk pergi ke menu dan pilih t/T untuk keluar :')
    if ask == "y" or ask == "Y":
        menu()
    elif ask == "t" or ask == "T":
        exit()
    else:
        answrong()
      
menu()