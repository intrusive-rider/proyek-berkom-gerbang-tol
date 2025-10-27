palang_buka = False
gol = [1,2,3,4,5]

gol_pengguna = int(input("\nMasukkan golongan kendaraan\n(1, 2, 3, 4, 5): "))

gol_boleh_masuk = False

for golongan in gol:
    if gol_pengguna == golongan:
        gol_boleh_masuk = True
        break

if not gol_boleh_masuk:
    print("\nKendaraan tidak boleh masuk tol.\n\n")
    exit()

ruas_tol = ["Surabaya", "Semarang", "Bandung", "Jakarta"]

asal_pengguna = input("\nMasukkan ruas tol asal\n(Surabaya, Semarang, Bandung, Jakarta): ")

daerah_ada_tol = False

for asal in ruas_tol:
    if asal_pengguna == asal:
        daerah_ada_tol = True
        break

tujuan_pengguna = input("\nMasukkan ruas tol tujuan\n(Surabaya, Semarang, Bandung, Jakarta): ")

for tujuan in ruas_tol:
    if tujuan_pengguna == tujuan:
        daerah_ada_tol = True
        break

if not daerah_ada_tol:
    print("\nBelum ada tol di daerah-daerah tersebut.\n\n")
    exit()

harga_per_gol = [20_000,30_000,40_000,50_000,60_000]

harga_total = max(abs(ruas_tol.index(tujuan_pengguna) - ruas_tol.index(asal_pengguna)) + 1, 1) * harga_per_gol[gol_pengguna - 1]

saldo_cukup = False

while not saldo_cukup:
    print(f"\n=== Anda harus membayar Rp{harga_total},00. ===\n")
    saldo_pengguna = int(input(f"Masukkan saldo Anda: "))

    if saldo_pengguna < harga_total:
        print("Saldo Anda tidak cukup. Mohon isi ulang.")
    else:
        saldo_cukup = True
        palang_buka = True

print(f"\n=== Sisa saldo Anda Rp{saldo_pengguna - harga_total},00. ===\n\nSilakan lewat.\n\n")