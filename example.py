import tkinter as tk
import tkinter.ttk as ttk
from popup import PopUp


class Application():
    def __init__(self):
        # Create root
        self.root = root = tk.Tk()

        button = ttk.Button(
            root,
            text="window 1",
            command=lambda: PopUp(self.root, 'window1', text="1st win",
                                  title="test title"))
        button.pack()

        button2 = ttk.Button(
            root,
            text="window 2",
            command=lambda: PopUp(self.root, '2ndwindow', text="2nd win"))
        button2.pack()

        root.mainloop()


MyApp = Application()
