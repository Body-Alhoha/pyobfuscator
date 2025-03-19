from core.utils.logger import Logger
import random, string
import os

class PyObfuscator:
    def __init__(self, input : str, output : str, transformers = []) -> None:
        self.input = input
        self.output = output
        self.logger = Logger()
        self.transformers = transformers

    def obfuscate(self):
        self.logger.info("CORE", "Starting obfuscator", input=self.input, output=self.output, long_form=True)
        for root, dirs, files in os.walk(self.input):
            for file in files:
                if file.endswith(".py"):
                    self.obfuscate_file(os.path.join(root, file), f"{self.output}\\{file}")

    def random_ascii_string(self, length=10):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def obfuscate_file(self, input : str, output : str):
        with open(input, "r", encoding="utf-8") as file:
            code = file.read()

        for transformerClass in self.transformers:
            transformer = transformerClass(self)
            code = transformer.process(code)

        with open(output, "w", encoding="utf-8") as file:
            file.write(code)
        
            