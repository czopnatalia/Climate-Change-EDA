import zipfile
import os

# Ścieżka do folderu z plikami .zip
folder_zip = "C:/IiAD/uczenie_maszynowe/klimat_projekt/rest_data"

# Ścieżka, gdzie będą rozpakowane archiwa
folder_wyjsciowy = "C:/IiAD/uczenie_maszynowe/klimat_projekt/rest_data/unzip"

# Tworzymy folder wyjściowy jeśli nie istnieje
os.makedirs(folder_wyjsciowy, exist_ok=True)

# Iterujemy po wszystkich plikach w folderze
for plik in os.listdir(folder_zip):
    if plik.endswith(".zip"):
        sciezka_zip = os.path.join(folder_zip, plik)
        # Tworzymy osobny folder dla każdego archiwum
        nazwa_folderu = os.path.join(folder_wyjsciowy, os.path.splitext(plik)[0])
        os.makedirs(nazwa_folderu, exist_ok=True)
        
        # Rozpakowywanie archiwum
        with zipfile.ZipFile(sciezka_zip, 'r') as zip_ref:
            zip_ref.extractall(nazwa_folderu)
        
        print(f"Rozpakowano: {plik} -> {nazwa_folderu}")
