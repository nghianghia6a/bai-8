import tkinter as tk

print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Programming Language Selector")

# Tạo biến lưu giá trị lựa chọn
v = tk.IntVar()
v.set(1)  # Khởi tạo lựa chọn ban đầu là Python

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm xử lý sự kiện khi chọn radio button
def ShowChoice():
    print(v.get())

# Tạo nhãn hướng dẫn
tk.Label(root, 
         text="Choose your favourite programming language:", 
         justify=tk.LEFT, 
         padx=20).pack()

# Tạo các nút indicator cho từng ngôn ngữ lập trình
for language, val in languages:
    tk.Radiobutton(root, 
                   text=language, 
                   indicatoron=0, 
                   width=20, 
                   padx=20, 
                   variable=v, 
                   command=ShowChoice, 
                   value=val).pack(anchor=tk.W)

# Hiển thị cửa sổ
root.mainloop()
