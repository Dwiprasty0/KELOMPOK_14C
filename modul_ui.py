import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import modul_csv as csv_mod

# Fungsi untuk navigasi ke halaman tertentu
def show_page(root, page, frames):
    for frame in frames:
        frame.pack_forget()
    page.pack(fill="both", expand=True)

# Fungsi untuk memperbarui gambar latar belakang sesuai dengan ukuran window
def update_background(event, bg_image, bg_canvas):
    new_width = event.width
    new_height = event.height

    # Resize gambar latar belakang sesuai ukuran window
    bg_image_resized = bg_image.resize((new_width, new_height))  # Menyesuaikan dengan ukuran baru
    bg_photo_resized = ImageTk.PhotoImage(bg_image_resized)

    # Update gambar latar belakang pada canvas
    bg_canvas.create_image(0, 0, anchor="nw", image=bg_photo_resized)
    bg_canvas.image = bg_photo_resized  # Simpan referensi gambar

def add_data_ui(kategori_var, kategori_combo, jenis_barang_entry, kondisi_barang_var, lokasi_penyimpanan_var, nama_donatur_entry, status_distribusi_var):
    kategori = kategori_var.get()
    jenis_barang = jenis_barang_entry.get()
    kondisi_barang = kondisi_barang_var.get()
    lokasi_penyimpanan = lokasi_penyimpanan_var.get()
    nama_donatur = nama_donatur_entry.get()
    status_distribusi = status_distribusi_var.get()

    if not (kategori and jenis_barang and kondisi_barang and lokasi_penyimpanan and nama_donatur):
        messagebox.showwarning("Input Error", "Harap isi semua field dengan benar!")
        return

    # Mendapatkan ID barang yang akan datang secara berurutan
    existing_items = csv_mod.view_data(kategori)  # Ambil data barang yang sudah ada
    next_item_id = len(existing_items) + 1  # ID berikutnya adalah jumlah barang + 1

    # Generate ID baru berdasarkan kategori dan urutan barang, dengan format dua huruf kategori + tiga digit angka
    id_barang = f"{kategori[:2].upper()}{next_item_id:03}"  # Format ID: Kode kategori + urutan barang dalam kategori

    
    # Menambahkan data ke CSV
    csv_mod.add_data(id_barang, kategori, jenis_barang, kondisi_barang, lokasi_penyimpanan, nama_donatur, status_distribusi)

    messagebox.showinfo("Sukses", f"Barang berhasil ditambahkan dengan ID: {id_barang}")
    kategori_var.set("")
    jenis_barang_entry.delete(0, tk.END)
    kondisi_barang_var.set("")
    lokasi_penyimpanan_var.set("")
    nama_donatur_entry.delete(0, tk.END)
    status_distribusi_var.set("")


# Fungsi untuk melihat data barang
def view_data_ui(tree, kategori_filter_var):
    for row in tree.get_children():
        tree.delete(row)

    selected_kategori = kategori_filter_var.get()
    data = csv_mod.view_data(selected_kategori)
    
    for item in data:
        tree.insert("", tk.END, values=(item["ID"], item["Kategori"], item["Jenis Barang"], item["Kondisi Barang"], item["Lokasi Penyimpanan"], item["Nama Donatur"], item["Status Distribusi"]))

# Fungsi untuk memperbarui data barang
def edit_data_ui(edit_id_entry, edit_field_var, edit_value_var):
    item_id = edit_id_entry.get()
    selected_field = edit_field_var.get()
    new_value = edit_value_var.get()

    if not new_value:
        messagebox.showerror("Input Error", "Harap masukkan nilai baru.")
        return

    updated = csv_mod.edit_data(item_id, selected_field, new_value)

    if updated:
        messagebox.showinfo("Sukses", "Data berhasil diperbarui!")
    else:
        messagebox.showwarning("Error", "ID Barang tidak ditemukan!")
        
