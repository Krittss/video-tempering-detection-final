import tkinter as tk
from tkinter import filedialog, ttk
from ai_generated_detection import detect_ai_generated_content
from tampering_detection import detect_tampering

# Function to handle file upload and action
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
    if file_path:
        # Call detection methods based on user selection
        action = action_var.get()
        if action == "Detect AI-generated Content":
            result = detect_ai_generated_content(file_path)
            result_label.config(text=f"AI Generated: {'Yes' if result else 'No'}")
        elif action == "Detect Tampering":
            result = detect_tampering(file_path)
            result_label.config(text=f"Tampered: {'Yes' if result else 'No'}")

# Main Tkinter application window
app = tk.Tk()
app.title("Video Detection Interface")
app.geometry("400x200")

# File upload button
upload_button = tk.Button(app, text="Upload Video", command=open_file)
upload_button.pack(pady=10)

# Action selection dropdown
action_var = tk.StringVar(value="Detect AI-generated Content")
action_menu = ttk.Combobox(app, textvariable=action_var)
action_menu['values'] = ("Detect AI-generated Content", "Detect Tampering")
action_menu.pack(pady=10)

# Submit button
submit_button = tk.Button(app, text="Submit", command=open_file)
submit_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
