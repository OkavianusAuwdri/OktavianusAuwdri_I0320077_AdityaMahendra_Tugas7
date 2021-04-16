# Exercise 7.1
# Variabel global
nama = "Posi"
tahun = "2008"

def help():
    # variabel lokal
    nama = "Lab Posi"
    tahun = "18"
    print("nama= %s" % nama)
    print("tahun = %s" % tahun)

print("nama = %s" % nama)
print("tahun = %s" % tahun)
help()
