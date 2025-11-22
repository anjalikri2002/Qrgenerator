import tkinter as tk
from tkinter import filedialog, messagebox
from qr_utils import generate_qr

def generate_gui():
    text = entry_text.get()
    filename = entry_filename.get() or "myqr.png"
    color = entry_color.get() or "black"
    bg_color = entry_bg.get() or "white"
    logo_path = logo_var.get()

    if not text:
        messagebox.showerror("Error", "Enter text or URL!")
        return

    if not filename.endswith(".png"):
        filename += ".png"

    try:
        path = generate_qr(text, filename, color, bg_color, logo_path)
        messagebox.showinfo("Success", f"QR Code saved at: {path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def browse_logo():
    path = filedialog.askopenfilename(
        title="Select Logo",
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    logo_var.set(path)


root = tk.Tk()
root.title("Professional QR Code Generator")
root.geometry("400x420")

tk.Label(root, text="Enter Text / URL").pack()
entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Output Filename").pack()
entry_filename = tk.Entry(root, width=40)
entry_filename.pack()

tk.Label(root, text="QR Color").pack()
entry_color = tk.Entry(root, width=40)
entry_color.pack()

tk.Label(root, text="Background Color").pack()
entry_bg = tk.Entry(root, width=40)
entry_bg.pack()

logo_var = tk.StringVar()
tk.Button(root, text="Select Logo", command=browse_logo).pack(pady=8)

tk.Button(root, text="Generate QR", command=generate_gui, bg="black", fg="white").pack(pady=10)

root.mainloop()
