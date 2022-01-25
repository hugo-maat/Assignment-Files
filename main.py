__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

"""Assignment: Files voor Winc Academy
Hugo Maat, 25-1-2022
Versie 1.0

Note: deze code vervult de opdracht, maar werd niet goedgekeurd
door Wincpy. Onderaan staat een alternatieve versie van vraag 3 en 4
die goedgekeurd werd door Wincpy maar niet de opdracht vervulde.
Ik denk dat Wincpy een andere schrijfwijze van de Path wilde zien.
"""

from pathlib import Path
from zipfile import ZipFile

# Part 1
def clean_cache():
    if Path('cache').exists() != True:
        Path('cache').mkdir()
    p = Path('cache')
    q = p.iterdir()
    for item in q:
        item.unlink()
    
# Part 2
def cache_zip(zip_file_path, cache_dir_path):
    ZipFile(zip_file_path, 'r').extractall(cache_dir_path)

# Part 3
def cached_files():
    p = Path('cache')
    q = p.iterdir()
    list = [file.resolve() for file in q]
    return list

# Part 4
def find_password(list):
    for file in list:
        content = file.read_text()
        if 'password' in content.lower():
            return content

# XKCD! Natuurlijk. Uitstekende keuze.

"""
def cached_files():
    import os
    p = Path('cache')
    q = p.iterdir()
    list = [os.path.abspath(file) for file in q]
    return list

# Part 4
def find_password(list):
    for file in list:
        path = Path(file)
        content = path.read_text()
        if 'password' in content.lower():
            return content
"""