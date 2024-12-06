print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")  # Đặt màu nền cho cửa sổ

painter = turtle.Turtle()  # Tạo một "turtle" để vẽ
painter.fillcolor('blue')  # Đặt màu tô là màu xanh
painter.pencolor('blue')  # Đặt màu bút là màu xanh
painter.pensize(3)  # Đặt kích thước bút vẽ

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):  # Vẽ 4 cạnh hình vuông
        t.forward(s)  # Tiến lên một đoạn s
        t.left(90)  # Quay trái 90 độ để tạo góc vuông

# Vẽ hình xoay hình vuông
for i in range(1, 180):
    painter.left(18)  # Quay trái 18 độ
    drawsq(painter, 200)  # Vẽ hình vuông với cạnh dài 200

window.mainloop()  # Giữ cửa sổ mở
