import sysconfig

locale_info = sysconfig.get_config_var('LOCALIZED')
print(f"Informasi lokal: {locale_info}")
# Fungsi: Mengetahui apakah Python mendukung lokal atau tidak berdasarkan konfigurasi.
# Kondisi: Ketika Anda ingin memeriksa dukungan lokal di aplikasi Python Anda.