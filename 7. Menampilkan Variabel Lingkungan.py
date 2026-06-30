import sysconfig

env_vars = sysconfig.get_platform()
print(f"Variabel lingkungan: {env_vars}")
# Fungsi: Menampilkan variabel lingkungan yang terkait dengan konfigurasi Python.
# Kondisi: Ketika Anda ingin melihat setelan lingkungan untuk Python yang sedang berjalan.