# 
# 基于文件名将歌曲文件分类到歌手目录

import os
import shutil
import sys

def movefile(source, dest):    
    try:
        shutil.move(source, dest)
    except shutil.Error:
        os.remove(source)

root_dir = os.path.abspath(sys.argv[1])
target_dir = os.path.abspath(sys.argv[2])
print("ROOT: ", root_dir)
print("target_dir: ", target_dir)

for file in os.listdir(root_dir):
    if(os.path.isfile(file)):
        artist, music = file.split(" - ", 1)
        print("artist: ", artist, "  music:", music)
        output_path = os.path.join(target_dir, artist)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        print('    ' + file + ' --> ', output_path)
        movefile(file, output_path)        
