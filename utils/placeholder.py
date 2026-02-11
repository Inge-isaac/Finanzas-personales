import tkinter as tk


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", color="grey", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg = self["fg"]

        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

        self.bind("<FocusIn>", self._focus_in)
        self.bind("<FocusOut>", self._focus_out)

    def _focus_in(self, e):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self["fg"] = self.default_fg

    def _focus_out(self, e):
        if not self.get():
            self.insert(0, self.placeholder)
            self["fg"] = self.placeholder_color
