from core.obfuscator import PyObfuscator
from transformers.string_encryption import StringEncryption
from transformers.builtins import BuiltinsTransformer

obfusctor = PyObfuscator(
    "tests/input",
    "tests/output",
    transformers=[
        BuiltinsTransformer,
        StringEncryption
    ]
)

obfusctor.obfuscate()