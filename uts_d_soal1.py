# ============================
# SOAL 1 – VIGENERE CIPHER
# ============================

plaintext = "SECURITYISPRIORITY"
key = "LEMON"

# ---- Helper functions ----
def char_to_num(c):
    return ord(c) - 65

def num_to_char(n):
    return chr((n % 26) + 65)

# ---- Extend key ----
def repeat_key(key, length):
    key = key.upper()
    return (key * (length // len(key))) + key[:length % len(key)]

# Generate repeated key
key_full = repeat_key(key, len(plaintext))

# ---- Encryption ----
ciphertext = ""
table = []  # to store calculation rows

for p, k in zip(plaintext, key_full):
    Pn = char_to_num(p)
    Kn = char_to_num(k)
    Cn = (Pn + Kn) % 26
    C = num_to_char(Cn)
    ciphertext += C

    table.append((p, Pn, k, Kn, Cn, C))

# ---- Decryption (verification) ----
decrypted = ""
for c, k in zip(ciphertext, key_full):
    Cn = char_to_num(c)
    Kn = char_to_num(k)
    Pn = (Cn - Kn) % 26
    decrypted += num_to_char(Pn)

# ---- OUTPUT ----
print("=== SOAL 1 – VIGENÈRE CIPHER ===")
print("Plaintext :", plaintext)
print("Key       :", key)
print("Full Key  :", key_full)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)

print("\n--- Tabel Perhitungan ---")
print("P   P#   K   K#   (P+K)%26   C")
for row in table:
    p, pn, k, kn, cn, c = row
    print(f"{p}   {pn:2}   {k}   {kn:2}     {cn:2}        {c}")
