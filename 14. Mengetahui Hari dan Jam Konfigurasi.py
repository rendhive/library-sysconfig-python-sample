import sysconfig

def config_date():
    build_time = sysconfig.get_config_var('DATE')
    print(f"Waktu konfigurasi: {build_time}")

config_date()
# Fungsi: Mengetahui kapan Python dikompilasi.
# Kondisi: Ketika Anda ingin memastikan kapan versi tertentu dari Python dibangun.