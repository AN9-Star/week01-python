import sys
import platform

print("=" * 40)
print("环境跑通了")
print("=" * 40)
print(f"Python 版本: {sys.version.split()[0]}")
print(f"解释器路径: {sys.executable}")
print(f"操作系统  : {platform.system()} {platform.release()}")
