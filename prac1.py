import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")

btn = ctk.CTkButton(app, text="Submit")
btn.pack(pady=50)

app.mainloop()