from .transformer import Transformer

import ast
import astor
import random

class BuiltinsTransformer(Transformer):
    
    class BuiltinsNodeTransformer(ast.NodeTransformer):
        def __init__(self, global_name):
            self.global_name = global_name
            super().__init__()
        
        def visit_Name(self, node):
            
            if not isinstance(node.ctx, ast.Load):
                return node
            
            if node.id not in __builtins__:
                return node
            
            return ast.Call(
                    func=ast.Name(id='getattr', ctx=ast.Load()),
                    args=[
                        ast.Subscript(
                            value=ast.Name(id=self.global_name, ctx=ast.Load()),
                            slice=ast.Constant(value='__builtins__'),
                            ctx=ast.Load()
                        ),
                        ast.Constant(value=node.id, kind=None)
                    ],
                    keywords=[]
            )
              
    def process(self, code: str) -> str:
            
        self.obfuscator.logger.info("PROCESSING", "Processing transformer", name="Builtins Obfuscation")
        global_name = f"_{self.obfuscator.random_ascii_string()}"

        try:
            tree = ast.parse(code)
            tree = self.BuiltinsNodeTransformer(global_name).visit(tree)
            ast.fix_missing_locations(tree)
            processed_code = astor.to_source(tree)
            
            final_code = f"{global_name} = eval(\"globals\")()\n{processed_code}"
            return final_code

        except Exception as e:
            self.obfuscator.logger.error("PROCESSING", 
                                       f"Error processing builtins transformation: {str(e)}",
                                       exc_info=True)
            raise