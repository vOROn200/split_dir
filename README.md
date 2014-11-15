split_dir
=========
Разбивает директорию на поддиректории в зависимости от размера:

usage: split_dir.py [-h] -i IN_PATH -o OUT_PATH -s SIZE_PART

optional arguments:
  -h, --help            show this help message and exit
  -i IN_PATH, --in_path IN_PATH
  -o OUT_PATH, --out_path OUT_PATH
  -s SIZE_PART, --size_part SIZE_PART (в байтах)

Пример:

split_dir.exe --in_path="H:\Sid Meiers Civilization Beyond Earth" --out_path="H:\work\Civ" --size_part=1073741824
