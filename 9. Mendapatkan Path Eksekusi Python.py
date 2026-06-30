import sysconfig

python_executable = sysconfig.get_config_var('PYTHONEXECUTABLE')
print(f"Path eksekusi Python: {python_executable}")
# Fungsi: Mendapatkan jalur eksekusi Python yang sedang digunakan.
# Kondisi: Ketika Anda ingin mengetahui lokasi file eksekusi Python.