# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


def _on_key_pressed(event):
    text = f'Tecla {repr(event.char)} pressionada.'
    label['text'] = text


def _on_key_release(event):
    text = f'Tecla {repr(event.char)} liberada.'
    label['text'] = text


root = tk.Tk()
root.title(string='Janela principal')

width = round(number=root.winfo_screenwidth() / 2)
height = round(number=root.winfo_screenheight() / 2)
root.geometry(newGeometry=f'{width}x{height}')
root.minsize(width=width, height=height)

root.bind(sequence="<Key>", func=_on_key_pressed)
root.bind(sequence="<KeyRelease>", func=_on_key_release)

# Frame.
frame = tk.Frame(master=root)
frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

label = tk.Label(master=frame, text='Pressione qualquer tecla')
label.pack(expand=True, fill=tk.BOTH)

root.mainloop()