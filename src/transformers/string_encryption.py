from .transformer import Transformer

import ast
import astor

from fernet import Fernet
import base64

def encrypt(value : str):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    return base64.b64encode(key + b":" + cipher.encrypt(value.encode())).decode()

def decrypt(value : str):
    key, encrypted_value = base64.b64decode(value.encode()).split(b":", 1)
    return Fernet(key).decrypt(encrypted_value).decode()

class StringEncryption(Transformer):

    class StringTransformer(ast.NodeTransformer):
        def __init__(self, name) -> None:
            self.name = name
            super().__init__()

        def visit_Constant(self, node):
            if isinstance(node.value, str):
                return ast.Call(
                    func=ast.Name(id=self.name, ctx=ast.Load()),
                    args=[ast.Constant(value=encrypt(node.value), kind=None)],
                    keywords=[]
                )
            return node
        
        def visit_Str(self, node):
            return ast.Call(
                func=ast.Name(id=self.name, ctx=ast.Load()),
                args=[ast.Str(s=encrypt(node.s))],
                keywords=[]
            )
              
    def process(self, code: str) -> str:
        self.obfuscator.logger.info("PROCESSING", "Processing transformer", name="String Encryption")
        function_name = self.obfuscator.random_ascii_string()

        try:
            tree = ast.parse(code)
            tree = self.StringTransformer(function_name).visit(tree)
            code = astor.to_source(tree)

            return f"""from fernet import Fernet
import base64
def {function_name}(a : str):
    b, c = base64.b64decode(a.encode()).split(b":", 1)
    return Fernet(b).decrypt(c).decode()
{code}
            """

        except Exception as e:
            self.obfuscator.logger.error("PROCESSING", 
                                       f"Error processing string encryption: {str(e)}",
                                       exc_info=True)
            raise