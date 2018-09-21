import tkinter as tk
import get_posts
import good_read

def get_post(button):
    """Retrieve Expedia facebook posts and put in window"""
    listbox.delete(0, tk.END)
    post_list = get_posts.get_posts_in_json()
    for item in post_list:
        listbox.insert(tk.END, item["post"])

def get_goodread(button):
    """
    Retrieve Goodread Mark Twain Quotes and put in frame
    Check to see if the user submitted email and password are correct
    """
    listbox.delete(0, tk.END)
    url = 'https://www.goodreads.com/'
    br = good_read.open_page(url)
    login_success = good_read.user_login(br, e1.get(), e2.get())
    if login_success.response.url == url:
        listbox.insert(tk.END, "You successfully logged In")
    else:
        listbox.insert(tk.END, "The email/password you input is not valid")
    quote_list = good_read.get_quotes(e1.get(), e2.get())
    for item in quote_list:
        listbox.insert(tk.END, item["quote"])

"""
Initialized the GUI and all the buttons and fields
"""
root = tk.Tk()
root.geometry("600x500")

button = tk.Button(root, text="Get 8 latest Expedia Facebook Posts")
button.pack()
button.bind("<Button-1>", get_post)

L1 = tk.Label(root, text="Goodread Email")
L2 = tk.Label(root, text="Goodread Password")
e1 = tk.Entry(root)
e2 = tk.Entry(root)
L1.pack()
e1.pack()
L2.pack()
e2.pack()

listbox = tk.Listbox(root)
button2 = tk.Button(root, text="Get 10 most liked Mark Twain Quotes")
button2.pack()
button2.bind("<Button-1>", get_goodread)

listbox.pack()
listbox.config(width=0)
listbox.insert(tk.END, "Retrieved data shows here")

root.mainloop()
