import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# soal 1
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x * 1.05)(row['Gaji'])

# soal 2
print("DataFrame setelah peningkatan gaji 5%:")
print(df)

# Ringkasan perubahan
summary_1 = df.describe()

# Soal 3

for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x * 1.02)(row['Gaji'])

# Soal 4

print("\nDataFrame setelah peningkatan gaji tambahan untuk karyawan di atas 30 tahun:")
print(df)

# Ringkasan perubahan
summary_2 = df.describe()

# Ringkasan hasil
print("\nRingkasan hasil setelah peningkatan gaji:")
print(summary_2 - summary_1)
