#import library yang digunakan
import socket
import random

HOST = 'IP ADDRESS'     # IP address perangkat yang terhubung ke jaringan (IP address yang terhubung ke jaringan)
PORT = 'PORT'           # Port yang digunakan untuk koneksi (dalam bentuk angka bebas, yang penting sama dengan port client)

# Membuat fungsi permainan tebak angka
def permainan(connect):
    angka = random.randint(1, 51)   # Membangkitkan angka acak antara 1 dan 51
    maksimum_tebakan = 5            # Jumlah maksimum tebakan yang diperbolehkan
    nomor_tebakan = 0               # Jumlah tebakan yang sudah dilakukan
    tebakan_benar = False           # Status apakah tebakan sudah benar atau belum

    teks_petunjuk = 'Masukkan tebakan ke {}:'
    while not tebakan_benar and not nomor_tebakan >= maksimum_tebakan:
        nomor_tebakan += 1
        tebakan = connect.recv(1024).decode()   # Menerima tebakan dari client
        print(teks_petunjuk.format(nomor_tebakan), tebakan)
        tebakan = int(tebakan)
        if tebakan == angka:
            print('Tebakan benar')
            tebakan_benar = True
            connect.send('Tebakan benar'.encode())   # Mengirimkan pesan tebakan benar ke client
        elif tebakan > angka:
            print('Tebakan terlalu besar')
            connect.send('Tebakan terlalu besar'.encode())   # Mengirimkan pesan tebakan terlalu besar ke client
        else:
            print('Tebakan terlalu kecil')
            connect.send('Tebakan terlalu kecil'.encode())   # Mengirimkan pesan tebakan terlalu kecil ke client

    if tebakan_benar:
        #print('Selamat! Anda berhasil menebak angka')
        connect.send('Selamat! Anda berhasil menebak angka'.encode())   # Mengirimkan pesan berhasil menebak ke client
    else:
        #print('Kesempatan menebak anda habis, anda kalah.')
        #print('Angka yang benar adalah', angka)
        connect.send('Kesempatan menebak anda habis, anda kalah.\n'.encode())   # Mengirimkan pesan habis kesempatan menebak ke client
        connect.send(('Angka yang benar adalah ' + str(angka)+ '\n').encode())   # Mengirimkan angka yang benar ke client
    connect.send(str(tebakan_benar).encode())
    result = nilai(nomor_tebakan)
    connect.send(result.encode())   # Mengirimkan nilai ke client

# Membuat fungsi nilai sesuai kondisi tebakan keberapa
def nilai(nomor_tebakan):
    if nomor_tebakan == 0:
        a = 'Nilai kamu -> 100'
        return a
    elif nomor_tebakan == 1:
        b = 'Nilai kamu -> 90'
        return b
    elif nomor_tebakan == 2:
        c = 'Nilai kamu -> 80'
        return c
    elif nomor_tebakan == 3:
        d = 'Nilai kamu -> 70'
        return d
    elif nomor_tebakan == 4:
        e = 'Nilai kamu -> 60'
        return e
    else :
        nol = 'Kamu belum berhasil mendapatkan nilai'
        return nol

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Membuat objek socket
server.bind((HOST, PORT))                                    # Mengikat host dan port
server.listen(5)
print('Menunggu terhubung ke client...')                     # Akan tampil di layar server sebelum client terhubung

while True:
    connect, address = server.accept()   # Menerima koneksi dari client
    print('Terhubung dengan', address)
    connect.send("!!!SELAMAT DATANG DI PERMAINAN TEBAK ANGKA!!!".encode())   # Mengirimkan pesan selamat datang ke client

    permainan(connect)   # Memulai permainan

    connect.close()   # Menutup koneksi dengan client