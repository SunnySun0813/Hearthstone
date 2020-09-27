import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('900x600+120+120')

def button_hover(e,a,b,c):
    my_button["bg"] = "white"
    status_label.config(text=1)

def button_hover_leave(e):
    my_button["bg"] = "SystemButtonFace"
    status_label.config(text="")

my_button = tk.Button(window, text='Click Me', font=("Helvetica", 28))
my_button.pack()
my_button.bind("<Enter>", lambda event, a=10, b=20, c=30: button_hover(a, b, c))
my_button.bind("<Leave>", button_hover_leave)

status_label = tk.Label(window, text='test', bd=1, anchor='e')
status_label.pack(ipady=2)

my_button1 = tk.Button(window, text='Click Me1', font=("Helvetica", 28))
my_button1.pack()
my_button1.bind("<Enter>", lambda event, a=10, b=20, c=30: button_hover(a, b, c))
my_button1.bind("<Leave>", button_hover_leave)



window.mainloop()

# import tkinter as tk
#
# class SampleApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.frame = tk.Frame(self)
#         self.frame.pack()
#         self.button = tk.Button(self.frame, text="click me",
#                              command=lambda a=1, b=2, c=3:
#                                 self.rand_func(a, b, c))
#         self.button.pack()
#         self.frame.bind("<Return>",
#                         lambda event, a=10, b=20, c=30:
#                             self.rand_func(a, b, c))
#         # make sure the frame has focus so the binding will work
#         self.frame.focus_set()
#
#     def rand_func(self, a, b, c):
#         print(a)
#         print(b)
#         print(c)
#
#         # print "self:", self, "a:", a, "b:", b, "c:", c
#         # print (a+b+c)
#
# app = SampleApp()
# app.mainloop()


