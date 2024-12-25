import csv
import os

CSV_FILE = "donasi.csv"

# Fungsi untuk memastikan file CSV ada dengan header
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Kategori", "Jenis Barang", "Kondisi Barang", "Lokasi Penyimpanan", "Tanggal Masuk", "Jumlah", "Satuan", "Nama Donatur", "Status Distribusi"])

def validate_csv_header():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            expected_header = ["ID", "Kategori", "Jenis Barang", "Kondisi Barang", "Lokasi Penyimpanan", "Tanggal Masuk", "Jumlah", "Satuan", "Nama Donatur", "Status Distribusi"]
            if header != expected_header:
                print("Header CSV tidak sesuai. Memperbarui header...")
                data = list(reader)
                with open(CSV_FILE, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(expected_header)
                    writer.writerows(data)

# Fungsi untuk menambahkan data ke CSV
def add_data(id_barang, kategori, jenis_barang, kondisi_barang, lokasi_penyimpanan, tanggal_masuk, Jumlah, satuan, nama_donatur, status_distribusi):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id_barang, kategori, jenis_barang, kondisi_barang, lokasi_penyimpanan, tanggal_masuk, Jumlah, satuan, nama_donatur, status_distribusi])

# Fungsi untuk melihat data dari CSV sesuai kategori
def view_data(selected_kategori):
    data = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for item in reader:
                # Tambahkan nilai default jika kolom tidak ditemukan
                item.setdefault("Tanggal Masuk", "dd/mm/yyyy")
                item.setdefault("Jumlah", "0")
                if selected_kategori == "Semua Data" or item["Kategori"] == selected_kategori:
                    data.append(item)
    return data


# Fungsi untuk memperbarui data di file CSV
def edit_data(item_id, selected_field, new_value):
    updated = False
    data = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["ID"] == item_id:
                    row[selected_field] = new_value
                    updated = True
                data.append(row)

    if updated:
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Kategori", "Jenis Barang", "Kondisi Barang", "Lokasi Penyimpanan", "Nama Donatur", "Status Distribusi"])
            writer.writeheader()
            writer.writerows(data)
    return updated

