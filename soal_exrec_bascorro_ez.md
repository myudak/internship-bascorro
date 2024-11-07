# PROJECT LIVE CODING EWS BASCORRO

## Teknis pelaksanaan:

1. Peserta bersiap di ruangan 5 menit sebelum melaksanakan project.
2. Peserta diberikan soal pemrograman sesuai dengan pembagian kelompok.
3. Peserta diberi waktu 45 menit untuk menyelesaikan kode pemrograman.
4. Peserta diberi waktu 5 menit untuk melakukan presentasi dari kode pemrograman yang telah diselesaikan.
5. Peserta diberi waktu 10 menit untuk menyelesaikan tantangan yang diberikan oleh penilai.
6. Hasil kode pemrograman dikumpulkan kepada penilai.

## Ketentuan:

1. Peserta membawa laptop masing-masing.
2. Peserta dibebaskan menggunakan Code Editor apapun untuk menyelesaikan pemrograman.
3. Peserta menggunakan bahasa Python atau C++ untuk menyelesaikan pemrograman.
4. Peserta diperbolehkan menggunakan tools AI (Artificial Intelligence) dalam menyelesaikan project.
5. Peserta dilarang menggunakan tools AI (Artificial Intelligence) dalam menyelesaikan tantangan.
6. Peserta dilarang bekerja sama dengan peserta lainnya.
7. Kode pemrograman dibuat saat tahap pelaksanaan bukan dipersiapkan dari rumah/kos.

# 1. Soal Pemrograman: Permainan Tebak Angka

## Deskripsi Soal

Buatlah sebuah program di mana pengguna diminta untuk menebak angka yang dipilih secara acak oleh program. Program akan memberikan petunjuk apakah tebakan pengguna terlalu tinggi atau terlalu rendah hingga pengguna menebak angka yang benar. Angka acak yang dihasilkan akan berada dalam rentang 1 hingga 100.

### Catatan

- Program harus berhenti setelah pengguna berhasil menebak angka yang benar.
- Setiap tebakan akan mendapatkan petunjuk “terlalu tinggi” atau “terlalu rendah” jika angka tebakan tidak sesuai.
- Gunakan fungsi acak bawaan untuk menghasilkan angka.

## Penjelasan Input

- Program tidak menerima input sebelum dimulai.
- Setiap kali pengguna memberikan tebakan, program menerima input berupa angka integer dari 1 hingga 100.

## Penjelasan Output

- Untuk setiap tebakan yang salah, program akan menampilkan petunjuk:
  - "Terlalu tinggi" jika tebakan lebih besar dari angka acak.
  - "Terlalu rendah" jika tebakan lebih kecil dari angka acak.
- Setelah tebakan benar, program akan menampilkan pesan:
  - "Selamat! Anda menebak dengan benar."

### Contoh

#### Input

50

75

63

68

#### Output

Terlalu rendah

Terlalu tinggi

Terlalu rendah

Selamat! Anda menebak dengan benar

## Jawaban Python

```python
import random

target_number = random.randint(1, 100)
tebakan = None

while tebakan != target_number:
    tebakan = int(input("Tebakan: "))

    if tebakan < target_number:
        print("Terlalu rendah")
    elif tebakan > target_number:
        print("Terlalu tinggi")
    else:
        print("Betul")
```

# 2. Soal Pemrograman: Generator Password Acak

## Deskripsi Soal

Buatlah sebuah program yang menghasilkan password acak dengan panjang tertentu sesuai permintaan pengguna. Password yang dihasilkan harus terdiri dari kombinasi huruf besar dan huruf kecil. Pengguna akan diminta untuk menentukan panjang password yang diinginkan sebelum password dihasilkan.

### Catatan

- Pastikan bahwa password yang dihasilkan selalu memiliki kombinasi dari huruf besar dan huruf kecil.

## Penjelasan Input

- Input pertama adalah angka integer yang mewakili panjang password yang diinginkan (minimal 6 karakter, maksimal 20 karakter).

## Penjelasan Output

- Program akan menampilkan sebuah password acak dengan panjang sesuai input pengguna, yang mengandung kombinasi huruf besar dan huruf kecil.

### Contoh

#### Input

```
12
```

#### Output

```
xAnHydIKkLoP
```

## Jawaban Python

```python
def password_generators(L):
    if L < 8 or L > 20:
        raise Exception("error")
    LIST_PASSWORD = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890"
    )

    HURUF_BESAR = random.choice(LIST_PASSWORD[:27])
    HURUF_KECIL = random.choice(LIST_PASSWORD[27:54])
    KARAKTER_SPESIAL = random.choice(LIST_PASSWORD[54:62])
    ANGKA = random.choice(LIST_PASSWORD[62:72])
    SISANYA = "".join(random.choice(LIST_PASSWORD) for _ in range(L - 4))

    password = list(HURUF_BESAR + HURUF_KECIL + KARAKTER_SPESIAL + ANGKA + SISANYA)
    random.shuffle(password)

    return "".join(password)
```

# 3. Soal Pemrograman: Sistem Pemesanan Kursi Bioskop

### Deskripsi Soal

Buatlah sebuah program yang menampilkan tata letak kursi bioskop dalam bentuk array 2 dimensi berukuran 4 baris x 7 kolom. Setiap elemen array merepresentasikan kursi yang belum dipesan dengan format "A1", "A2", dst. Pengguna dapat memesan kursi dengan memilih kode kursi, dan setelah dipesan, kursi tersebut akan ditandai sebagai "Booked". Program akan terus meminta input hingga pengguna selesai memesan kursi.

**Catatan:**

- Baris pertama diwakili oleh huruf **A**, baris kedua oleh **B**, baris ketiga oleh **C**, dan baris keempat oleh **D**.
- Program harus memvalidasi apakah kursi sudah dipesan sebelumnya. Jika sudah, berikan pesan bahwa kursi tersebut tidak tersedia.
- Pemesanan berakhir ketika pengguna memasukkan "selesai" sebagai input.

### Penjelasan Input

- Program menerima input berupa kode kursi seperti "A1", "B4", dsb., yang menunjukkan kursi yang dipesan.
- Pengguna bisa mengetik **"selesai"** untuk mengakhiri pemesanan.

### Penjelasan Output

- Setelah setiap pemesanan, program akan menampilkan array dengan tanda **"Booked"** di posisi kursi yang sudah dipesan.
- Jika kursi yang dimasukkan tidak valid atau sudah dipesan, program akan memberikan pesan kesalahan.

---

### Contoh Input

```
A1
B4
selesai
```

### Contoh Output

Sebelum pemesanan:

```
A1 A2 A3 A4 A5 A6 A7
B1 B2 B3 B4 B5 B6 B7
C1 C2 C3 C4 C5 C6 C7
D1 D2 D3 D4 D5 D6 D7
```

Setelah A1 dan B4 dipesan:

```
Booked A2 A3 A4 A5 A6 A7
B1 B2 B3 Booked B5 B6 B7
C1 C2 C3 C4 C5 C6 C7
D1 D2 D3 D4 D5 D6 D7
```
