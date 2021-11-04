# Sistem e-Library - Kelompok 06 - Kelas 01 Pengenalan Komputasi
# Nabila Vira Nandhita (16020311)
# Yogi Pamungkas (16020336)
# Felix Fernando (16020231)
# Medina Alifia Zahrani (16020391)

#Data username user
username_data = ["","","","","","","","","",""]

#Data password user
password_data = ["","","","","","","","","",""]

#Data untuk buku yang dipinjam user 
books_borrowed = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#Data buku yang tersedia dengan format ["judul buku", jumlah buku] (matriks 2 x N)
books = [["Purcell - Calculus 9th Edition", 3], 
        ["Halliday & Resnick - Fundamentals Of Physics 10th Edition", 2], 
        ["Brady - Chemistry 7th Edition", 4],
        ["Chang - Chemistry 10th Edition", 5],
        ["Giancoli - Physics Prcinciples with Applications 7th Edition", 5],
        ["Serway - Principle of Physics 4th Edition", 0],
        ["Riley - Mathematical Methods for Physics and Engineering", 1]]

#Fungsi untuk menampilkan start menu
def startMenu():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("            Selamat Datang di Sistem E-Library            ")
    print("==========================================================")
    print("---------------------- Pilihan Menu ----------------------")
    print("1. Login")
    print("2. Sign Up")
    print("3. Quit")
    #Menerima input dari user untuk navigasi ke menu lainnya
    start = int(input("Masukkan Pilihan Menu : "))
    print("==========================================================")
    print("")
    #Conditional untuk input yang dimasukkan oleh user
    if start == 1:
        #Navigasi ke menu login
        login()
    elif start == 2:
        #Navigasi ke menu login
        signUp()
    else:
        #Menghentikan program
        print("Terima kasih telah mengunjungi E-Library, Sampai Jumpa")
        print("==========================================================")
        return False

#Fungsi untuk cek login dari user
def login():
    global logged #Mendefinisikan variable global "logged" agar dapat diakses diluar fungsi login()
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                         Log-in                           ")
    print("==========================================================")
    print("------------- Masukkan username dan password -------------")
    #Menerima username dan password user
    username = str(input("Username : "))
    password = str(input("Password : "))
    #Kondisi jika username terdapat dalam database
    if username in username_data: 
        #Kondisi jika password yang dimasukkan benar
        if password == password_data[username_data.index(username)]: 
            #Mengubah nilai dari logged menjadi index user yang telah berhasil melakukan login
            logged = username_data.index(username) 
            #Tampilan pada console
            print("==========================================================")
            print("")
        #Kondisi jika password yang dimasukkan user salah
        else: 
            #Tampilan pada console
            print("username atau password anda salah.")
            print("==========================================================")
            print("")
            #Navigasi ke menu start
            startMenu()
    #Kondisi jika username tidak terdapat dalam database 
    else:
        #Tampilan pada console
        print("username atau password anda salah.")
        print("==========================================================")
        print("")
        #Navigasi ke menu start
        startMenu()

#Fungsi untuk membuat akun baru
def signUp():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                         Sign-up                          ")
    print("==========================================================")
    print("--- Masukkan username dan password yang akan digunakan ---")
    #Menerima input dari user berupa username dan password yang akan didaftarkan pada sistem
    username = str(input("Username : "))
    password = str(input("Password : "))
    #Kondisi jika username belum digunakan / belum terdapat dalam database
    if username not in username_data:
        for i in range(10):
            if username_data[i] == "":
                #Memasukkan data username dan password yang telah diinput ke dalam database
                username_data[i] = username
                #Memasukkan data username dan password yang telah diinput ke dalam database
                password_data[i] = password
                break
        #Tampilan pada console
        print("Akun anda sudah terdaftar")
    #Kondisi jika username telah digunakan / terdapat dalam database
    else: 
        #Tampilan pada console
        print("Username tersebut telah dipakai")
    print("==========================================================")
    print("")
    #Navigasi ke menu start
    startMenu()

#Fungsi untuk menampilkan menu apabila pengguan berhasil melakukan login
def loggedIn():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                         E-Library                        ")
    print("==========================================================")
    print("Selamat Datang %s di E-Library" %(username_data[logged]))
    print("---------------------- Pilihan Menu ----------------------")
    print("1. Buku yang telah dipinjam")
    print("2. Pengembalian Buku")
    print("3. Buku yang tersedia")
    print("4. Pinjam buku")
    print("5. Log out")
    #Menerima input dari user untuk navigasi ke menu lainnya
    logged_menu = int(input("Masukkan Pilihan Menu : "))
    #Tampilan pada console
    print("==========================================================")
    print("")
    #Conditional untuk input yang dimasukkan oleh user
    if logged_menu == 1:
        #Navigasi ke menu list buku yang telah dipinjam
        borrowed()
    elif logged_menu == 2:
        #Navigasi ke menu list buku yang telah dipinjam
        returnBook()
    elif logged_menu == 3:
        #Navigasi ke menu list buku yang tersedia
        bookList()
    elif logged_menu == 4:
        #Navigasi ke menu untuk meminjam buku
        borrow()
    elif logged_menu == 5:
        #Tampilan pada console
        print("Sampai Jumpa %s" %(username_data[logged]))
        print("==========================================================")
        print("")
        #sign out dari akun
        return False

