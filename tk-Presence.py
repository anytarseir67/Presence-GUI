import tkinter as tk
from pypresence import Presence
import time
import sys

timer = False

root = tk.Tk()
root.configure(background='#525252')
root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50, weight=1)
root.columnconfigure([0, 1, 2, 3, 4, 5], minsize=50, weight=1)

client_id_label = tk.Label(master=root, text="client id", background='#525252', foreground='#ffffff')
client_id_label.grid(row=6, column=0)
client_id_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
client_id_entry.grid(row=7, column=0)

details_label = tk.Label(master=root, text="details", background='#525252', foreground='#ffffff')
details_label.grid(row=0, column=0)
state_label = tk.Label(master=root, text="state", background='#525252', foreground='#ffffff')
state_label.grid(row=0, column=1)

details_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
state_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')

small_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
large_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
small_label = tk.Label(master=root, text="small image", background='#525252', foreground='#ffffff')
small_label.grid(row=2, column=1)
large_label = tk.Label(master=root, text="large image", background='#525252', foreground='#ffffff')
large_label.grid(row=2, column=0)

small_tooltip_label = tk.Label(master=root, text="small image tooltip", background='#525252', foreground='#ffffff')
large_tooltip_label = tk.Label(master=root, text="large image tooltip", background='#525252', foreground='#ffffff')
small_tooltip_label.grid(row=4, column=1)
large_tooltip_label.grid(row=4, column=0)

small_tooltip_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
large_tooltip_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
small_tooltip_entry.grid(row=5, column=1)
large_tooltip_entry.grid(row=5, column=0)

button_1_text_label = tk.Label(master=root, text="button 1 text", background='#525252', foreground='#ffffff')
button_1_text_label.grid(row=0, column=3)
button_1_text_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
button_1_text_entry.grid(row=1, column=3)
button_1_url_label = tk.Label(master=root, text="button 1 url", background='#525252', foreground='#ffffff')
button_1_url_label.grid(row=2, column=3)
button_1_url_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
button_1_url_entry.grid(row=3, column=3)

button_2_text_label = tk.Label(master=root, text="button 2 text", background='#525252', foreground='#ffffff')
button_2_text_label.grid(row=0, column=4)
button_2_text_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
button_2_text_entry.grid(row=1, column=4)
button_2_url_label = tk.Label(master=root, text="button 2 url", background='#525252', foreground='#ffffff')
button_2_url_label.grid(row=2, column=4)
button_2_url_entry = tk.Entry(master=root, fg="black", bg="blue", background='#525252', foreground='#ffffff')
button_2_url_entry.grid(row=3, column=4)

timer_label = tk.Label(master=root, text="timer", background='#525252', foreground='#ffffff')
timer_label.grid(row=6, column=4)

def set_timer():
    global timer
    global timer_text
    if timer == False:
        timer = True
        timer_text.set("True")
    else:
        timer = False
        timer_text.set("False")
        
timer_text = tk.StringVar()
timer_text.set("False")
timer_button = tk.Button(master=root, textvar=timer_text, command=set_timer, background='#525252', foreground='#ffffff')
timer_button.grid(row=7, column=4)

def set_presence():
    global timer
    print(timer)
    RPC = Presence(client_id_entry.get(),pipe=0)
    RPC.connect()
    
    entrys = []
    entrys.append(details_entry.get())
    entrys.append(state_entry.get())
    entrys.append(large_entry.get())
    entrys.append(small_entry.get())
    entrys.append(button_1_text_entry.get())
    entrys.append(button_1_url_entry.get())
    entrys.append(button_2_text_entry.get())
    entrys.append(button_2_url_entry.get())
    entrys.append(large_tooltip_entry.get())
    entrys.append(small_tooltip_entry.get())
    for i, entry in enumerate(entrys):
        if entry == "":
            entrys[i] = None

    if entrys[4] != None and entrys[5] != None and entrys[6] != None and entrys[7] != None:
        entrys[4] = [{"label": entrys[4], "url": entrys[5]},{"label": entrys[6], "url": entrys[7]}]
        print(entrys[4])
        entrys.pop(5)
        entrys.pop(5)
        entrys.pop(5)
    elif entrys[4] != None and entrys[5] != None:
        entrys[4] = [{"label": entrys[4], "url": entrys[5]}]
        entrys.pop(5)
    elif entrys[6] != None and entrys[7] != None:
        entrys[4] = [{"label": entrys[6], "url": entrys[7]}]
        entrys.pop(5)
        entrys.pop(5)
        entrys.pop(5)
    else:
        entrys[4] = None
        entrys.pop(5)
        entrys.pop(5)
        entrys.pop(5)
    
    if timer == False:
        time_to_set = None
    else:
        time_to_set = time.time()
    
    RPC.update(details=entrys[0], state=entrys[1], large_image=entrys[2], small_image=entrys[3], large_text=entrys[5], small_text=entrys[6], buttons=entrys[4], start=time_to_set)

def close():
    sys.exit(0) 


details_entry.grid(row=1, column=0)
state_entry.grid(row=1, column=1)
small_entry.grid(row=3, column=1)
large_entry.grid(row=3, column=0)
btn = tk.Button(master=root, text="set rpc", command=set_presence, background='#525252', foreground='#ffffff')
btn.grid(row=1, column=2)
close_button = tk.Button(master=root, text="quit", command=close, background='#525252', foreground='#ffffff')
close_button.grid(row=3, column=2)

root.mainloop()
