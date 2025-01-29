import os
import re
from pathlib import Path

def rename_images_and_update_md():
    # 1. 获取所有图片文件
    image_dir = Path("images/deep_learning_for_vision_systems")
    image_dir.mkdir(parents=True, exist_ok=True)
    images = list(Path("Deep-Learning-for-Vision-Systems").glob("*.png"))
    
    # 获取现有的图片数量
    existing_images = list(image_dir.glob("image_rename*.png"))
    start_index = len(existing_images) + 1
    
    # 2. 重命名并移动图片文件
    new_image_names = {}  # 存储旧文件名到新文件名的映射
    for i, img_path in enumerate(sorted(images), start=start_index):
        new_name = f"image_rename{i}.png"
        new_path = image_dir / new_name
        
        # 保存旧名字和新名字的对应关系
        new_image_names[str(img_path)] = str(new_path)
        
        # 移动并重命名文件
        if img_path != new_path:
            img_path.rename(new_path)
            print(f"Moved and Renamed: {img_path} -> {new_path}")

    # 3. 更新markdown文件中的图片引用
    md_files = list(Path(".").glob("*.md"))
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        # 替换所有图片引用
        for old_path, new_path in new_image_names.items():
            old_path = old_path.replace("\\", "/")
            new_path = new_path.replace("\\", "/")
            content = content.replace(old_path, new_path)
        
        # 写回文件
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated markdown file: {md_file}")

if __name__ == "__main__":
    rename_images_and_update_md()