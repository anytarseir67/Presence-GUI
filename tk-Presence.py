import tkinter as tk
from pypresence import Presence

client_id = '''client id here'''
RPC = Presence(client_id,pipe=0)
RPC.connect()

root = tk.Tk()
root.rowconfigure([0, 1, 2], minsize=50, weight=1)
root.columnconfigure([0, 1, 2], minsize=50, weight=1)

label1 = tk.Label(master=root, text="details")
label1.grid(row=0, column=0)
label2 = tk.Label(master=root, text="state")
label2.grid(row=0, column=1)

entry = tk.Entry(master=root, fg="black", bg="blue")
entry2 = tk.Entry(master=root, fg="black", bg="blue")
def conv():
    print(RPC.update(details=f"{entry.get()}", state=f"{entry2.get()}", large_image="test_img", small_image="py", large_text="secret toast", small_text="le language"))  # Set the presence

entry.grid(row=1, column=0)
entry2.grid(row=1, column=1)

btn = tk.Button(master=root, text="set rpc", command=conv)
btn.grid(row=2, column=0)

root.mainloop()
