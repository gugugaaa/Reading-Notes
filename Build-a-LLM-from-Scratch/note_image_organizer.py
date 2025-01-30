import os
from pathlib import Path

def rename_images_and_update_md():
    # 设置基础目录
    base_dir = Path("Build-a-LLM-from-Scratch")
    image_dir = base_dir / "images" / "build-a-llm"
    image_dir.mkdir(parents=True, exist_ok=True)
    
    # 获取所有PNG图片
    images = list(base_dir.glob("*.png"))
    existing_images = list(image_dir.glob("image_rename*.png"))
    start_index = len(existing_images) + 1

    # 重命名并移动图片
    new_image_names = {}
    for i, img_path in enumerate(sorted(images), start=start_index):
        new_name = f"image_rename{i}.png"
        new_path = image_dir / new_name
        
        relative_old_path = img_path.relative_to(base_dir)
        relative_new_path = new_path.relative_to(base_dir)
        
        new_image_names[str(relative_old_path)] = str(relative_new_path)
        
        if img_path != new_path:
            img_path.rename(new_path)
            print(f"Moved and Renamed: {relative_old_path} -> {relative_new_path}")

    # 更新markdown文件
    md_files = list(base_dir.glob("*.md"))
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_path, new_path in new_image_names.items():
            old_path = str(old_path).replace("\\", "/")
            new_path = str(new_path).replace("\\", "/")
            content = content.replace(old_path, new_path)
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated markdown file: {md_file}")

if __name__ == "__main__":
    rename_images_and_update_md()