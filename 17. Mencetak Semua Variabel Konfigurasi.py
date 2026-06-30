import sysconfig

def print_all_vars():
    for var in dir(sysconfig):
        if not var.startswith("_"):
            print(var)

print_all_vars()
# Fungsi: Menampilkan semua variabel dan fungsi yang tersedia di modul sysconfig.
# Kondisi: Ketika Anda ingin menjelajahi semua opsi yang bisa dibuat di modul sysconfig.