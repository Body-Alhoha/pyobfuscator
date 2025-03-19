import colr
import time

class Logger:

    color_scheme = {
        'info': (76,121,234),
        'error': (175, 0, 0),
        'success': (101,165,8),
        'background': (68, 68, 68),
        'warning': (255, 108, 28),
        'text': (208, 208, 208),
    }

    show_time = True

    def __init__(self) -> None:
        pass

    
    def log(self, color : str, type : str, message : str, is_input : bool = False, **kwargs):
        if color not in self.color_scheme:
            raise ValueError(f"Color {color} not found in color scheme")
        message = colr.color(message, fore=self.color_scheme["text"])
        message = colr.color(type, fore=self.color_scheme[color]) + colr.color(" ● ", fore=self.color_scheme["background"]) + message

        if self.show_time:
            message = colr.color(f"{time.strftime('%H:%M:%S', time.localtime())} » ", fore=self.color_scheme["background"]) + message

        
        if len(kwargs) > 0:
            if kwargs.get("long_form", False):
                kwargs.pop("long_form")
                message_space = " " * (1 + len(type) + len(f"{time.strftime('%H:%M:%S', time.localtime())} » "))
                message += "\n"
                args = []
                for key in kwargs:
                    args.append(message_space + colr.color("→ ", fore=self.color_scheme["background"]) + colr.color(key, fore=self.color_scheme["text"]) + " [" + colr.color(kwargs[key], fore=self.color_scheme[color]) + "]")
                
                message += "\n".join(args)
            else:
                message += colr.color(" → ", fore=self.color_scheme["background"])
                args = []
                for key in kwargs:
                    args.append(colr.color(key, fore=self.color_scheme["text"]) + " [" + colr.color(kwargs[key], fore=self.color_scheme[color]) + "]")
                
                message += colr.color(" | ", fore=self.color_scheme["background"]).join(args)
        return input(message) if is_input else print(message)
    

    def info(self, type : str, message : str, **kwargs):
        self.log("info", type, message, **kwargs)
    
    def error(self, type : str, message : str, **kwargs):
        self.log("error", type, message, **kwargs)

    def warning(self, type : str, message : str, **kwargs):
        self.log("warning", type, message, **kwargs)
    
    def success(self, type : str, message : str, **kwargs):
        self.log("success", type, message, **kwargs)

    def prompt(self, type : str, message : str, **kwargs):
        return self.log("warning", type, message, True, **kwargs)