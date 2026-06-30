import sysconfig

def list_libs():
    libs = sysconfig.get_paths()
    for key, value in libs.items():
        print(f"{key}: {value}")

list_libs()
# Fungsi: Menampilkan semua jalur pustaka dan direktori Python.
# Kondisi: Ketika Anda ingin mengetahui jalur direktori pustaka Python yang terpasang.