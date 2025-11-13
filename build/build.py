#!/usr/bin/env python3
"""
孤客录屏大师 - 打包脚本
用于将Python代码打包为可执行文件
"""

import os
import sys
import PyInstaller.__main__
from PIL import Image, ImageDraw

def create_default_icon():
    """创建默认图标"""
    try:
        size = (256, 256)
        img = Image.new('RGBA', size, (26, 26, 46, 0))
        draw = ImageDraw.Draw(img)
        
        # 绘制录制图标
        outer_margin = 15
        outer_box = [outer_margin, outer_margin, size[0]-outer_margin, size[1]-outer_margin]
        draw.ellipse(outer_box, fill=(0, 136, 255, 255), outline=(0, 255, 136, 255), width=10)
        
        inner_margin = 50
        inner_box = [inner_margin, inner_margin, size[0]-inner_margin, size[1]-inner_margin]
        draw.ellipse(inner_box, fill=(255, 68, 68, 255))
        
        # 保存为ICO
        img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
        return 'icon.ico'
    except Exception as e:
        print(f"图标创建失败: {e}")
        return None

def build_executable():
    """构建可执行文件"""
    print("🚀 开始打包智能录屏大师...")
    
    # 图标处理
    icon_path = 'icon.ico'
    if not os.path.exists(icon_path):
        print("📝 创建默认图标...")
        icon_path = create_default_icon()
    
    # 打包参数
    args = [
        'src/main.py',
        '--name=ScreenRecorderMaster',
        '--onefile',
        '--windowed',
        '--clean',
        '--noconfirm',
        '--hidden-import=cv2',
        '--hidden-import=PIL',
        '--hidden-import=PIL._tkinter_finder',
        '--hidden-import=numpy',
        '--hidden-import=pyautogui',
        '--add-data=tcl;tcl',
        '--add-data=tk;tk',
    ]
    
    if icon_path and os.path.exists(icon_path):
        args.extend(['--icon', icon_path])
        print(f"🎯 使用图标: {icon_path}")
    
    try:
        PyInstaller.__main__.run(args)
        
        # 检查结果
        if os.path.exists('dist/ScreenRecorderMaster.exe'):
            file_size = os.path.getsize('dist/ScreenRecorderMaster.exe') / (1024 * 1024)
            print(f"✅ 打包成功！")
            print(f"📁 文件位置: dist/ScreenRecorderMaster.exe")
            print(f"📊 文件大小: {file_size:.1f} MB")
            return True
        else:
            print("❌ 打包失败")
            return False
            
    except Exception as e:
        print(f"❌ 打包出错: {e}")
        return False

def main():
    print("=" * 50)
    print("       智能录屏大师 - 打包工具")
    print("=" * 50)
    
    # 检查依赖
    try:
        import PyInstaller
        from PIL import Image
    except ImportError:
        print("❌ 缺少必要的依赖")
        print("请运行: pip install pyinstaller pillow")
        return
    
    # 构建
    if build_executable():
        print("\n🎉 打包完成！")
        print("文件已生成在 dist 目录中")
        print("可以分发给其他Windows用户使用")
    else:
        print("\n💥 打包失败")

if __name__ == "__main__":
    main()
