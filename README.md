# 言办 · 产品介绍网页

一个用于介绍「言办」的静态网页，包含产品介绍、使用说明、常见问题，以及 **扫码下载 APK** 的下载二维码。

## 文件结构

```
.
├── index.html                 # 网页主文件（样式与脚本已内联，可直接打开）
├── app_icon.png               # App 原始 Logo（源文件，1536×1536）
├── assets/
│   ├── app_icon.png           # 网页用的 Logo（512×512 优化版）
│   ├── icon-192.png           # 192×192（可作 PWA 图标）
│   ├── favicon.png            # 浏览器标签页图标
│   ├── screenshot.png         # App 运行效果图（来源：Screenshot_20261007_180004.png）
│   └── qr-download.png        # 下载二维码（扫码下载 APK）
├── generate_qr.py             # 重新生成二维码的脚本
└── 产品及使用说明书.md          # 产品说明文档（内容来源）
```

## 如何上线

`index.html` 是一个完全静态的单文件网页（仅引用 `assets/` 下的图片），可直接：

1. 用浏览器打开 `index.html` 预览；
2. 将整个目录上传到任意静态托管（GitHub Pages、Vercel、Nginx、对象存储等）。

## 更新下载链接（重要）

APK 下载地址目前是**待定**状态，二维码指向占位地址 `https://example.com/yanban.apk`。拿到真实地址后，按以下两步更新：

1. **重新生成二维码**：
   ```bash
   pip install qrcode   # 首次需要
   python generate_qr.py "https://你的真实下载地址/yanban.apk"
   ```
2. **改网页里的下载链接**：编辑 `index.html`，把底部 `<script>` 里的
   `DOWNLOAD_URL` 常量改成同一个地址，下载按钮会自动变为可点击。

## 说明

- 目前仅支持 Android（Android 7.0 及以上）。
- App 本身不提供模型服务，用户需自行申请 DeepSeek API Key（`deepseek-flash`）。
