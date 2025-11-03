palang_buka = False # Kondisi palang (terbuka/tertutup).
gol = [1,2,3,4,5] # Golongan kendaraan

gol_pengguna = int(input("\nMasukkan golongan kendaraan\n(1, 2, 3, 4, 5): ")) # Golongan kendaraan pengguna

# Mengecek golongan kendaraan pengguna
if gol_pengguna not in gol:
    print("\nKendaraan tidak boleh masuk tol.\n\n")
    exit()

ruas_tol = ["Surabaya", "Semarang", "Bandung", "Jakarta"] # Ruas tol (misalkan ada 4)

asal_pengguna = input("\nMasukkan ruas tol asal\n(Surabaya, Semarang, Bandung, Jakarta): ") # Ruas tempat pengguna masuk
tujuan_pengguna = input("\nMasukkan ruas tol tujuan\n(Surabaya, Semarang, Bandung, Jakarta): ") # Ruas tempat pengguna keluar

# Mengecek apakah ruas tol masuk dan keluar ada
if asal_pengguna not in ruas_tol or tujuan_pengguna not in ruas_tol:
    print("\nBelum ada tol di daerah-daerah tersebut.\n\n")
    exit()

harga_per_gol = [20_000,30_000,40_000,50_000,60_000] # Harga per golongan

# Perhitungan harga total
tol_diff = abs(ruas_tol.index(tujuan_pengguna) - ruas_tol.index(asal_pengguna)) # "Selisih" ruas tol yang akan ditempuh
harga_total = max(tol_diff + 1, 1) * harga_per_gol[gol_pengguna - 1] # Harga yang harus dibayar (bayar pas masuk + keluar [jika beda ruas])

saldo_cukup = False # Apakah saldo cukup

# Palang terbuka jika saldo cukup dan sebaliknya
while not saldo_cukup:
    print(f"\n=== Anda harus membayar Rp{harga_total},00. ===\n")
    saldo_pengguna = int(input("Masukkan saldo Anda: "))

    if saldo_pengguna < harga_total:
        print("Saldo Anda tidak cukup. Mohon isi ulang.")
    else:
        saldo_cukup = True
        palang_buka = True

# Tampilan sisa saldo pengguna
print(f"\n=== Sisa saldo Anda Rp{saldo_pengguna - harga_total},00. ===\n\nSilakan lewat.\n\n")