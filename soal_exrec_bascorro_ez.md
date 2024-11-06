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
