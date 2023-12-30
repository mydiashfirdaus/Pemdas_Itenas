import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

df['Gaji Bonus'] = [(lambda x: x * 1.05)(gaji) for gaji in df['Gaji']]

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nDataFrame Gaji setelah Bonus")
print(df[['Nama', 'Usia', 'Gaji', 'Gaji Bonus']])

print("\nRingkasan Gaji:")
for index, row in df.iterrows():
        print(f"{row['Nama']}: Gaji Awal {row['Gaji']:.1f}, Gaji setelah Bonus {row['Gaji Bonus']:.1f}, Peningkatan sebesar {row['Gaji Bonus'] - row['Gaji']:.1f}")

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

df['Gaji Tambahan usia > 30'] = [row['Gaji'] * 1.05 * 1.02 if row['Usia'] > 30 else row['Gaji Bonus'] for _, row in df.iterrows()]

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

print("\nDataFrame setalah peningkatan gaji")
print(df)

print("\n Ringkasan peningkatan")
for index, row in df.iterrows():
        print(f"{row['Nama']}: Gaji setelah Tambahan {row['Gaji Tambahan usia > 30']:.1f}, Peningkatan sebesar {row['Gaji Tambahan usia > 30'] - row['Gaji Bonus']:.1f}")

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.