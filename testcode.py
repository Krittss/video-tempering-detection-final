import tkinter as tk
from tkinter import filedialog
from ai_generated_detection import detect_ai_generated_content
from tampering_detection import detect_tampering

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Call detection methods based on user selection
        result = detect_ai_generated_content(file_path)
        result_label.config(text=f"AI Generated: {'Yes' if result else 'No'}")

app = tk.Tk()
app.title("Video Detection UI")

upload_button = tk.Button(app, text="Upload Video", command=open_file)
upload_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
