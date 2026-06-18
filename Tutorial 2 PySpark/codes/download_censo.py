import os
import requests
import zipfile
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

YEAR = "2021"
URL = f"https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_{YEAR}.zip"

RAW_DIR = "../raw"
ZIP_PATH = f"{RAW_DIR}/censo_{YEAR}.zip"
EXTRACT_PATH = f"{RAW_DIR}/{YEAR}"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(EXTRACT_PATH, exist_ok=True)

print(f"Downloading Censo Escolar {YEAR}...")
response = requests.get(URL, verify=False)

with open(ZIP_PATH, "wb") as f:
    f.write(response.content)

print(f"Extracting Censo Escolar {YEAR}...")
with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
    zip_ref.extractall(EXTRACT_PATH)

print("Download and extraction completed.")