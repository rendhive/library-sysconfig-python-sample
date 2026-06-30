import sysconfig

install_dir = sysconfig.get_python_lib()
print(f"Direktori instalasi Python: {install_dir}")
# Fungsi: Mendapatkan lokasi direktori pustaka instalasi Python.
# Kondisi: Ketika Anda ingin mengetahui direktori tempat Python diinstal.