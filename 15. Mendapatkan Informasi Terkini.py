import sysconfig

latest_info = sysconfig.get_platform() + f" - Versi Python: {sysconfig.get_python_version()}"
print("Informasi terkini:", latest_info)
# Fungsi: Menampilkan informasi terakhir dari konfigurasi.
# Kondisi: Ketika Anda memerlukan ringkasan terbaru dari konfigurasi Python.