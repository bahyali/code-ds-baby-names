import requests
import zipfile
from pathlib import Path


def download_extract_baby_names():
    zip_file_path = "names.zip"
    r = requests.get('https://www.ssa.gov/oact/babynames/names.zip')

    open(zip_file_path, "wb").write(r.content)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall("data")


def data_is_downloaded():
    root_directory = Path('./data')
    data_dir_size = sum(
        f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())

    return data_dir_size >= 26000000   # approximate size of directory
