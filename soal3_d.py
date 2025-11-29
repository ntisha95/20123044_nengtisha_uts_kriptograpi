from collections import Counter
import matplotlib.pyplot as plt

# === 1. INPUT CIPHERTEXT ===
ciphertext = """
ZIT JX UFN ZIT VXFG QGMTR JXU BMEK ZIT OQFN
JXU ZDGMEK ZIT UFN BMEK JXU VXFG QGMTR
"""

# Bersihkan teks
clean_text = ciphertext.replace(" ", "").replace("\n", "")

# === 2. HITUNG FREKUENSI HURUF ===
frekuensi = Counter(clean_text)

# Urutkan dari terbesar
frekuensi_sorted = sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)

# === 3. TAMPILKAN TABEL FREKUENSI ===
print("=== TABEL FREKUENSI HURUF ===")
print("Huruf | Frekuensi")
print("------------------")
for huruf, jumlah in frekuensi_sorted:
    print(f"  {huruf}   |    {jumlah}")

# === 4. BUAT GRAFIK BATANG ===
huruf = [item[0] for item in frekuensi_sorted]
jumlah = [item[1] for item in frekuensi_sorted]

plt.figure()
plt.bar(huruf, jumlah)
plt.xlabel("Huruf")
plt.ylabel("Frekuensi")
plt.title("Grafik Frekuensi Huruf Ciphertext")
plt.grid(True)

# === 5. SIMPAN GRAFIK KE FILE ===
plt.savefig("grafik_frekuensi_ciphertext.png")
plt.show()

print("\nGrafik berhasil disimpan sebagai: grafik_frekuensi_ciphertext.png")
