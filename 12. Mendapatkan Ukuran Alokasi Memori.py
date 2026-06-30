import sysconfig

def memory_size():
    size = sysconfig.get_config_var('PyMem_GetSize')
    print(f"Ukuran alokasi memori: {size}")

memory_size()
# Fungsi: Mengetahui ukuran memori yang dialokasikan untuk objek Python.
# Kondisi: Ketika Anda ingin mengukur penggunaan memori di lingkungan Python tertentu.