import os
import re
from pathlib import Path

def rename_images_and_update_md():
    # 设置基础目录
    base_dir = Path("Deep-Learning-for-Vision-Systems")
    image_dir = base_dir / "images/deep_learning_for_vision_systems"
    image_dir.mkdir(parents=True, exist_ok=True)
    
    # 获取所有图片文件（直接位于基础目录下的png文件）
    images = list(base_dir.glob("*.png"))
    
    # 获取现有的图片数量
    existing_images = list(image_dir.glob("image_rename*.png"))
    start_index = len(existing_images) + 1
    
    # 重命名并移动图片文件
    new_image_names = {}
    for i, img_path in enumerate(sorted(images), start=start_index):
        new_name = f"image_rename{i}.png"
        new_path = image_dir / new_name
        
        # 保存相对路径的对应关系
        old_relative = str(img_path.relative_to(base_dir))
        new_relative = str(new_path.relative_to(base_dir))
        new_image_names[old_relative] = new_relative
        
        # 移动并重命名文件
        if img_path != new_path:
            img_path.rename(new_path)
            print(f"Moved and Renamed: {img_path} -> {new_path}")

    # 更新指定目录下的markdown文件
    md_files = list(base_dir.glob("*.md"))
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