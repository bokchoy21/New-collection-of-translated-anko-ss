import re
from pathlib import Path

def sanitize_filenames():
    """
    将当前目录下所有文件的文件名中的空格（包括连续多个空格）和下划线替换为单个“-”，
    并去除首尾多余的“-”。仅处理文件，不处理子目录。
    """
    cwd = Path(".")
    for path in cwd.iterdir():
        if not path.is_file():
            continue

        old_name = path.name
        stem = path.stem      # 主文件名（不含扩展名）
        suffix = path.suffix  # 扩展名（含点）

        # 将空格、下划线（一个或多个）替换为一个“-”，并去掉首尾的“-”
        new_stem = re.sub(r'[\s_]+', '-', stem).strip('-')

        # 如果替换后主名为空（如原文件名全是空格/下划线），给一个默认名
        if not new_stem:
            new_stem = "renamed"

        new_name = new_stem + suffix
        new_path = path.with_name(new_name)

        # 如果新文件名已存在，跳过以避免覆盖
        if new_path.exists():
            print(f"⏭ 跳过 {old_name} -> {new_name}（目标已存在）")
            continue

        # 执行重命名
        try:
            path.rename(new_path)
            print(f"✓ {old_name} -> {new_name}")
        except Exception as e:
            print(f"✗ 重命名 {old_name} 失败: {e}")

if __name__ == "__main__":
    sanitize_filenames()