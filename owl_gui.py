import tkinter as tk
import owl_lib
import converter
import ast

# 視窗設定

root = tk.Tk()
root.title("osu-wacom-linux-gui")
root.geometry("600x400+700+200")

# 實體化 Entry Box

user_input_area = tk.Entry(root)
user_input_x = tk.Entry(root)
user_input_y = tk.Entry(root)

# 建立繪圖板 data array

area_array = owl_lib.area()
res_array = owl_lib.res()

# Set Button 動作

def get_user_input():
    area = user_input_area.get()
    x = user_input_x.get()
    y = user_input_y.get()

# 轉換輸入值(str -> float)

    new_area = converter.area_proportion(ast.literal_eval(area), area_array[2])
    new_x = float(x)
    new_y = float(y)

# 建立設定參數

    x_coor = area_array[2] * (float(new_area/100))
    y_coor = x_coor * res_array[1] / res_array[0]
    x_off  = (area_array[2] - x_coor) * (new_x/100)
    y_off  = (area_array[3] - y_coor) * (new_y/100)

# 設定

    owl_lib.set_area(0 + x_off, 0 + y_off, x_coor + x_off, y_coor + y_off) 
    owl_lib.no_smoothing()

# 實體化 Set Button

set_button = tk.Button(
    root, text="Set", 
    command=get_user_input
)

# rotate 設定

def rotate_y():
    owl_lib.rotate("y")

def rotate_n():
    owl_lib.rotate("n")

select = tk.IntVar()

# 實體化 Radiobutton

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

# 元件擺放

user_input_area.grid(row=0, column=1)
user_input_x.grid(row=1, column=1)
user_input_y.grid(row=2, column=1)
tablet_rotate_yes.grid(row=1, column=2)
tablet_rotate_no.grid(row=2, column=2)
set_button.grid(row=3, column=1)

# 實體化視窗

root.mainloop()
