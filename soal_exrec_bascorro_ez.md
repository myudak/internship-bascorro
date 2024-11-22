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

```
50

75

63

68
```

#### Output

```
Terlalu rendah

Terlalu tinggi

Terlalu rendah

Selamat! Anda menebak dengan benar
```

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

# 4. Soal Pemrograman Sistem Antrian Penumpang di Bandara

### Deskripsi Soal

Buatlah sebuah program yang mensimulasikan sistem antrian penumpang pesawat berdasarkan nomor penerbangan. Setiap penumpang memiliki nomor penerbangan dan masuk ke dalam antrian sesuai urutan mereka datang. Ketika penumpang dipanggil, mereka akan dikeluarkan dari antrian. Program harus mampu:

- Menambahkan penumpang ke antrian.
- Mengeluarkan penumpang dari antrian ketika dipanggil.

#### Catatan:

- Nomor penerbangan berupa kode seperti "GA123", "SJ456", dsb.
- Pemanggilan penumpang dilakukan satu per satu berdasarkan urutan antrian.
- Program harus memungkinkan untuk terus menerima penumpang hingga ada perintah khusus untuk memanggil penumpang.

### Penjelasan Input

Input berupa dua jenis perintah:

1. **`Masuk [Nomor Penerbangan]`**: Menambahkan penumpang ke antrian.
2. **`Panggil`**: Memanggil penumpang yang berada di urutan pertama dalam antrian.
3. **`selesai`**: Mengakhiri program.

### Penjelasan Output

- Setelah penumpang ditambahkan ke antrian, program akan menampilkan daftar penumpang yang sedang mengantri berdasarkan nomor penerbangan.
- Setiap kali perintah **`Panggil`** diberikan, program akan menampilkan nomor penerbangan penumpang yang dipanggil dan memperbarui antrian.

---

### Contoh Input

```
Masuk GA123
Masuk SJ456
Masuk QZ789
Panggil
Masuk GA987
Panggil
selesai
```

### Contoh Output

```
Antrian saat ini: GA123, SJ456, QZ789
Penumpang dengan nomor penerbangan GA123 dipanggil.
Antrian saat ini: SJ456, QZ789
Penumpang dengan nomor penerbangan SJ456 dipanggil.
Antrian saat ini: QZ789, GA987
```

# 5. Soal Pemrograman Sistem Registrasi Masuk-Keluar Event

### Deskripsi Soal

Pada sebuah event, setiap peserta harus menggunakan ID card untuk masuk dan keluar dari venue melalui pintu masuk dan keluar. Sistem harus mencatat ID card mana saja yang sedang berada di dalam venue dan memperbarui daftar tersebut setiap kali ada aktivitas masuk atau keluar. Tidak diperlukan validasi khusus terkait penggunaan ulang ID card.

Tugas Anda adalah membuat sistem yang mencatat aktivitas masuk dan keluar, serta menampilkan daftar peserta yang sedang berada di dalam venue setiap kali ada aktivitas masuk atau keluar.

#### Catatan:

- ID card yang sudah keluar dari venue akan dihapus dari daftar peserta yang ada di dalam venue.
- Setiap kali ada aktivitas masuk atau keluar, tampilkan daftar ID card yang sedang berada di dalam venue.

---

### Penjelasan Input

1. **Baris pertama** berisi sebuah bilangan bulat **N** yang menyatakan jumlah aktivitas (masuk atau keluar) yang terjadi.
2. **Baris-baris berikutnya** berisi dua elemen:
   - **String ID card** yang digunakan.
   - **Karakter aktivitas** (`I` untuk "masuk" dan `O` untuk "keluar").

---

### Penjelasan Output

Untuk setiap aktivitas:

1. Cetak:
   - `"ID card <ID> berhasil masuk"` jika aktivitas masuk berhasil.
   - `"ID card <ID> berhasil keluar"` jika aktivitas keluar berhasil.
2. Setelah setiap aktivitas, cetak daftar ID card yang berada di dalam venue dalam format:
   - `"ID di dalam venue saat ini: <daftar ID>"` jika ada ID card yang berada di dalam.
   - `"ID di dalam venue saat ini: Tidak ada."` jika tidak ada peserta yang berada di dalam venue.

