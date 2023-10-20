# import tkinter as tk
# import qrcode
# from PIL import Image, ImageTk
# from tkinter import filedialog
# import pyperclip

# def generate_qr_code():
#     url = url_entry.get()
#     if url:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(url)
#         qr.make(fit=True)
#         img = qr.make_image(fill_color="black", back_color="white")

#         qr_img = ImageTk.PhotoImage(image=Image.fromarray(img))
#         qr_label.config(image=qr_img)
#         qr_label.image = qr_img

# def save_qr_code():
#     file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
#     if file_path:
#         qr_img = qr_label.image
#         img = qr_img._PhotoImage__photo.zoom(2)
#         img.write(file_path)

# def copy_to_clipboard():
#     url = url_entry.get()
#     pyperclip.copy(url)

# # Create the main window
# root = tk.Tk()
# root.title("QR Code Generator")

# # URL input field
# url_label = tk.Label(root, text="Enter URL:")
# url_label.pack()
# url_entry = tk.Entry(root)
# url_entry.pack()

# # Generate QR code button
# generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
# generate_button.pack()

# # QR code display
# qr_label = tk.Label(root)
# qr_label.pack()

# # Save QR code button
# save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
# save_button.pack()

# # Copy URL to clipboard button
# copy_button = tk.Button(root, text="Copy URL to Clipboard", command=copy_to_clipboard)
# copy_button.pack()

# root.mainloop()


import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor(title="Choose a Color")[1]
    color_label.config(text=f"Selected Color: {color}")
    canvas.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Color Chooser")

urlPrompt=tk.Label(root, text="Enter the URL", width=50)
urlPrompt.pack()

# Create a button to open the color chooser dialog
choose_color_button = tk.Button(root, text="Choose Color", command=choose_color)
choose_color_button.pack(pady=10)

# Create a label to display the selected color
color_label = tk.Label(root, text="Selected Color: None")
color_label.pack()

# Create a canvas to display the selected color
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

root.mainloop()
