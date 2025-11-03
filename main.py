palang_buka = False # Kondisi palang (terbuka/tertutup).
gol = [1,2,3,4,5] # Golongan kendaraan

gol_pengguna = int(input("\nMasukkan golongan kendaraan\n(1, 2, 3, 4, 5): ")) # Golongan kendaraan pengguna

gol_boleh_masuk = False # Apakah kendaraan boleh masuk

# Mengecek golongan kendaraan pengguna
for golongan in gol:
    if gol_pengguna == golongan:
        gol_boleh_masuk = True
        break

# Kendaraan pengguna tidak boleh masuk tol jika bukan golongan yang boleh masuk
if not gol_boleh_masuk:
    print("\nKendaraan tidak boleh masuk tol.\n\n")
    exit()

ruas_tol = ["Surabaya", "Semarang", "Bandung", "Jakarta"] # Ruas tol (misalkan ada 4)

asal_pengguna = input("\nMasukkan ruas tol asal\n(Surabaya, Semarang, Bandung, Jakarta): ") # Ruas tempat pengguna masuk
tujuan_pengguna = input("\nMasukkan ruas tol tujuan\n(Surabaya, Semarang, Bandung, Jakarta): ") # Ruas tempat pengguna keluar

daerah_ada_tol = False # Apakah ruas tol ada

# Mengecek apakah ruas tol masuk dan keluar ada
for asal in ruas_tol:
    if asal_pengguna == asal:
        daerah_ada_tol = True
        break

for tujuan in ruas_tol:
    if tujuan_pengguna == tujuan:
        daerah_ada_tol = True
        break

# Tidak bisa pake tol kalau ruas tol belum ada
if not daerah_ada_tol:
    print("\nBelum ada tol di daerah-daerah tersebut.\n\n")
    exit()

harga_per_gol = [20_000,30_000,40_000,50_000,60_000] # Harga per golongan

# Perhitungan harga total
tol_diff = abs(ruas_tol.index(tujuan_pengguna) - ruas_tol.index(asal_pengguna)) # "Selisih" ruas tol yang akan ditempuh
harga_total = max(tol_diff + 1, 1) * harga_per_gol[gol_pengguna - 1] # Harga yang harus dibayar (bayar pas masuk + keluar)

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