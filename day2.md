# PYTHON

## SOAL UNIT 2

### 1. Berikut adalah tipe data dalam Python, KECUALI:

- Semua adalah tipe data
- **Lists**
- **Tuples**
- **Dictionaries**

**Jawaban**: Semua adalah tipe data

**Penjelasan**: Dalam Python, tipe data yang sering digunakan adalah `List`, `Tuple`, dan `Dictionary`. Oleh karena itu, pilihan "Semua adalah tipe data" adalah jawaban yang salah.

---

### 2. Pernyataan berikut benar mengenai komentar di Python, KECUALI:

- Setiap komentar dimulai dengan simbol `#` untuk menunjukkan bahwa itu adalah komentar
- Komentar ada untuk membuat kode lebih mudah dibaca dan dipahami
- Komentar diperlukan agar kode dapat berjalan dengan benar
- Komentar tidak akan pernah dieksekusi

**Jawaban**: Komentar diperlukan agar kode dapat berjalan dengan benar

**Penjelasan**: Komentar hanya digunakan untuk membantu programmer memahami kode; mereka tidak dieksekusi dan tidak diperlukan agar kode dapat berfungsi.

---

### 3. Metode Python mana yang mengambil input dari pengguna?

- `enter()`
- `prompt()`
- **input()**
- `print()`

**Jawaban**: `input()`

**Penjelasan**: Di Python, `input()` digunakan untuk menerima masukan dari pengguna. Metode ini menampilkan prompt di layar dan mengembalikan nilai yang dimasukkan pengguna.

---

### 4. Jika `x = 11` dan `y = 3`, berapa nilai `z` jika `z = x % y`?

- **2**
- 3
- 1
- 18

**Jawaban**: 2

**Penjelasan**: Operator `%` adalah operator modulus, yang memberikan sisa pembagian dari dua angka. Di sini, `11 % 3` menghasilkan sisa 2.

---

### 5. Untuk apa metode `print()` digunakan dalam Python?

- Semua benar
- Mengirim sesuatu ke printer
- Menghapus nilai dari variabel
- **Menampilkan sesuatu ke layar**

**Jawaban**: Menampilkan sesuatu ke layar

**Penjelasan**: Fungsi `print()` di Python digunakan untuk menampilkan output ke layar, bukan untuk mencetak ke printer atau membersihkan variabel.


## SOAL UNIT 3

### 1. Dalam pemrograman, keputusan perlu diambil.

- Mungkin
- **Benar**
- Salah

**Jawaban**: Benar

**Penjelasan**: Dalam pemrograman, sering kali diperlukan pengambilan keputusan untuk menentukan alur logika, seperti menggunakan pernyataan `if` untuk melakukan tindakan berdasarkan kondisi tertentu.

---

### 2. Pernyataan kondisi dalam Python dievaluasi menjadi __________________________.

- Ya atau Ya
- Ya atau Tidak
- stop atau continue
- **Benar atau Salah**

**Jawaban**: Benar atau Salah

**Penjelasan**: Pernyataan kondisi dalam Python dievaluasi menjadi `True` (Benar) atau `False` (Salah), yang kemudian menentukan apakah blok kode tertentu dijalankan.

---

### 3. Ketika Anda perlu memeriksa suatu kondisi berulang kali hingga kondisi itu terpenuhi, jenis loop apa yang harus Anda gunakan?

- for loop
- **while loop**
- do loop
- until loop

**Jawaban**: while loop

**Penjelasan**: `while` loop digunakan untuk mengulangi blok kode selama kondisi yang diberikan bernilai `True`. Loop ini akan terus berjalan hingga kondisi tersebut bernilai `False`.

---

### 4. Berapakah nilai dari ekspresi kondisional berikut?
```python
if 'Go' == 'go' or 4 > 1
```

- Gogo
- **True**
- None
- False

**Jawaban**: True

**Penjelasan**: Kondisi pertama `'Go' == 'go'` bernilai `False`, tetapi kondisi kedua `4 > 1` bernilai `True`. Karena operator `or` digunakan, cukup satu kondisi yang benar untuk menghasilkan `True`.

---

### 5. Berapa banyak iterasi yang dimiliki loop berikut?
```python
for num in range(7):
```

- 8
- 6
- random
- **7**

**Jawaban**: 7

**Penjelasan**: Fungsi `range(7)` menghasilkan angka dari 0 hingga 6, yang berarti loop ini akan dijalankan sebanyak 7 kali (untuk setiap angka dari 0 sampai 6).

Here is the Markdown version of these study notes, with answers and explanations in Indonesian.

---


## SOAL UNIT 4

### 1. Berapa banyak parameter yang dapat diterima oleh sebuah metode?

- **Minimal satu**
- Satu atau lebih
- Nol atau lebih
- Maksimal lima

**Jawaban**: Nol atau lebih

**Penjelasan**: Sebuah metode di Python dapat menerima nol atau lebih parameter. Parameter yang diberikan pada definisi metode dapat bersifat opsional (dengan nilai default) atau wajib.

---

