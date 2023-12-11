import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
print(df)

# Pertanyaan 1: Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
gaji_peningkatan1 = lambda gaji: gaji * 1.05

for index, row in df.iterrows():
    df.at[index, 'Gaji'] = gaji_peningkatan1(row['Gaji'])


# Pertanyaan 2: Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nDataFrame Setelah Pembaruan:")
print(df)

print("Ringkasan Perubahan:")
for index, row in df.iterrows():
    print(f"{row['Nama']}: Gaji awal {row['Gaji']/1.05:.2f}, Gaji setelah peningkatan {row['Gaji']:.2f}")


# Pertanyaan 3: Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
gaji_peningkatan2 = lambda gaji, usia: gaji * 1.02 if usia > 30 else gaji * 1

for index, row in df.iterrows():
    df.at[index, 'Gaji'] = gaji_peningkatan2(row['Gaji'], row['Usia'])


# Pertanyaan 4: Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame Setelah Pembaruan:")
print(df)

print("Ringkasan Hasil:")
for index, row in df.iterrows():
    if row['Usia'] >30 :
        print(f"{row['Nama']}: Gaji awal {row['Gaji'] / 1.02:.2f}, Gaji setelah peningkatan {row['Gaji']:.2f}")
    else :
        print(f"{row['Nama']}: Gaji awal {row['Gaji'] / 1:.2f}, Gaji setelah peningkatan {row['Gaji']:.2f}")