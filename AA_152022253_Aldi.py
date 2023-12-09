import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1: Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for index in df.index:
    df.at[index, 'Gaji'] *= 1.05

# Pertanyaan 2: Tampilkan DataFrame setelah peningkatan gaji 5%.
print("DataFrame setelah peningkatan gaji 5%:")
print(df)

# Pertanyaan 3: Mengubah tipe data kolom 'Gaji' menjadi float
df['Gaji'] = df['Gaji'].astype(float)

# Fungsi lambda untuk menghitung naik gaji
hitung_gaji_baru = lambda usia, gaji: gaji * 1.07 if usia > 30 else gaji * 1.05

# Membuat kolom baru 'GajiBaru' dengan nilai yang sudah diperbarui
df['GajiBaru'] = df.apply(lambda row: hitung_gaji_baru(row['Usia'], row['Gaji']), axis=1)

# Pertanyaan 4: Tampilkan DataFrame dengan kolom 'GajiBaru'
print("\nDataFrame setelah peningkatan tambahan:")
print(df[['Nama', 'Usia', 'Gaji', 'GajiBaru']])

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:
# - Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# - Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# - Tampilkan hasil dan ringkasan dengan jelas.
# - Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.



