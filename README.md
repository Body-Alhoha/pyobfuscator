# pyobfuscator

Proof of concept python obfuscator made in less than an hour and a half using the `ast` and `astor` Python packages

Transformers:
- String encryption
- Builtins calls hider
(more whenever i feel like it)

<br>

Example input:
```python
print("Hello, World")
```

Output:
```python
from fernet import Fernet
import base64
def HlZzdoXnZQ(a : str):
    b, c = base64.b64decode(a.encode()).split(b":", 1)
    return Fernet(b).decrypt(c).decode()
_YAQLHMxVMc = eval(HlZzdoXnZQ(
    'Rmc3Y1ltRkxvRVhQQW0xVzhQWkR3aWFCUDktdmVieEJGOUNYc2FCaGxRVT06Z0FBQUFBQm4yMFhZZ3lmdFBMYzNkVExYcmdVM280Rjg5bUg1TVZRTnc4Znd4REVzTTJ1akg4YUtnNk5IOHNPaDJrREtodFlYWVN5UE9tODVUMEtienc0R1hhbWY1MWhmdVE9PQ=='
    ))()
getattr(_YAQLHMxVMc[HlZzdoXnZQ(
    'SjNieFRXa1UxNTZUV05EaXRLTXdyWEhGRlZPTHhfSUxSTjlleEFtX0VIdz06Z0FBQUFBQm4yMFhZbkwtZUF3NXBXQ05aYVN2eWZDSExOaDB2SVZwekhPc2U1Q0lOZF9DX0hMajdMcG91Q0hJRnY4T09zODlwV2p6NWI4M1RwUkhjbl9TWjc4TFdwR21adXc9PQ=='
    )], HlZzdoXnZQ(
    'N2JmWnl4VTlTZzUzOVdHaHppUnMzR0pBd1dmS0ZEY19CT081Q1hHTkZWMD06Z0FBQUFBQm4yMFhZQjRoV2lmUWZKR0Eyb0J4b3RMMGQwOUFqenNlbm83YlN5VFVNSjVmQ3l3a3ZjQjViSUFXSmtXbmRnU2JwTkwtRUl1c2x2RVc0LTFJa2U1OE1zTGVEN3c9PQ=='
    ))(HlZzdoXnZQ(
    'NkJfS2cxWDZDekg3SHVZaGJSUkkyWDFsOGR3VE1vWFFqZF9uU3I2N2hhQT06Z0FBQUFBQm4yMFhZaHZHQ3VjaWctUVFjNUwtMHlZUi1DNTBqRHlGcEZhY2tDenc0NlJDXzVZdm5ZOTI4aGY3YS1EQzl6WHg4NnYxTjBIb25uNWtITEg4TEpIREJiMTZMSFE9PQ=='
    ))
```
