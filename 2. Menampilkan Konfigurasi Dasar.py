import sysconfig

def display_config():
    config = sysconfig.get_config_vars()
    for key, value in config.items():
        print(f"{key}: {value}")

display_config()
# Fungsi: Menampilkan semua variabel konfigurasi dasar untuk Python.
# Kondisi: Ketika Anda ingin melihat pengaturan dasar dari Python yang sedang berjalan.