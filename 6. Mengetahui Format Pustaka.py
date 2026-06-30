import sysconfig

lib_format = sysconfig.get_config_var('LD_VERSION')
print(f"Format pustaka: {lib_format}")
# Fungsi: Mendapatkan format versi pustaka dari Python.
# Kondisi: Ketika Anda ingin mengetahui versi pustaka yang terpasang.