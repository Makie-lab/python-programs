import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("7_2_Activity.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS bookmark_tb(
    Bk_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    URL TEXT NOT NULL  
    )        
    """)

conn.commit()

def add_bookmark():
    win = tk.Toplevel()
    win.title("Add Bookmark")
    win.geometry("400x200")

    tk.Label(win, text="Bookmark Title:").grid(row=0, column=0, padx=10, pady=10)
    title_entry = tk.Entry(win)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(win, text="Bookmark URL:").grid(row=1, column=0, padx=10, pady=10)
    url_entry = tk.Entry(win)
    url_entry.grid(row=1, column=1, padx=10, pady=10)

    def save_bookmark():
        title = title_entry.get()
        url = url_entry.get()
        cur.execute("""
            INSERT INTO bookmark_tb (Title, URL) VALUES (?, ?)""", 
            (title, url)
        )

        if not title or not url:
            messagebox.showerror(
                    "Error",
                    "Please enter a valid bookmark ID."
                    )

        conn.commit()
        list_bookmarks()
        win.destroy()

    tk.Button(win, text="Save", command=save_bookmark).grid(row=2, columnspan=2, pady=10)

    conn.commit()

def remove_bookmark():
    win = tk.Toplevel(window)
    win.title("Remove Bookmark")
    win.geometry("250x150")

    tk.Label(
        win,
        text="Enter Bookmark #:"
    ).pack(pady=10)

    id_entry = tk.Entry(win)
    id_entry.pack()

    def del_bookmark():
        try:
            selected_id = int(id_entry.get())

            cur.execute("SELECT * FROM bookmark_tb")
            bookmarks = cur.fetchall()

            if selected_id < 1 or selected_id > len(bookmarks):
                messagebox.showerror(
                    "Error",
                    "Invalid bookmark ID."
                )
                return
            bk_id = bookmarks[selected_id - 1][0]

            cur.execute(
                "DELETE FROM bookmark_tb WHERE Bk_ID = ?", 
                (bk_id,)
                )

            conn.commit()

            messagebox.showinfo(
            "Success",
            "Bookmark removed successfully!"
            )
            
            list_bookmarks()
            win.destroy()

        except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid bookmark ID."
                    )

    tk.Button(
        win,
        text="Delete",
        command=del_bookmark
    ).pack(pady=10)

def edit_bookmark():
    win = tk.Toplevel()
    win.title("Edit Bookmark")
    win.geometry("400x200")

    tk.Label(win, text="Bookmark Number:").grid(row=0, column=0, padx=10, pady=10)
    id_entry = tk.Entry(win)
    id_entry.grid(row=0, column=1)

    tk.Label(win, text="New Title:").grid(row=1, column=0, padx=10, pady=10)
    new_title = tk.Entry(win)
    new_title.grid(row=1, column=1)

    tk.Label(win, text="New URL:").grid(row=2, column=0, padx=10, pady=10)
    new_url = tk.Entry(win)
    new_url.grid(row=2, column=1)

    def save_edit():
        try:
            selected_id = int(id_entry.get())

            cur.execute("SELECT * FROM bookmark_tb")
            bookmarks = cur.fetchall()

            if selected_id < 1 or selected_id > len(bookmarks):
                messagebox.showerror(
                    "Error",
                    "Invalid bookmark ID."
                )
                return
            bk_id = bookmarks[selected_id - 1][0]

            cur.execute("""
                UPDATE bookmark_tb 
                SET Title = ?, URL = ? 
                WHERE Bk_ID = ?""", 
                (new_title.get(), new_url.get(), bk_id)
            )

            conn.commit()

            messagebox.showinfo(
            "Success",
            "Bookmark updated successfully!"
            )
            
            list_bookmarks()
            win.destroy()

        except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid bookmark number."
                    )

    btn_save = tk.Button(
        win,
        text="Save",
        command=save_edit
        )

    btn_save.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
        )

    print("Bookmark added successfully!")

def list_bookmarks():
    bookmark_list.delete(0, tk.END)  # Clear the listbox before populating

    cur.execute("SELECT * FROM bookmark_tb")
    bookmarks = cur.fetchall()

    if not bookmarks: 
        messagebox.showinfo(
            "Bookmarks",
            "No bookmarks found."
        )
        return bookmarks
    
    for i, bk in enumerate(bookmarks, start=1):
        bookmark_list.insert(
            tk.END, 
            f"({i}) {bk[1]} - {bk[2]}")

    return bookmarks

conn.commit()
print("Bookmarks (bookmarks dbm)")

window = tk.Tk()
window.title("Bookmarks")
window.geometry("500x600")

title = tk.Label(
    window, 
    text="Bookmarks",
    font=("Apple UI", 15, "bold")
    ).pack(pady=5)

title2 = tk.Label(
    window,
    text="Options",
    font=("Apple UI", 12, "bold")
    ).place(x=35, y=490)

btn_add = tk.Button(
    window,
    text="Add",
    command=add_bookmark
    ).place(x=50, y=520
)

btn_remove = tk.Button(
    window,
    text="Remove",
    command=remove_bookmark
    ).place(x=130, y=520)

btn_edit = tk.Button(
    window,
    text="Edit",
    command=edit_bookmark
    ).place(x=230, y=520)

btn_list = tk.Button(
    window,
    text="List Bookmarks",
    command=list_bookmarks
    ).place(x=310, y=520)

bookmark_list = tk.Listbox(
    window,
    width=50,
    height=25
    )
bookmark_list.place(x=25, y=50)


window.mainloop()
conn.close()

