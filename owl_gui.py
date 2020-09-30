import tkinter as tk
import owl_lib
import converter
import ast

root = tk.Tk()
root.title("osu-wacom-linux-gui")
root.geometry("600x400+700+200")

user_input_area = tk.Entry(root)
user_input_x = tk.Entry(root)
user_input_y = tk.Entry(root)

def get_user_input():
    area = user_input_area.get()
    x = user_input_x.get()
    y = user_input_y.get()

    area_array = owl_lib.area()
    res_array = owl_lib.res()

    new_area = converter.area_proportion(ast.literal_eval(area), area_array[2])
    new_x = float(x)
    new_y = float(y)

    x_coor = area_array[2] * (float(new_area/100))
    y_coor = x_coor * res_array[1] / res_array[0]
    x_off  = (area_array[2] - x_coor) * (new_x/100)
    y_off  = (area_array[3] - y_coor) * (new_y/100)
    owl_lib.set_area(0 + x_off, 0 + y_off, x_coor + x_off, y_coor + y_off) 
    owl_lib.no_smoothing()
set_button = tk.Button(
    root, text="Set", 
    command=get_user_input
)

def rotate_y():
    owl_lib.rotate("y")
def rotate_n():
    owl_lib.rotate("n")
select = tk.IntVar()
tablet_rotate_yes = tk.Radiobutton(
    root, text="y", 
    command=rotate_y, variable=select, 
    value=1
)
tablet_rotate_no = tk.Radiobutton(
    root, text="n", 
    command=rotate_n, variable=select, 
    value=2
)

user_input_area.pack()
user_input_x.pack()
user_input_y.pack()
tablet_rotate_yes.pack()
tablet_rotate_no.pack()
set_button.pack()

root.mainloop()