import tkinter as tk
from tkinter import messagebox, filedialog

# Caesar Cipher function
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():
            encrypted += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            encrypted += char
    return encrypted

# Encrypt Text
def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    shift_val = shift_entry.get().strip()
    
    if not shift_val.isdigit():
        messagebox.showerror("Invalid Shift", "Shift must be a numeric value.")
        return
    
    shift = int(shift_val)
    result = caesar_encrypt(text, shift)
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state='normal')

# Copy to Clipboard
def copy_to_clipboard():
    result = result_text.get("1.0", tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Encrypted text copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "No encrypted text to copy.")

# Save to File
def save_to_file():
    result = result_text.get("1.0", tk.END).strip()
    if not result:
        messagebox.showwarning("Empty", "No encrypted text to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Files", "*.txt")],
                                             title="Save Encrypted Text")
    if file_path:
        with open(file_path, "w") as file:
            file.write(result)
        messagebox.showinfo("Saved", f"Encrypted text saved to:\n{file_path}")

# --- Dark Theme Colors ---
bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_bg = "#2e2e2e"
button_bg = "#3a3a3a"
highlight = "#4caf50"
font_main = ("Consolas", 12)

# GUI Setup
root = tk.Tk()
root.title("IMPLEMENTATION OF CEASER CIPHER")
root.geometry("620x500")
root.configure(bg=bg_color)

# Heading
heading = tk.Label(root, text="IMPLEMENTATION OF CEASER CIPHER", font=("Helvetica", 16, "bold"), bg=bg_color, fg=highlight)
heading.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg=bg_color)
frame.pack(pady=10)

tk.Label(frame, text="Enter Text:", font=font_main, bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w")
input_text = tk.Text(frame, height=4, width=60, bg=entry_bg, fg=fg_color, insertbackground="white")
input_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

tk.Label(frame, text="Shift Value:", font=font_main, bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="w")
shift_entry = tk.Entry(frame, width=10, bg=entry_bg, fg=fg_color, insertbackground="white")
shift_entry.grid(row=2, column=1, sticky="w", pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_text, bg=highlight, fg="black", font=font_main)
encrypt_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg=button_bg, fg=fg_color, font=font_main)
copy_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="Save to File", command=save_to_file, bg=button_bg, fg=fg_color, font=font_main)
save_button.grid(row=0, column=2, padx=5)

# Output Box
tk.Label(root, text="Encrypted Result:", font=font_main, bg=bg_color, fg=fg_color).pack()
result_text = tk.Text(root, height=4, width=60, bg=entry_bg, fg=fg_color, insertbackground="white")
result_text.pack(pady=5)
result_text.config(state='normal')

# Run App
root.mainloop()
