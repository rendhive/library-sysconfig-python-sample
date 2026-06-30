import sysconfig

def interactive_config():
    config_vars = sysconfig.get_config_vars()
    for key in config_vars:
        print(f"{key}: {config_vars[key]}")

interactive_config()
# Fungsi: Menampilkan semua variabel konfigurasi dalam sesi interaktif.
# Kondisi: Ketika Anda perlu question tentang konfigurasi dalam cara interaktif.