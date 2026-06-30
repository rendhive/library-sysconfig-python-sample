import sysconfig

def programmer_paths():
    paths = sysconfig.get_paths(True)  # Mengambil semua jalur termasuk developer
    print("Jalur untuk pengembang:", paths)

programmer_paths()
# Fungsi: Mendapatkan jalur pembuatan untuk menyerupai pengembang.
# Kondisi: Ketika Anda mengembangkan dalam Python dan memerlukan jalur pembangunan.