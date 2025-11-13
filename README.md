# 🎬 孤客录屏大师 - Screen Recorder Master

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

一个功能强大、界面美观的屏幕录制工具，支持全屏和区域录制，具有现代化的用户界面。

## ✨ 特性

- 🖥️ **全屏/区域录制** - 支持全屏或自定义区域录制
- 🎯 **多种画质** - 超清、高清、标准、流畅四种画质选择
- ⚡ **快捷键操作** - F9开始/停止录制，F10紧急停止
- 🎨 **现代化界面** - 深色科技主题，美观易用
- 📁 **文件管理** - 录制历史管理，支持播放和删除
- 💾 **自定义保存路径** - 自由选择文件保存位置

## 🚀 快速开始

### 方式一：使用预编译版本（推荐）

1. 前往 [Releases](https://github.com/GUKE007/Guke-Screen-Recording-Tool/) 页面
2. 下载最新版本的 `ScreenRecorderMaster_v1.0.0.exe`
3. 双击即可运行，无需安装任何依赖

### 方式二：从源代码运行

1. 克隆项目
```bash
git clone https://github.com/GUKE007/Guke-Screen-Recording-Tool.git
cd screen-recorder-master

```

安装依赖

```bash
pip install -r requirements.txt

```

运行程序

```bash
python src/main.py

```

🎮 使用方法
基本操作
选择录制模式：全屏或区域录制

选择画质：根据需求选择适合的画质

设置保存路径：选择文件保存位置

开始录制：点击"开始录制"按钮或按 F9 键

停止录制：再次按 F9 键或点击"停止录制"

快捷键
F9 - 开始/停止录制

F10 - 紧急停止录制

双击文件 - 播放选中的录制文件

🛠️ 自行打包
如果需要自行打包为exe文件：

```bash

# 安装打包工具
pip install pyinstaller
```

# 打包程序
python build/build.py
打包后的exe文件将生成在 dist 目录中。

📸 界面预览
<img width="495" height="680" alt="image" src="https://github.com/user-attachments/assets/de433073-def5-46df-a17e-44d370b0e301" />


📁 项目结构
```text
screen-recorder-master/
├── src/                 # 源代码
│   ├── main.py         # 主程序
│   └── requirements.txt # 依赖列表
├── docs/               # 文档和截图
├── build/              # 打包脚本
├── dist/               # 发布文件
└── README.md          # 项目说明

```

🤝 贡献
欢迎提交 Issue 和 Pull Request！

📄 许可证
本项目采用 MIT 许可证 - 查看 LICENSE 文件了解详情

🙏 致谢
感谢以下开源项目：

PyAutoGUI - 屏幕操作

OpenCV - 视频处理

Pillow - 图像处理

text

### CHANGELOG.md
```markdown
# 更新日志

## [1.0.0] - 2024-01-XX

### 新增
- 全屏和区域录制功能
- 四种画质选择（超清、高清、标准、流畅）
- 快捷键支持（F9开始/停止，F10紧急停止）
- 现代化深色主题界面
- 录制文件管理功能
- 自定义保存路径

### 技术特性
- 基于Python和Tkinter开发
- 使用OpenCV进行视频编码
- 多线程录制，不影响界面响应
- 自动文件大小计算和显示
```
