print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import turtle, random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter.pensize(3)

for i in range(10):
    color = random.choice(colors)          # Lựa chọn màu ngẫu nhiên từ danh sách `colors`
    painter.pencolor(color)                # Đặt màu bút
    painter.circle(100)                    # Vẽ một hình tròn với bán kính 100
    painter.right(30)                      # Quay phải 30 độ
    painter.left(60)                       # Quay trái 60 độ
    painter.setposition(0, 0)              # Đưa con trỏ về vị trí (0, 0)
