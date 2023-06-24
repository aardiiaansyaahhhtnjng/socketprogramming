import socket

HOST = 'IP ADDRESS'     # IP address perangkat yang terhubung ke jaringan (IP address yang terhubung ke jaringan)
PORT = 'PORT'           # Port yang digunakan untuk koneksi (dalam bentuk angka bebas, yang penting sama dengan port server)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Menerima pesan selamat datang dari server
    pesan_selamat_datang = client.recv(1024).decode()
    print(pesan_selamat_datang)

    # Memulai permainan
    while True:
        tebakan = input("Tebakan: ")
        client.send(tebakan.encode())  # Mengirimkan tebakan ke server

        # Menerima status tebakan dari server
        tebakan_status = client.recv(1024).decode()
        print(tebakan_status)

        if 'Tebakan benar' in tebakan_status:
            break  # Jika tebakan benar, keluar dari perulangan
        elif 'Kesempatan menebak' in tebakan_status:
            pesan_angka = client.recv(1024).decode()
            print(pesan_angka, end='')

    # Menerima hasil pesan dari server
    pesan_hasil = client.recv(1024).decode()
    print(pesan_hasil)

    # Menerima nilai dari server
    nilai = client.recv(1024).decode()
    print(nilai)

    client.close()

if __name__ == '__main__':
    main()
