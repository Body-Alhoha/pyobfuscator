from core.obfuscator import PyObfuscator

class Transformer:
    def __init__(self, obfuscator : PyObfuscator) -> None:
        self.obfuscator = obfuscator

    def process(self, code : str) -> str:
        pass