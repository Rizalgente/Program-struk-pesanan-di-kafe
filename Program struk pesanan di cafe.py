print("==== PROGRAM HITUNG TOTAL HARGA PESANAN ====".center(50))
print("="*38)
print("*Menu*".center(37))
print("="*38)
print("1. Susu".rjust(8), "Rp.7.000".rjust(27))
print("2. Teh".rjust(7), "Rp.5.000".rjust(28))
print("3. Kopi".rjust(8), " Rp.5.000".rjust(27))
print("="*38, "\n")

banyak_jenis = int(input("banyak jenis: "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
total = []
i = 0
while i < banyak_jenis:
    print("jenis ke", i+1)
    kode_potong.append(input("kode Pesanan [S/T/K]: "))
    banyak_potong.append(int(input("banyak Pesanan: \n")))

    if kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("Susu")
        harga.append("7000")
        total.append(banyak_potong[i]*int("7000"))
    elif kode_potong[i] == "T" or kode_potong[i] == "t":
        jenis_potong.append("Teh")
        harga.append("5000")
        total.append(banyak_potong[i]*int("5000"))
    elif kode_potong[i] == "K" or kode_potong[i] == "k":
        jenis_potong.append("Kopi")
        harga.append("5000")
        total.append(banyak_potong[i] * int("5000"))
    else:
        jenis_potong.append("Kode salah")
        harga.append("0")
        total.append(banyak_potong[i]*int("0"))
    i = i+1

print("="*61)
print("*CAFE BALE-BALE*".center(61))
print("="*61)
print("No".rjust(4), "Jenis".rjust(10), "Harga".rjust(15), "Banyak".rjust(15), "Jumlah".rjust(10))
print("".rjust(4), "Potong".rjust(11), "satuan".rjust(15), "Beli".rjust(13), "Harga".rjust(11))
print("-"*61)

jumlah_bayar = 0
a = 0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar + total[0]
    print("  %i       %s            %s            %i       Rp.%i\n" % (a+1, jenis_potong[a],
                                                                       harga[a], banyak_potong[a], total[a]))
    a = a + 1
print("Total jumlah Rp.".rjust(52), jumlah_bayar)
print("-"*61)

jumlah = jumlah_bayar
if jumlah >= 35000:
    diskon = jumlah_bayar / 10
    total_bayar = jumlah_bayar - diskon
    print("Diskon 10% Rp.".rjust(50), diskon)
    print("kamu hanya perlu membayar Rp.".rjust(49), total_bayar)
elif jumlah >= 35000 or jumlah_bayar >= 15000:
    diskon = jumlah_bayar / 5
    total_bayar = jumlah_bayar - diskon
    print("Diskon 5% Rp.".rjust(50), diskon)
    print("kamu hanya perlu membayar Rp.".rjust(49), total_bayar)
elif jumlah < 15000:
    diskon = 0
    total = jumlah_bayar
    print("Diskon Rp.0".rjust(47))
    print("Total bayar Rp.".rjust(51), total)
print("="*61)
