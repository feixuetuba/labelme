import importlib.metadata

__appname__ = "Labelme"

# Semantic Versioning 2.0.0: https://semver.org/
# 1. MAJOR version when you make incompatible API changes;
# 2. MINOR version when you add functionality in a backwards-compatible manner;
# 3. PATCH version when you make backwards-compatible bug fixes.
# e.g., 1.0.0a0, 1.0.0a1, 1.0.0b0, 1.0.0rc0, 1.0.0, 1.0.0.post0
try:
    __version__ = importlib.metadata.version("labelme")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

# XXX: onnxruntime used to be imported here to ensure correct DLL loading order
# on Windows (before PySide6). It's now lazily loaded in _automation modules
# when AI features are actually used. See issue #1564.
