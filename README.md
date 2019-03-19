# PopUp
## A module to quickly produce and manage basic popups in tkinter

Allows for the handling of multiple pop-up windows.
Each one is asigned a window_id.
If a popup with the specified window_id is already open, switch focus
and update the text/header to the new info.

Example use:
  ```python
  root = tk.Tk()

  PopUp(root,                     Parent window
        'window1',                window ID
         text="text",             text in popup
         heading="header text",   heading in popup
         center=False,            center window or not
         size="200x200")          set size of window
```

A working example can be found in "example.py"
