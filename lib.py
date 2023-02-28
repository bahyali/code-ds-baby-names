import os
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


def loop_on_files(filter="all"):
    with os.scandir("./data") as data:
        for item in data:
            if item.name.endswith(".txt") and item.is_file():
                with open(item.path, "r") as year_file:
                    read_content = year_file.read()
                yield item.name, item.name.strip("yob.txt"), read_content


if __name__ == "__main__":
    for file_name, year, content in loop_on_files():
        print(file_name, year, content)
