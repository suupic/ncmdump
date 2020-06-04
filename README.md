# ncmdump

## 简介

本项目在[yoki123/ncmdump](https://github.com/yoki123/ncmdump)基础上改进，更方便地对大量文件进行批量处理

## 新特性

1. 支持子目录遍历
2. 允许跳过处理已转化过的ncm文件
3. 支持输出到新的目录并保持原目录结构
4. 更友好的CLI命令行

## 如何使用？

- 使用命令ncmdump
```
    NAME:
    NCMDump - Covert Neteast Cloud Music's .ncm file to .flac or .mp3 format

    USAGE:
    ncmdump.exe [global options] command [command options] [arguments...]

    VERSION:
    0.3.1

    COMMANDS:
        help, h  Shows a list of commands or help for one command

    GLOBAL OPTIONS:
    --base path BASE PATH, -b BASE PATH  BASE PATH of resources
    --force, -f             force to process .ncm which has already coverted
    --input PATH, -i PATH   input PATH of .ncm files
    --output PATH, -o PATH  output PATH of coverted files
    --recursive, -r         recursive sub directories
    --help, -h              show help
    --version, -v           show the version    
```

## Example
```
ncmdump.exe -r -i "J:\CloudMusic" -b "J:\CloudMusic" -o "j:\output"  
```
## 感谢

- [@anonymous5l](https://github.com/anonymous5l)提供的原版ncmdump
- [@eternal-flame-AD](https://github.com/eternal-flame-AD)提供的flac封面写入和目录自动寻找ncm文件
- [@yoki123](https://github.com/yoki123)提供的Golang版ncmdump