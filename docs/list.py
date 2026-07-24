from pathlib import Path

def generate_list():
    # 获取当前目录下所有 .md 文件，按名称排序
    md_files = sorted(Path(".").glob("*.md"))
    for f in md_files:
        stem = f.stem  # 不含扩展名的文件名
        print(f"* [{stem}](./docs/{stem})")

if __name__ == "__main__":
    generate_list()