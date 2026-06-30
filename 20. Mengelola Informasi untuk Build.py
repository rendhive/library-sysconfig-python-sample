import sysconfig

build_info = sysconfig.get_platform()
print(f"Platform untuk build: {build_info}")
# Fungsi: Mengambil informasi tentang platform untuk membangun Python.
# Kondisi: Ketika Anda bekerja dengan berbagai build dan memerlukan detail tentang kondisi build.