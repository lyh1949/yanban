# -*- coding: utf-8 -*-
"""
重新生成下载二维码。

用法：
    python generate_qr.py "https://你的域名/yanban.apk"

说明：
    拿到真实的 APK 下载地址后，运行本脚本即可更新 assets/qr-download.png。
    同时记得把 index.html 里 script 中的 DOWNLOAD_URL 常量改成同一个地址。
"""

import sys

import qrcode

# 默认占位链接（待定），也可通过命令行参数传入真实地址
DEFAULT_URL = "https://github.com/lyh1949/yanban/releases/latest/download/app-release.apk"


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=16,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0f172a", back_color="#ffffff").convert("RGB")
    img.save("assets/qr-download.png")
    print(f"已生成 assets/qr-download.png，指向：{url}")


if __name__ == "__main__":
    main()
