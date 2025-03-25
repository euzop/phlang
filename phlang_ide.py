import sys
import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk
import tempfile

compiler_path = r"C:\Users\euzop\Downloads\proglang finals\phlang-compiler"
sys.path.append(compiler_path)

from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.codegen.generator import CodeGenerator
from src.error.error_handler import CompilerError

def compile_and_run(filename, args=None):
    try:
        start_time = time.time()
        
        with open(filename, 'r') as file:
            source_code = file.read()
        
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        code_generator = CodeGenerator(ast)
        python_code = code_generator.generate()
        
        compile_time = time.time() - start_time
        
        output_buffer = []
        original_stdout = sys.stdout
        
        class CaptureOutput:
            def write(self, text):
                output_buffer.append(text)
                original_stdout.write(text)
            def flush(self):
                original_stdout.flush()
        
        sys.stdout = CaptureOutput()
        
        try:
            exec(python_code, {})
            sys.stdout = original_stdout
            result = "".join(output_buffer) or "Matagumpay na naisagawa ang programa na walang output."
            result += f"\n\nOras ng pagkocompile: {compile_time:.4f} segundo"
            return result
        finally:
            sys.stdout = original_stdout
            
    except CompilerError as e:
        return f"Error sa pagkocompile: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

class LineNumbers(tk.Canvas):
    def __init__(self, parent, text_widget, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyPress>', self.on_key_press)
        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.text_widget.bind('<MouseWheel>', self.redraw)
        self.text_widget.bind('<<Modified>>', self.redraw)
        self.text_widget.bind('<Configure>', self.redraw)
        self.redraw()

    def on_key_press(self, event=None):
        self.redraw()

    def on_key_release(self, event=None):
        self.redraw()

    def redraw(self, event=None):
        self.delete("all")
        
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None: 
                break
            y = dline[1]
            linenum = i.split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#999999", font=("Consolas", 11))
            i = self.text_widget.index(f"{int(linenum) + 1}.0")

class DarkScrolledText(scrolledtext.ScrolledText):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(highlightbackground="#1e1e1e", highlightcolor="#1e1e1e")
        scrollbar = self.vbar
        scrollbar.configure(background="#333333", troughcolor="#1e1e1e", 
                           activebackground="#555555", borderwidth=0,
                           highlightbackground="#1e1e1e")

class LineNumberedText(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.bg = kwargs.get('bg', '#282c34')
        self.fg = kwargs.get('fg', '#f8f8f2')
        
        self.text = DarkScrolledText(self, *args, **kwargs)
        self.linenumbers = LineNumbers(self, self.text, width=35, 
                                       bg="#21252b", highlightthickness=0)
        
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<Tab>", self.handle_tab)
        self.text.bind("<Shift-Tab>", self.handle_shift_tab)
        
    def handle_tab(self, event):
        # Insert 4 spaces instead of tab character
        self.text.insert(tk.INSERT, "    ")
        return 'break'  # Prevent default tab behavior
        
    def handle_shift_tab(self, event):
        # Unindent current line
        current_line = self.text.get("insert linestart", "insert lineend")
        if current_line.startswith("    "):
            self.text.delete("insert linestart", "insert linestart + 4c")
        return 'break'  # Prevent default shift-tab behavior
    
    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)
        
    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)
        
    def see(self, *args, **kwargs):
        return self.text.see(*args, **kwargs)
        
    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)
        
    def config(self, *args, **kwargs):
        return self.text.config(*args, **kwargs)
        
    def configure(self, *args, **kwargs):
        return self.text.configure(*args, **kwargs)
        
    def pack(self, *args, **kwargs):
        super().pack(*args, **kwargs)
        
    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)
        
    def place(self, *args, **kwargs):
        super().place(*args, **kwargs)

class PHLangIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("PHLang IDE")
        self.root.geometry("1200x700")
        
        if os.name == 'nt':
            try:
                from ctypes import windll, byref, sizeof, c_int
                windll.uxtheme.SetWindowTheme(windll.user32.GetParent(root.winfo_id()), "DarkMode_Explorer", None)
                
                DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                set_window_attribute = windll.dwmapi.DwmSetWindowAttribute
                set_window_attribute(windll.user32.GetParent(root.winfo_id()), DWMWA_USE_IMMERSIVE_DARK_MODE, byref(c_int(1)), sizeof(c_int))
                
                myappid = 'com.phlang.ide.1.0'
                windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            except:
                pass
        
        self.set_icon()
        self.apply_dark_theme()
        self.filename = None
        self.update_title()
        self.create_menu()
        self.create_layout()
    
    def set_icon(self):
        icon_path = os.path.join(compiler_path, "phlang_icon.png")
        icon_paths = [
            icon_path,
            os.path.join(compiler_path, "phlang-compiler", "phlang_icon.png"),
            os.path.join(compiler_path, "..", "phlang_icon.png"),
            r"C:\Users\euzop\Downloads\proglang finals\phlang_icon.png"
        ]
        
        for path in icon_paths:
            if os.path.exists(path):
                try:
                    if os.name == 'nt' and path.lower().endswith('.png'):
                        icon_img = Image.open(path)
                        self.icon_photo = ImageTk.PhotoImage(icon_img)
                        self.root.iconphoto(True, self.icon_photo)
                        
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.ico') as icon_file:
                            icon_img.save(icon_file.name, format='ICO')
                            self.root.iconbitmap(icon_file.name)
                            self.ico_path = icon_file.name
                            
                            if os.name == 'nt':
                                try:
                                    from ctypes import windll
                                    windll.shell32.SetCurrentProcessExplicitAppUserModelID("phlang.ide")
                                except:
                                    pass
                    else:
                        icon_img = Image.open(path)
                        self.icon_photo = ImageTk.PhotoImage(icon_img)
                        self.root.iconphoto(True, self.icon_photo)
                    
                    return True
                except Exception as e:
                    print(f"Error setting icon: {e}")
        
        return False

    def apply_dark_theme(self):
        bg_color = "#2d2d2d"
        fg_color = "#f0f0f0"
        select_bg = "#505050"
        select_fg = "#ffffff"
        button_bg = "#404040"
        menu_bg = "#333333"
        menu_fg = "#f0f0f0"
        
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('.', background=bg_color, foreground=fg_color)
        style.configure('TFrame', background=bg_color)
        style.configure('TLabel', background=bg_color, foreground=fg_color)
        style.configure('TLabelframe', background=bg_color, foreground=fg_color)
        style.configure('TLabelframe.Label', background=bg_color, foreground=fg_color)
        
        style.configure('TButton', background=button_bg, foreground=fg_color)
        style.map('TButton', 
                background=[('active', select_bg), ('pressed', select_bg)],
                foreground=[('active', select_fg), ('pressed', select_fg)])
        
        style.configure('TPanedwindow', background=bg_color)
        
        style.configure('Vertical.TScrollbar', 
                       background=bg_color, 
                       troughcolor="#1e1e1e", 
                       arrowcolor=fg_color,
                       borderwidth=0)
        
        style.map('Vertical.TScrollbar',
                 background=[('active', select_bg), ('pressed', button_bg)],
                 arrowcolor=[('active', fg_color), ('pressed', fg_color)])
        
        style.configure('Horizontal.TScrollbar', 
                       background=bg_color, 
                       troughcolor="#1e1e1e", 
                       arrowcolor=fg_color,
                       borderwidth=0)
        
        style.map('Horizontal.TScrollbar',
                 background=[('active', select_bg), ('pressed', button_bg)],
                 arrowcolor=[('active', fg_color), ('pressed', fg_color)])
        
        self.root.configure(background=bg_color)
        
        self.root.option_add('*Menu.background', menu_bg)
        self.root.option_add('*Menu.foreground', menu_fg)
        self.root.option_add('*Menu.selectBackground', select_bg)
        self.root.option_add('*Menu.selectForeground', select_fg)
        self.root.option_add('*Menu.activeBackground', select_bg)
        self.root.option_add('*Menu.activeForeground', select_fg)
        
        self.root.option_add('*Scrollbar.background', bg_color)
        self.root.option_add('*Scrollbar.troughColor', "#1e1e1e")
        self.root.option_add('*Scrollbar.activeBackground', select_bg)
        self.root.option_add('*Scrollbar.borderWidth', 0)
        
    def update_title(self):
        if self.filename:
            base_filename = os.path.basename(self.filename)
            self.root.title(f"PHLang IDE - {base_filename}")
        else:
            self.root.title("PHLang IDE - Bagong File")

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Bago", command=self.new_file)
        file_menu.add_command(label="Buksan", command=self.open_file)
        file_menu.add_command(label="I-save", command=self.save_file)
        file_menu.add_command(label="I-save Bilang", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Umalis", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        run_menu = tk.Menu(menubar, tearoff=0)
        run_menu.add_command(label="Patakbuhin", command=self.run_code)
        menubar.add_cascade(label="Patakbuhin", menu=run_menu)
        
        self.root.config(menu=menubar)

    def create_layout(self):
        editor_bg = "#282c34"
        editor_fg = "#f8f8f2"
        editor_cursor = "#f8f8f2"
        editor_select_bg = "#44475a"
        output_bg = "#282c34"
        output_fg = "#f8f8f2"
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        editor_frame = ttk.LabelFrame(paned_window, text="PHLang Code Editor")
        paned_window.add(editor_frame, weight=3)  # Editor gets more space
        
        # Replace DarkScrolledText with LineNumberedText
        self.code_editor = LineNumberedText(editor_frame, 
                                          wrap=tk.WORD, 
                                          font=("Consolas", 11),
                                          bg=editor_bg, fg=editor_fg,
                                          insertbackground=editor_cursor,
                                          selectbackground=editor_select_bg,
                                          selectforeground=editor_fg)
        self.code_editor.pack(fill=tk.BOTH, expand=True)
        
        output_frame = ttk.LabelFrame(paned_window, text="Output")
        paned_window.add(output_frame, weight=2)  
        
        self.output_text = DarkScrolledText(output_frame, wrap=tk.WORD,
                                          font=("Consolas", 10),
                                          state="disabled",
                                          bg=output_bg, fg=output_fg,
                                          selectbackground=editor_select_bg,
                                          selectforeground=editor_fg)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        run_button = ttk.Button(button_frame, text="Patakbuhin ang Code", command=self.run_code)
        run_button.pack(side=tk.RIGHT, padx=5)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Handa")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def new_file(self):
        if self.code_editor.get("1.0", tk.END).strip():
            if not messagebox.askyesno("Bagong File", "Gusto mo bang itapon ang kasalukuyang mga pagbabago?"):
                return
        self.code_editor.delete("1.0", tk.END)
        self.filename = None
        self.update_title()
        self.status_var.set("Bagong File")

    def open_file(self):
        if self.code_editor.get("1.0", tk.END).strip():
            if not messagebox.askyesno("Buksan ang File", "Gusto mo bang itapon ang kasalukuyang mga pagbabago?"):
                return
                
        filepath = filedialog.askopenfilename(
            filetypes=[("PHLang Files", "*.ph"), ("Lahat ng Files", "*.*")]
        )
        
        if not filepath:
            return
            
        self.code_editor.delete("1.0", tk.END)
        
        with open(filepath, "r") as file:
            text = file.read()
            self.code_editor.insert("1.0", text)
            
        self.filename = filepath
        self.update_title()
        self.status_var.set(f"Nabuksan: {filepath}")

    def save_file(self):
        if not self.filename:
            return self.save_as_file()
            
        with open(self.filename, "w") as file:
            text = self.code_editor.get("1.0", tk.END)
            file.write(text)
            
        self.status_var.set(f"Na-save: {self.filename}")
        return True

    def save_as_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".ph",
            filetypes=[("PHLang Files", "*.ph"), ("Lahat ng Files", "*.*")]
        )
        
        if not filepath:
            return False
            
        self.filename = filepath
        self.update_title()
        return self.save_file()

    def run_code(self):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        
        if self.filename:
            self.save_file()
        else:
            if not self.save_as_file():
                return
        
        try:
            self.status_var.set("Nagko-compile at nagpapatakbo...")
            
            output = compile_and_run(self.filename)
            
            self.output_text.insert("1.0", output)
            self.status_var.set("Tapos na ang pagpapatakbo")
            
        except Exception as e:
            self.output_text.insert("1.0", f"Error: {str(e)}")
            self.status_var.set("Nabigo ang pagpapatakbo")
        
        self.output_text.config(state="disabled")
    
    def __del__(self):
        if hasattr(self, 'ico_path') and os.path.exists(self.ico_path):
            try:
                os.unlink(self.ico_path)
            except:
                pass

def main():
    root = tk.Tk()
    app = PHLangIDE(root)
    root.mainloop()

if __name__ == "__main__":
    main()