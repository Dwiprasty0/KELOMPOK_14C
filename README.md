# KELOMPOK_14C
# **Sistem Pengelolaan Barang Donasi** 
## Anggota Kelompok : 
- Putri Nailah Azalia Priyambodo (I0324097)
- Cut Adra Rizkina (I0324113)
- Dwi Prastyo (I0324114)
- Restu Dewi Andinia (I0324135)

## Deskripsi
Program ini adalah aplikasi berbasis GUI (Graphical User Interface) yang digunakan untuk mengelola barang donasi. Program ini memungkinkan pengguna untuk menambahkan data barang donasi, melihat data yang telah tersimpan, dan mengedit status distribusi barang. Data barang disimpan dalam file CSV agar mudah diakses dan dimodifikasi.

---

## Fitur Utama
1. **Input Data Barang**:
   - Menambahkan data barang seperti kategori, jenis barang, kondisi barang, lokasi penyimpanan, nama donatur, dan status distribusi.
   - ID barang dihasilkan secara otomatis berdasarkan kategori.

2. **Lihat Data Barang**:
   - Menampilkan daftar barang yang telah dimasukkan.
   - Filter data berdasarkan kategori barang.

3. **Edit Data Barang**:
   - Mengubah status distribusi barang berdasarkan ID barang.

---

## Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python
- **Perpustakaan**:
  - `tkinter`: Untuk membangun antarmuka pengguna.
  - `pillow`: Untuk mengimport gambar.
  - `os`: Untuk mengecek keberadaan file CSV.

---

## Panduan Penggunaan
### **1. Halaman Utama**
-Berisi 3 Menu yang Dapat Dipilih (Input Data, Lihat Data, Edit Data)
### **1. Input Data**
- Pilih kategori barang dari dropdown.
- Masukkan informasi barang seperti jenis barang, kondisi, lokasi penyimpanan, nama donatur, dan status distribusi.
- Klik tombol **Tambah Barang** untuk menyimpan data.

### **2. Lihat Data**
- Gunakan filter kategori untuk memfilter daftar barang (opsional).
- Klik tombol **Tampilkan Data** untuk melihat data yang tersimpan.

### **3. Edit Data**
- Masukkan ID barang yang ingin diubah.
- Pilih kategori yang akan diedit
- Masukkan Nilai Baru Sesuai Kategori yang Dipilih
- Klik tombol **Update Data** untuk menginput data baru yang telah dimasukkan sebelumnya

---

## Struktur Data CSV
File CSV (`donasi.csv`) digunakan untuk menyimpan data barang dengan struktur berikut:
- **ID**: ID unik untuk setiap barang.
- **Kategori**: Kategori barang (Pakaian, Makanan, Elektronik, Alat Tulis).
- **Jenis Barang**: Deskripsi jenis barang.
- **Kondisi Barang**: Kondisi barang (Baru, Bekas, Layak Pakai).
- **Lokasi Penyimpanan**: Lokasi penyimpanan barang (Gudang A, Gudang B).
- **Nama Donatur**: Nama pemberi donasi.
- **Status Distribusi**: Status distribusi barang (Tersedia, Disalurkan)

.![Diagram Tanpa Judul drawio](https://github.com/user-attachments/assets/b77778df-95e3-441f-9054-94a6638dad68)




<img width="683" alt="site map" src="https://github.com/user-attachments/assets/9e5e8eb1-08d4-4289-82e4-74ecf8842dba">