### 2. Apa yang dilakukan pernyataan `global car` ketika digunakan di dalam sebuah metode?

- Ini membuat variabel `car` yang dapat digunakan di setiap skrip Python.
- Tidak ada yang spesial, hanya cara lain untuk mendeklarasikan sebuah variabel.
- **Ini membuat variabel global `car` tersedia untuk dimodifikasi di dalam metode.**
- Ini membuat variabel `car` dengan tipe khusus `global`.

**Jawaban**: Ini membuat variabel global `car` tersedia untuk dimodifikasi di dalam metode.

**Penjelasan**: Dengan menggunakan kata kunci `global`, variabel `car` yang didefinisikan di luar fungsi/metode dapat diubah di dalam fungsi tersebut. Tanpa `global`, perubahan hanya akan berlaku di dalam ruang lingkup lokal fungsi.

---

### 3. Sebuah metode didefinisikan sebagai `get_value(a, b, c=3)`. Mana dari panggilan fungsi berikut yang salah?

- `get_value(5, 4)`
- `get_value(4, 5, 3)`
- **`get_value(3)`**
- Tidak ada yang salah

**Jawaban**: `get_value(3)`

**Penjelasan**: Fungsi `get_value` memerlukan dua parameter wajib (`a` dan `b`), dan `c` memiliki nilai default 3. Panggilan `get_value(3)` hanya menyediakan satu parameter, yang tidak cukup untuk memenuhi dua parameter wajib (`a` dan `b`).

---

### 4. Mana yang benar tentang variabel yang didefinisikan dalam metode?

- **Mereka tidak dapat digunakan di luar metode.**
- Mereka tersedia untuk sesaat setelah metode dipanggil.
- Mereka hanya tersedia dalam skrip yang memanggil metode tersebut.
- Mereka tersedia di mana saja, bahkan di skrip lain.

**Jawaban**: Mereka tidak dapat digunakan di luar metode.

**Penjelasan**: Variabel yang didefinisikan di dalam metode adalah variabel lokal dan hanya dapat diakses dalam lingkup metode tersebut. Setelah metode selesai dieksekusi, variabel tersebut tidak lagi ada.

---

### 5. Bagaimana cara memanggil metode `go_home()`?

- `!go_home()`
- call `go_home()`
- **`go_home()`**
- `go_home()!`

**Jawaban**: `go_home()`

**Penjelasan**: Di Python, metode dipanggil dengan menggunakan nama metode diikuti dengan tanda kurung, misalnya `go_home()`. Tidak ada tanda seru (`!`) atau kata kunci `call` yang diperlukan.

Here is the Markdown version of these study notes, with answers and explanations in Indonesian.

---

## SOAL UNIT 5

### 1. Anda ingin mendefinisikan sebuah kelas Python bernama `Manager`, apa dua kata pertama yang harus Anda tulis?

- `def Manager`
- `define Manager`
- `Manager class`
- **`class Manager`**

**Jawaban**: `class Manager`

**Penjelasan**: Untuk mendefinisikan kelas di Python, gunakan kata kunci `class` diikuti oleh nama kelas, seperti `class Manager:`.

---

### 2. Dalam Pemrograman Berorientasi Objek (OOP), objek terdiri dari apa dan apa?

- **Atribut dan metode**
- Atribut dan kelas
- Kelas dan metode
- Metode dan fungsi

**Jawaban**: Atribut dan metode

**Penjelasan**: Dalam OOP, objek terdiri dari atribut (data) dan metode (fungsi) yang digunakan untuk bekerja dengan data tersebut. Kelas mendefinisikan struktur umum dari objek-objek tersebut.

---

### 3. Sebuah instance dari kelas dibuat menggunakan ___________________ dari kelas tersebut.

- instantiator
- properties
- **constructor**
- initiator

**Jawaban**: constructor

**Penjelasan**: Di Python, `constructor` adalah metode khusus `__init__()` dalam kelas yang secara otomatis dipanggil ketika sebuah instance baru dari kelas dibuat.

---

### 4. Metode dalam kelas dapat mengubah variabel apa pun dalam kelas.

- **True**
- False

**Jawaban**: True

**Penjelasan**: Metode dalam kelas dapat mengubah nilai dari variabel (atribut) yang didefinisikan di dalam kelas, selama variabel tersebut memiliki cakupan akses yang memungkinkan modifikasi.

---

### 5. Jika `john` adalah instance dari kelas `Manager`, dan `pay_salaries()` adalah metode instance dari kelas `Manager`, bagaimana Anda bisa memanggil metode `pay_salaries()`?

- `Manager.john.pay_salaries()`
- **`john.pay_salaries()`**
- `john.Manager.pay_salaries()`
- `pay_salaries()`

**Jawaban**: `john.pay_salaries()`

**Penjelasan**: Untuk memanggil metode instance pada objek, gunakan sintaks `instance.method()`. Karena `john` adalah instance dari kelas `Manager`, Anda cukup menulis `john.pay_salaries()` untuk memanggil metode `pay_salaries()`.
