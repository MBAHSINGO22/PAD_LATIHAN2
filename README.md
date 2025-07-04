# PAD_LATIHAN2

Repositori ini berisi latihan pemrograman Python untuk memenuhi tugas pada mata kuliah **Pemrograman Aplikasi Dasar (PAD)**. Terdapat dua latihan utama dalam bentuk file Python:

## 📁 Struktur File

```
PAD_LATIHAN2/
├── no1.py
├── no2.py
└── README.md
```

---

## 📌 Deskripsi Program

### 🔹 no1.py – Bilangan Ganjil Kelipatan 3

Program ini meminta input sebuah bilangan bulat dari pengguna, lalu mencetak semua bilangan **ganjil yang merupakan kelipatan 3** dari 3 hingga bilangan tersebut.

#### Cara Kerja:
- Program menerima input dari user.
- Menggunakan perulangan `for` dengan langkah 3.
- Menyimpan bilangan dalam list, kemudian menampilkannya.

#### Contoh Output:
```
Masukkan bilangan: 20
Bilangan ganjil berkelipatan 3 dari 20 adalah:
3 6 9 12 15 18 
```

---

### 🔹 no2.py – Grafik Harga Kue Nastar dan Putri Salju

Program ini menggunakan **Matplotlib dan NumPy** untuk menggambarkan grafik hubungan antara **jumlah penjualan (dalam toples)** dan **harga (dalam Rupiah)** untuk dua jenis kue: **Nastar** dan **Putri Salju**.

#### Fitur:
- Fungsi harga `P = f(Q)`:
  - Nastar: `P = 1000 × Q + 40000`
  - Putri Salju: `P = -333.33 × Q + 50000`
- Menampilkan grafik interaktif dengan label, grid, dan legenda.

#### Visualisasi:
- Grafik menunjukkan bagaimana harga berubah terhadap jumlah toples yang terjual.
- Membantu membandingkan strategi harga dari kedua jenis kue.

---

## ✅ Ketergantungan

Untuk menjalankan program `no2.py`, pastikan telah menginstal pustaka berikut:

```bash
pip install matplotlib numpy
```

---

## 👨‍💻 Author

- GitHub: [MBAHSINGO22](https://github.com/MBAHSINGO22)

---

## 📝 Lisensi

Repositori ini bebas digunakan untuk keperluan belajar dan akademik. Jika digunakan untuk publikasi, mohon cantumkan sumbernya.