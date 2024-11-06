import pyfiglet

def generate_banner(text):
    # Menggunakan font 'block' yang lebih tebal
    banner = pyfiglet.figlet_format(text, font="block")
    return banner

def display_banner():
    banner = generate_banner("RYZWAN")  # Ganti dengan teks yang diinginkan
    print(banner)

# Menjalankan fungsi untuk menampilkan banner
display_banner()
