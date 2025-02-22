import requests
import json
import os
import sys

# URL raw dari users.json di GitHub
URL_USERS = "https://raw.githubusercontent.com/goldeneye121/xi/refs/heads/main/users.json"

# Token akses yang akan divalidasi di bot.py
SECURITY_TOKEN = "DARK-XPROFESIONALMADEININDONESIA"

def ambil_users(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Pastikan status 200
        return json.loads(response.text)
    except requests.RequestException as e:
        print("Terjadi kesalahan saat mengambil data:", e)
        return None
    except json.JSONDecodeError:
        print("Gagal membaca format JSON.")
        return None

def cek_integritas():
    """Cek apakah bot.py masih ada, jika tidak, hentikan eksekusi."""
    if not os.path.exists("bot.py"):
        print("Peringatan: bot.py hilang! Program dihentikan.")
        sys.exit(1)

def main():
    cek_integritas()
    
    users = ambil_users(URL_USERS)
    if users is None:
        print("Tidak dapat mengambil data pengguna. Program dihentikan.")
        return
    
    username_input = input("Masukkan username Anda: ").strip()

    if username_input in users:
        print("Selamat datang, akses diterima!")

        # Set environment variable untuk bot.py
        os.environ["ACCESS_TOKEN"] = SECURITY_TOKEN

        # Jalankan script berikutnya (bot.py)
        os.system("python3 bot.py")
    else:
        print("Maaf, akses ditolak. Username tidak ditemukan.")

if __name__ == '__main__':
    main()
