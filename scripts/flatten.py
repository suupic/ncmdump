# 将多级子目录中的文件整理到一级目录
# 适用于将 “歌手-专辑-歌曲” 的结构转化为 “歌手-歌曲”

import os
import shutil
import sys

def movefile(source, dest):    
    try:
        shutil.move(source, dest)
    except shutil.Error:
        os.remove(source)

def output(src, target_dir, dir):
    output_path = os.path.join(target_dir, dir)
    print('    ' + src + ' --> ', output_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    movefile(src, output_path)

def flatten(dir, root, target_dir):
    print("  checking ", dir)
    for sub_dir in os.listdir(dir):
        sub_dir_path = os.path.join(dir, sub_dir)
        if(os.path.isdir(sub_dir_path)):
            flatten(sub_dir_path, root, target_dir)
        else:
            output(sub_dir_path, target_dir, root)

root_dir = os.path.abspath(sys.argv[1])
target_dir = os.path.abspath(sys.argv[2])
print("ROOT: ", root_dir)
print("target_dir: ", target_dir)

for dir in os.listdir(root_dir):
    if(os.path.isdir(dir)):
        print("  process dir: ", dir)
        flatten(dir, dir, target_dir)