#Fungsi menampilkan buku yang telah dipinjam user
def borrowed():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                 Buku yang sedang dipinjam                ")
    print("==========================================================")
    #Loop untuk menampilkan buku yang telah dipinjam oleh user
    for i in range(5):
        if books_borrowed[logged][i] != 0:
            print("%s. %s" %(i+1, books[books_borrowed[logged][i]-1][0]))
        else:
            print("%s. " %(i+1))
    #Input untuk kembali ke menu sebelumnya
    input("Tekan Enter untuk kembali ke menu awal")
    print("==========================================================")
    print("")

#Fungsi untuk mengembalikan buku yang telah dipinjam user
def returnBook():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                     Pengembalian buku                    ")
    print("==========================================================")
    #Loop untuk menampilkan buku yang telah dipinjam oleh user
    for i in range(5):
        if books_borrowed[logged][i] != 0:
            print("%s. %s" %(i+1, books[books_borrowed[logged][i]-1][0]))
        else:
            print("%s. " %(i+1))
    print("Ketik 0 untuk kembali ke menu awal")
    #Menerima input user berupa kode buku yang akan dikembalikan
    return_book = int(input("Masukkan No. Buku yang Ingin dikembalikan : "))
    #Kondisi jika user tidak mengembalikan buku
    if return_book == 0 or return_book > 5 or books_borrowed[logged][return_book-1] == 0:
        #Kembali ke menu sebelumnya
        print("==========================================================")
        print("")
        return
    #Kondisi jika user akan mengembalikan buku
    else:
        #Menambahkan kembali buku ke list buku yang tersedia
        books[books_borrowed[logged][return_book-1]-1][1] += 1
        #Menghapus buku dari database user
        books_borrowed[logged][return_book-1] = 0
    print("")

#Fungsi untuk buku yang telah dipinjamkan
def bookList():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                        List Buku                         ")
    print("==========================================================")
    #Loop untuk menampilkan buku yang tersedia
    for i in range(7):
        print("%s. %s, Buku yang tersedia : %s" %(i+1, books[i][0], books[i][1]))
    #Input untuk kembali ke menu sebelumnya
    input("Tekan Enter untuk kembali ke menu awal")
    print("==========================================================")
    print("")

#Fungsi untuk meminjam buku 
def borrow():
    #Tampilan pada console
    print("")
    print("==========================================================")
    print("                      Meminjam Buku                       ")
    print("==========================================================")
    #Loop untuk menampilkan buku yang tersedia
    for i in range(7):
        print("%s. %s, Buku yang tersedia : %s" %(i+1, books[i][0], books[i][1]))
    #Tampilan pada console
    print("Ketik 0 untuk kembali ke menu awal")
    print("==========================================================")
    #Menerima input user berupa kode buku yang akan dipinjam
    borrow_book = int(input("Masukkan kode buku yang ingin dipinjam : "))
    #Kondisi jika user tidak meminjam buku
    if borrow_book == 0 or borrow_book > 7:
        #Kembali ke menu sebelumnya
        return
    #Kondisi jika user meminjam buku
    else:
        #Kondisi jika buku masih tersedia, buku belum dipinjam oleh user tersebut dan user belum memenuhi batas jumlah peminjaman buku
        if books[borrow_book-1][1] != 0 and borrow_book not in books_borrowed[logged] and 0 in books_borrowed[logged]:
            books[borrow_book-1][1] -= 1
            for i in range(5):
                if books_borrowed[logged][i] == 0:
                    books_borrowed[logged][i] = borrow_book
                    break
            print("%s telah dimasukkan ke daftar buku yang anda pinjam" %(books[borrow_book-1][0]))
        #Kondisi jika buku yang ingin dipinjam tidak tersedia
        elif books[borrow_book-1][1] == 0:
            print("Buku tidak tersedia")
        #Kondisi jika buku sudah dipinjam oleh user
        elif borrow_book in books_borrowed[logged]:
            print("Buku sedang anda pinjam")
        else:
            print("Anda telah memenuhi batas jumlah peminjaman buku")
    print("")

#Main Loop
while True:
    if startMenu() == False:
        break
    else:
        while True:
            if loggedIn() == False:
                break
