# DAY 3 RANGKUMAN STUDY NOTES BASCORRO INTERNSHIP

8 November 2024
https://app.theconstruct.ai/courses/

## C++ for Robotics

### UNIT 1 C++ Basics

Berikut adalah README lengkap dengan semua opsi jawaban, jawaban benar, dan penjelasan dalam Bahasa Indonesia:

---

#### C++ Quiz

**Passing Score:** 100%

Jawablah pertanyaan-pertanyaan berikut ini untuk menguji pemahamanmu tentang dasar-dasar pemrograman C++.

##### Soal dan Jawaban

###### 1. Ekspresi mana di bawah ini yang menghasilkan string `Hello World!` jika:

```cpp
string h = "Hello";
char[1] e = "!";
char[5] w = "World";
string s = " ";
```

**Pilihan:**

- `h * s * w * eh + w + s + eh + e + w + sh + s + w + e`

**Jawaban Benar:** Tidak ada jawaban yang diberikan yang menghasilkan "Hello World!" dengan benar. Dalam C++, operator `*` tidak digunakan untuk menggabungkan string atau karakter. Biasanya, untuk menggabungkan string, kita menggunakan operator `+` seperti berikut:

```cpp
string result = h + s + w + e;
```

Ini akan menghasilkan string `"Hello World!"`.

###### 2. Apakah kamu harus mengkompilasi ulang kode C++ setiap kali ada perubahan karena C++ adalah bahasa yang dikompilasi?

- **False**
- **True**

**Jawaban Benar:** True  
 **Penjelasan:** C++ adalah bahasa yang dikompilasi, yang berarti kode sumber harus dikompilasi menjadi kode mesin agar bisa dijalankan. Setiap kali ada perubahan pada kode, kita harus mengkompilasi ulang untuk menghasilkan program yang diperbarui.

###### 3. Misalkan kamu memiliki beberapa data berikut:

```cpp
{1: "One", 2: "Two", 3: "Three"}
```

Bagaimana cara mendeklarasikan variabel untuk menyimpan data ini?

- `map<int,string> some_data;`
- `map<sting,int> some_data;`
- `list<int,string> some_data;`
- `list<int,string> some_data;`

**Jawaban Benar:** `map<int,string> some_data;`  
 **Penjelasan:** Data di atas memiliki format `key-value` di mana kunci adalah integer (`int`) dan nilai adalah string (`string`). Struktur data yang sesuai untuk menyimpan data seperti ini di C++ adalah `map<int, string>`. Struktur data `map` menyimpan pasangan `key-value` dan mendukung pencarian cepat berdasarkan kunci.

###### 4. Ketika kamu mengkompilasi kode sumber C++, misalnya `quiz.cpp`, apa nama file output yang benar?

- `quiz.exe`
- `quiz_compiled.exe`
- `quiz_exec`
- `quiz_exec.cpp`

**Jawaban Benar:** `quiz.exe`  
 **Penjelasan:** Pada sistem operasi Windows, file hasil kompilasi biasanya memiliki ekstensi `.exe`, seperti `quiz.exe`. Pada sistem operasi lain seperti Linux, file output biasanya tidak memiliki ekstensi (contohnya hanya `quiz`).

###### 5. Apa kata kunci C++ untuk menyertakan kode sumber dari sumber lain?

- `#ref`
- `#import`
- `#include`
- `import`

**Jawaban Benar:** `#include`  
 **Penjelasan:** Di C++, `#include` adalah kata kunci yang digunakan untuk memasukkan file header atau pustaka lain ke dalam kode kita. Ini memungkinkan kita untuk menggunakan fungsi dan kelas yang didefinisikan di file lain.

### UNIT 2 Conditional Statements and Loops

### UNIT 3 Functions

#### QUIZ

###### Soal 1

**Identify the line where we have errors in the function below:**

```cpp
int sum_it(int a, int b) {
    int sum = a + b;
    return sum;
}

float res = sum_it(5, 4.5);
```

- **Jawaban yang benar:** `the float res = sum_it(5, 4.5); line`

**Penjelasan:** Di C++, fungsi `sum_it` menerima dua parameter bertipe `int`. Namun, ketika kita memanggil `sum_it(5, 4.5);`, kita mencoba memasukkan `4.5`, yang bertipe `float`. Hal ini menyebabkan kesalahan karena tipe parameter yang tidak cocok.

---

###### Soal 2

**What would be the output of the following code snippet?**

```cpp
void change_var() {
    string varr = "This is your new value!";
}
change_var();
cout << varr;
```

- **Jawaban yang benar:** `An error`

**Penjelasan:** Variabel `varr` dideklarasikan di dalam fungsi `change_var`, sehingga memiliki _scope_ lokal dalam fungsi tersebut. Saat kita mencoba mencetak `varr` di luar fungsi, C++ tidak mengenali variabel tersebut, sehingga terjadi kesalahan.

---

###### Soal 3

**In C++ functions, the return statement is mandatory.**

- **Jawaban yang benar:** `False`

**Penjelasan:** Dalam C++, fungsi yang bertipe `void` tidak memerlukan _return statement_, meskipun fungsi dengan tipe pengembalian (misalnya `int`, `float`) memang biasanya membutuhkan _return statement_.

---

###### Soal 4

**Without the use of functions there will be so much repeated code.**

- **Jawaban yang benar:** `True`

**Penjelasan:** Fungsi membantu kita menghindari pengulangan kode dengan memungkinkan kita menulis satu kali dan memanggilnya di tempat yang diperlukan. Ini juga mempermudah pemeliharaan kode.

---

###### Soal 5

**Suppose you have the function defined below. How do you call it?**

```cpp
void say_what() {
  cout << "What!" << endl;
}
```

- **Jawaban yang benar:** `say_what()`

**Penjelasan:** Fungsi `say_what` dipanggil dengan menggunakan nama fungsi diikuti oleh tanda kurung `()` tanpa argumen, sesuai dengan definisinya.
