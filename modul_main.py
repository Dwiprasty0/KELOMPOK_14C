import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import modul_ui as ui
import modul_csv as csv_mod
from PIL import Image, ImageTk

# Inisialisasi root window
root = tk.Tk()
root.title("Sistem Pengelolaan Barang Donasi")
root.geometry("1000x600")

# Memastikan CSV ada
csv_mod.initialize_csv()
csv_mod.validate_csv_header()

# Frame Halaman Utama
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Menambahkan canvas untuk background
bg_canvas = tk.Canvas(main_frame)
bg_canvas.place(relwidth=1, relheight=1)

# Memuat gambar latar belakang
bg_image = Image.open("ever_kind.png")
bg_image = bg_image.resize((1366, 768))
bg_photo = ImageTk.PhotoImage(bg_image)

# Menampilkan gambar pada canvas
bg_canvas.create_image(0, 0, anchor="nw", image=bg_photo)
bg_canvas.image = bg_photo

# Menambahkan binding untuk memperbarui background saat ukuran jendela berubah
root.bind("<Configure>", lambda event: ui.update_background(event, bg_image, bg_canvas))

# Menambahkan tombol-tombol
tk.Button(main_frame, text="Input Data", command=lambda: ui.show_page(root, input_frame, [main_frame, input_frame, view_frame, edit_frame]), font=("Arial", 14)).place(relx=0.200, rely=0.75, width=150, height=50)
tk.Button(main_frame, text="Lihat Data", command=lambda: ui.show_page(root, view_frame, [main_frame, input_frame, view_frame, edit_frame]), font=("Arial", 14)).place(relx=0.700, rely=0.75, width=150, height=50)

# Frame Halaman Input Data
input_frame = tk.Frame(root)

kategori_var = tk.StringVar()
kondisi_barang_var = tk.StringVar()
lokasi_penyimpanan_var = tk.StringVar()
tanggal_masuk_var = tk.StringVar()
jumlah_var = tk.StringVar()
satuan_var = tk.StringVar()
status_distribusi_var = tk.StringVar()
nama_donatur_entry = tk.StringVar()

tk.Label(input_frame, text="Kategori:").grid(row=0, column=0, pady=8, padx=8, sticky="w")
kategori_combo = ttk.Combobox(input_frame, textvariable=kategori_var, values=["Pakaian", "Makanan", "Elektronik", "Alat Tulis"])
kategori_combo.grid(row=0, column=1, pady=8, padx=8)

jenis_barang_entry = ttk.Entry(input_frame)
tk.Label(input_frame, text="Jenis Barang:").grid(row=1, column=0, pady=8, padx=8, sticky="w")
jenis_barang_entry.grid(row=1, column=1, pady=8, padx=8)

tk.Label(input_frame, text="Kondisi Barang:").grid(row=2, column=0, pady=8, padx=8, sticky="w")
kondisi_combo = ttk.Combobox(input_frame, textvariable=kondisi_barang_var, values=["Baru", "Bekas", "Layak Pakai"])
kondisi_combo.grid(row=2, column=1, pady=8, padx=8)

tk.Label(input_frame, text="Lokasi Penyimpanan:").grid(row=3, column=0, pady=8, padx=8, sticky="w")
lokasi_combo = ttk.Combobox(input_frame, textvariable=lokasi_penyimpanan_var, values=["Gudang A", "Gudang B"])
lokasi_combo.grid(row=3, column=1, pady=8, padx=8)

nama_donatur_entry = ttk.Entry(input_frame)
tk.Label(input_frame, text="Nama Donatur:").grid(row=4, column=0, pady=8, padx=8, sticky="w")
nama_donatur_entry.grid(row=4, column=1, pady=8, padx=8)

tk.Label(input_frame, text="Status Distribusi:").grid(row=5, column=0, pady=8, padx=8, sticky="w")
status_combo = ttk.Combobox(input_frame, textvariable=status_distribusi_var, values=["Tersedia"])
status_combo.grid(row=5, column=1, pady=8, padx=8)

tk.Label(input_frame, text="Tanggal Masuk:").grid(row=6, column=0, pady=8, padx=8, sticky="w")
tanggal_masuk_entry = DateEntry(input_frame, textvariable=tanggal_masuk_var, date_pattern="dd/mm/yyyy")
tanggal_masuk_entry.grid(row=6, column=1, pady=8, padx=8)

tk.Label(input_frame, text="Jumlah:").grid(row=7, column=0, pady=8, padx=8, sticky="w")
kuantitas_entry = ttk.Entry(input_frame, textvariable=jumlah_var)
kuantitas_entry.grid(row=7, column=1, pady=8, padx=8)

tk.Label(input_frame, text="Satuan:").grid(row=8, column=0, pady=8, padx=8, sticky="w")
satuan_combo = ttk.Combobox(input_frame, textvariable=satuan_var, values=["Pcs", "Kg", "Lusin", "Kardus", "Karung"])
satuan_combo.grid(row=8, column=1, pady=8, padx=8)

