# run_labelme.py
import sys
import importlib.metadata

# 保存原始函数
_original_version = importlib.metadata.version

def _patched_version(package_name):
    if package_name == "labelme":
        return "0.0.0.dev0"
    return _original_version(package_name)

# 应用 patch
importlib.metadata.version = _patched_version

# 现在可以安全导入 labelme
from labelme.__main__ import main

if __name__ == "__main__":
    main()