import tkinter as tk
from Controller.Main import controller


class GUI:

    def __init__(self):
        self.controller=controller()
        self.root = tk.Tk()
        self.root.title("Mr. Know All")
        # self.root.iconbitmap("./brain3.ico")

        self.colors = {
            "background_color": "#2C3E50",  # Light Black (Hex: #2C3E50)
            "foreground_color": "white",    # White
            "highlight_background": "#34495E",  # Navy Blue (Hex: #34495E)
            "highlight_color": "blue"
        }


        self.window_size()
        self.labels()

        self.langs={True:"English",False:"Hebrew"}
        self.lang_flag=True

        self.canvas_config()

        self.txt_buttons()
        self.text.config(state=tk.DISABLED)  # Disable the Text widget after inserting text


    def window_size(self):
        self.root.configure(bg=self.colors["background_color"])
        self.window_width = self.root.winfo_screenwidth() // 2
        self.window_height = self.root.winfo_screenheight() // 2
        self.window_width += self.window_width // 2
        self.window_height += self.window_height // 2
        self.window_width=int(self.window_width*1.1)
        self.window_height=int(self.window_height*1.1)
        self.root.geometry(f"{self.window_width}x{self.window_height}")

    def labels(self):

        self.label = tk.Label(self.root, text="Welcome to Mr. Know All!", font=("Comic Sans MS", 20),bg=self.colors["background_color"], fg=self.colors["foreground_color"])
        self.label.pack(pady=10)

        self.label2 = tk.Label(self.root, text="what do you want to know?", font=("Comic Sans MS", 12),bg=self.colors["background_color"], fg=self.colors["foreground_color"])
        self.label2.pack(pady=10)

    def canvas_config(self):
        w=self.window_width//2
        w+w//2
        w=int(w*1.3)
        h=self.window_height//2
        h+h//2
        h = int(h * 1.3)
        self.canvas = tk.Canvas(self.root, width=w, height=h,bg=self.colors["background_color"],highlightbackground=self.colors["highlight_background"],highlightcolor=self.colors["highlight_color"])
        self.canvas.pack()

        self.frame = tk.Frame(self.canvas,bg=self.colors["background_color"])
        self.canvas.create_window(0, 0, anchor=tk.NW, window=self.frame,width=w, height=h)

        self.text = tk.Text(self.frame, width=w, height=h, wrap=tk.WORD,font=("Arial", 14),bg=self.colors["background_color"], fg=self.colors["foreground_color"])
        self.text.pack(padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.frame, command=self.text.yview,bg=self.colors["background_color"], activebackground=self.colors["foreground_color"])
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.text.config(yscrollcommand=self.scrollbar.set)

    def txt_buttons(self):
        self.entry = tk.Entry(self.root, width=100,font=("Arial", 12))
        self.entry.pack(padx=10, pady=5)

        self.lang_button = tk.Button(self.root,width=7,height=1 ,text=self.langs[self.lang_flag], command=self.lang,font=("Arial", 12))
        self.lang_button.pack()

        self.send_button = tk.Button(self.root,width=10,height=2 ,text="Send", command=self.client_message,font=("Ariel", 12))
        self.send_button.pack(pady=5)

        self.root.bind('<Return>', self.client_message)

    def lang(self):
        self.lang_flag= not self.lang_flag
        self.lang_button.config(text=self.langs[self.lang_flag])
        self.controller.change_language()

    def client_message(self,event=None):
        self.text.config(state=tk.NORMAL)
        message = self.entry.get()
        self.text.insert(tk.END, f"You: {message}\n\n")
        self.text.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)
        ans= self.controller.query(message)
        self.server_answer(ans)

    def server_answer(self,ans):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, f"Me: {ans}\n\n")
        self.text.config(state=tk.DISABLED)
        self.text.see(tk.END)



    def main(self):
        self.root.mainloop()


