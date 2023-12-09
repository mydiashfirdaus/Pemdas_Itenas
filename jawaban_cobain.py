import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

bonus = 0.05
for index, i in df.iterrows():
        df.at[index, 'Bonus_Tetap(Use For)'] = i['Gaji'] + (i['Gaji'] * bonus)


df['Bonus_Tetap(Use Lambda)'] = df.apply(lambda x : x['Gaji'] + (x['Gaji'] * bonus), axis=1)

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

print('DataFrame yang sudah diperbarui:')
print(df)
print()
ringkasan = df[['Bonus_Tetap(Use For)', 'Bonus_Tetap(Use Lambda)']]
print('Ringkasan Penambahan Pada Tabel:')
print(ringkasan)
print()

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

tambahan = 0.02

for index, i in df.iterrows():
        if i['Usia'] > 30:
                df.at[index, 'Karyawan_Mendapatkan_Bonus'] = i['Nama']
        else:
             df.at[index, 'Karyawan_Mendapatkan_Bonus'] = 'Tidak Ada'  

df['Hasil_Tambahan_Gaji'] = df.apply(lambda x : x['Gaji'] + (x['Gaji'] * tambahan) if x['Usia'] > 30 else x['Gaji'], axis=1)

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

print('DataFrame yang sudah diperbaharui:')
print(df)
print()
ringkasan2 = df[['Karyawan_Mendapatkan_Bonus', 'Hasil_Tambahan_Gaji']]
print('Ringkasan Pada Kolom yang sudah ditambahkan:')
print(ringkasan2)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.