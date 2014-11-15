split_dir
=========
Разбивает директорию на поддиректории в зависимости от размера:

usage: split_dir.exe [-h] [--in_path IN_PATH] [--out_path OUT_PATH] [--size SIZE]

optional arguments:
-h, --help show this help message and exit
--in_path IN_PATH
--out_path OUT_PATH
--size SIZE (в байтах)

Пример:

split_dir.exe --in_path="H:\Sid Meiers Civilization Beyond Earth" --out_path="H:\work\Civ" --size=1073741824
