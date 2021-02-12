import tkinter as tk
from pypresence import Presence
import sys

client_id = '''client id here'''
RPC = Presence(client_id,pipe=0)
RPC.connect()

root = tk.Tk()
root.configure(background='#525252')
root.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
root.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

label1 = tk.Label(master=root, text="details", background='#525252', foreground='#ffffff')
label1.grid(row=0, column=0)
label2 = tk.Label(master=root, text="state", background='#525252', foreground='#ffffff')
label2.grid(row=0, column=1)

entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
entry2 = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')

small = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
large = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
small_label = tk.Label(master=root, text="small image", background='#525252', foreground='#ffffff')
small_label.grid(row=2, column=1)
large_label = tk.Label(master=root, text="large image", background='#525252', foreground='#ffffff')
large_label.grid(row=2, column=0)

def conv():
    try:
        print(RPC.update(details=f"{entry.get()}", state=f"{entry2.get()}", large_image=f"{large.get()}", small_image=f"{small.get()}", large_text="i cant think of a tooltip :(", small_text="see other tooltip"))  # Set the presence
    except:
        try:
            print(RPC.update(details=f"{entry.get()}", state=f"{entry2.get()}", small_image=f"{small.get()}", large_text="i cant think of a tooltip :(", small_text="see other tooltip"))  # Set the presence
        except:
                try:
                   print(RPC.update(details=f"{entry.get()}", state=f"{entry2.get()}", large_image=f"{large.get()}", large_text="i cant think of a tooltip :(", small_text="see other tooltip"))  # Set the presence 
                except:
                    print(RPC.update(details=f"{entry.get()}", state=f"{entry2.get()}", large_text="i cant think of a tooltip :(", small_text="see other tooltip"))  # Set the presence 

def close():
    sys.exit(1) 


entry.grid(row=1, column=0)
entry2.grid(row=1, column=1)
small.grid(row=3, column=1)
large.grid(row=3, column=0)
btn = tk.Button(master=root, text="set rpc", command=conv, background='#525252', foreground='#ffffff')
btn.grid(row=1, column=2)
close_button = tk.Button(master=root, text="quit", command=close, background='#525252', foreground='#ffffff')
close_button.grid(row=3, column=2)

root.mainloop()
