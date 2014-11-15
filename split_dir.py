# -*- coding: utf-8 -*-
__author__ = 'vOROn'

import os
import shutil
import argparse

def split_dir(in_path, out_path, size_tom):
    tom = 1
    current_size = 0
    root_len = len(in_path.split(os.sep))
    for (root, dirs, files) in os.walk(in_path):
        path = root.split(os.sep)
        for file in files:
            current_size += os.stat(root+os.sep+file).st_size

            if current_size > size_tom:
                current_size = 0
                tom += 1

            current_dir = os.sep.join(path[root_len:])

            if current_dir:
                print(out_path + os.sep + str(tom) + os.sep + current_dir + os.sep + file)
            else:
                print(out_path + os.sep + str(tom) + os.sep + file)

            new_dir = out_path + os.sep + str(tom) + os.sep + current_dir

            if not os.path.exists(new_dir):
                try:
                    os.makedirs(new_dir)
                except:
                    print("Error create directory: " + new_dir)

            try:
                shutil.copyfile(root + os.sep + file, new_dir + os.sep + file)
            except:
                print("Error copy file: " + new_dir + os.sep + file)


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--in_path', required=True)
    parser.add_argument('-o','--out_path', required=True)
    parser.add_argument('-s','--size_part', type=int, required=True)
    return parser

if __name__ == "__main__":
    parser = argParser()
    space = parser.parse_args()
    split_dir(space.in_path, space.out_path, space.size_part)