tk.Button(input_frame, text="Tambah Barang", command=lambda: ui.add_data_ui(kategori_var, jenis_barang_entry, kondisi_barang_var, lokasi_penyimpanan_var, tanggal_masuk_var, jumlah_var, satuan_var, nama_donatur_entry, status_distribusi_var)).grid(row=10, column=0, columnspan=2, pady=10)
tk.Button(input_frame, text="Kembali", command=lambda: ui.show_page(root, main_frame, [main_frame, input_frame, view_frame, edit_frame])).place(relx=0.850, rely=0.900, width=80, height=30)

# Frame Halaman Lihat Data
view_frame = tk.Frame(root)

tree = ttk.Treeview(view_frame, columns=("ID", "Kategori", "Jenis Barang", "Kondisi Barang", "Lokasi Penyimpanan", "Tanggal Masuk", "Jumlah", "Satuan", "Nama Donatur", "Status Distribusi"), show="headings")
for col in ["ID", "Kategori", "Jenis Barang", "Kondisi Barang", "Lokasi Penyimpanan", "Tanggal Masuk", "Jumlah", "Satuan", "Nama Donatur", "Status Distribusi"]:
    tree.heading(col, text=col)
    tree.column(col, width=137)

tree_scroll = ttk.Scrollbar(view_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.grid(row=1, column=2, sticky="ns", pady=10)

tree.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

tk.Button(view_frame, text="Tampilkan Data", command=lambda: ui.view_data_ui(tree, kategori_filter_var)).grid(row=2, column=0, pady=10, padx=10)

tk.Button(view_frame, text="Edit Data", command=lambda: ui.edit_data_from_view(tree, root, edit_frame, edit_id_entry, field_combo, edit_value_var)).grid(row=2, column=1, pady=10, padx=10)

tk.Button(view_frame, text="Kembali", command=lambda: ui.show_page(root, main_frame, [main_frame, input_frame, view_frame, edit_frame])).grid(row=3, column=0, columnspan=2, pady=10)

kategori_filter_var = tk.StringVar()
kategori_filter_combo = ttk.Combobox(view_frame, textvariable=kategori_filter_var, values=["Semua Data", "Pakaian", "Makanan", "Elektronik", "Alat Tulis"])
kategori_filter_combo.grid(row=0, column=0, pady=10, padx=10)

# Fungsi untuk memperbarui input berdasarkan kategori yang dipilih
def update_edit_field_input(event):
    selected_field = edit_field_var.get()

    # Menghapus input sebelumnya
    for widget in edit_value_frame.winfo_children():
        widget.destroy()

    if selected_field == "Kategori":
        field_combo = ttk.Combobox(edit_value_frame, textvariable=edit_value_var, values=["Pakaian", "Makanan", "Elektronik", "Alat Tulis"])
        field_combo.pack(padx=5, pady=5)
    elif selected_field == "Kondisi Barang":
        field_combo = ttk.Combobox(edit_value_frame, textvariable=edit_value_var, values=["Baru", "Bekas", "Layak"])
        field_combo.pack(padx=5, pady=5)
    elif selected_field == "Lokasi Penyimpanan":
        field_combo = ttk.Combobox(edit_value_frame, textvariable=edit_value_var, values=["Gudang A", "Gudang B"])
        field_combo.pack(padx=5, pady=5)
    elif selected_field == "Status Distribusi":
        field_combo = ttk.Combobox(edit_value_frame, textvariable=edit_value_var, values=["Tersedia", "Disalurkan"])
        field_combo.pack(padx=5, pady=5)
    else:
        # Untuk field lainnya, gunakan entry
        entry_field = ttk.Entry(edit_value_frame, textvariable=edit_value_var)
        entry_field.pack(padx=5, pady=5)

# Frame Halaman Edit Data
edit_frame = tk.Frame(root)

edit_id_entry = ttk.Entry(edit_frame)
edit_field_var = tk.StringVar()
edit_value_var = tk.StringVar()

tk.Label(edit_frame, text="Masukkan ID Barang:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
edit_id_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(edit_frame, text="Pilih Field untuk Diedit:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
field_combo = ttk.Combobox(edit_frame, textvariable=edit_field_var, values=[ "Kondisi Barang", "Lokasi Penyimpanan", "Status Distribusi"])
field_combo.grid(row=1, column=1, pady=5, padx=5)

tk.Label(edit_frame, text="Pilih Field untuk Diedit:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
field_combo = ttk.Combobox(edit_frame, textvariable=edit_field_var, values=[ "Kondisi Barang", "Lokasi Penyimpanan", "Status Distribusi"])
field_combo.grid(row=1, column=1, pady=5, padx=5)
field_combo.bind("<<ComboboxSelected>>", update_edit_field_input)

edit_value_frame = tk.Frame(edit_frame)
edit_value_frame.grid(row=2, column=0, columnspan=2)

tk.Button(edit_frame, text="Update Data", command=lambda: ui.edit_data_ui(edit_id_entry, edit_field_var, edit_value_var)).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(edit_frame, text="Kembali", command=lambda: ui.show_page(root, main_frame, [main_frame, input_frame, view_frame, edit_frame])).place(relx=0.850, rely=0.900, width=80, height=30)


# Menampilkan Halaman Utama
ui.show_page(root, main_frame, [main_frame, input_frame, view_frame, edit_frame])

root.mainloop()
