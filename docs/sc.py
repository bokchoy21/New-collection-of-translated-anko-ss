import os
from pathlib import Path

def rename_txt_to_md():
    cwd = Path.cwd()
    txt_files = list(cwd.glob("*.txt"))
    if not txt_files:
        print("当前目录没有 .txt 文件")
        return

    for txt_path in txt_files:
        md_path = txt_path.with_suffix(".md")
        if md_path.exists():
            print(f"跳过 {txt_path.name}：目标文件 {md_path.name} 已存在")
            continue
        try:
            txt_path.rename(md_path)
            print(f"已重命名：{txt_path.name} -> {md_path.name}")
        except Exception as e:
            print(f"重命名 {txt_path.name} 失败：{e}")

if __name__ == "__main__":
    rename_txt_to_md()