---

### Contoh Input

```

6
ID123 I
ID124 I
ID123 O
ID124 I
ID123 I
ID123 O

```

### Contoh Output

```

ID card ID123 berhasil masuk
ID di dalam venue saat ini: ID123
ID card ID124 berhasil masuk
ID di dalam venue saat ini: ID123 ID124
ID card ID123 berhasil keluar
ID di dalam venue saat ini: ID124
ID card ID124 berhasil keluar
ID di dalam venue saat ini: Tidak ada.
ID card ID123 berhasil masuk
ID di dalam venue saat ini: ID123
ID card ID123 berhasil keluar
ID di dalam venue saat ini: Tidak ada.

```

# Soal Pemrograman Pengelolaan Tempat Parkir

### Deskripsi Soal

Sebuah gedung parkir memiliki **3 lantai**, dan setiap lantai memiliki **25 slot parkir** yang diatur dalam format grid **5x5**. Anda diminta untuk membuat program untuk mengelola pengendalian tempat parkir. Program harus dapat:

1. Memasukkan kendaraan ke slot parkir yang dipilih secara manual oleh pengguna.
2. Mengeluarkan kendaraan dari slot parkir.
3. Menampilkan status tempat parkir di setiap lantai, menunjukkan apakah slot kosong atau sudah terisi.

#### Catatan:

- Sistem harus memberikan pesan peringatan jika pengguna mencoba memarkir kendaraan di slot yang sudah terisi atau memasukkan input yang tidak valid.
- Program harus mengelola **baris** dan **kolom** parkir dalam format grid 5x5.
- Pengguna dapat memilih **lantai (1-3)** serta koordinat **baris** dan **kolom** secara manual untuk setiap kendaraan yang datang.

---

### Penjelasan Input

Program akan menerima input berupa perintah:

1. **`Datang`**: Ketika kendaraan datang dan ingin diparkir. Setelah perintah ini:
   - Masukkan nomor kendaraan.
   - Pilih lantai (1-3).
   - Masukkan koordinat **baris** dan **kolom** yang dipisahkan dengan koma (contoh: `2,3`).
2. **`Keluar`**: Ketika kendaraan keluar. Setelah perintah ini, masukkan nomor kendaraan yang keluar.
3. **`Cek`**: Untuk menampilkan status semua slot parkir di gedung.

---

### Penjelasan Output

- **Untuk perintah `Datang`**:

  - Jika slot kosong, tampilkan pesan bahwa kendaraan berhasil diparkir beserta detail slotnya.
  - Jika slot sudah terisi, tampilkan pesan bahwa slot penuh.
  - Jika input koordinat tidak valid, tampilkan pesan kesalahan.

- **Untuk perintah `Keluar`**:

  - Tampilkan pesan bahwa kendaraan berhasil keluar dan slot telah dikosongkan.
  - Jika kendaraan tidak ditemukan, tampilkan pesan bahwa kendaraan tersebut tidak ada di parkir.

- **Untuk perintah `Cek`**:
  - Tampilkan status seluruh slot parkir di semua lantai dalam format grid, dengan keterangan:
    - `kosong` untuk slot yang tidak terisi.
    - Nomor kendaraan untuk slot yang terisi.

---

### Contoh Input dan Output

#### Contoh Input Datang

```
Masukkan perintah (Datang/Keluar/Cek): Datang
Masukkan nomor kendaraan: B1234XYZ
Pilih lantai (1-3): 1
Masukkan baris dan kolom (misal: 1,2): 2,3
```

#### Contoh Output Datang

```
Kendaraan B1234XYZ diparkir di Lantai 1 pada slot (2,3).
```

---

#### Contoh Input Cek

```
Masukkan perintah (Datang/Keluar/Cek): Cek
```

#### Contoh Output Cek

```
Status Lantai 1:
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  B1234XYZ kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong

Status Lantai 2:
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong

Status Lantai 3:
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
kosong  kosong  kosong  kosong  kosong
```
