import turtle

# Khởi tạo danh sách màu sắc
colors = ["red", "green", "blue"]

# Tạo đối tượng turtle
painter = turtle.Turtle()
painter.speed(0)  # Tăng tốc độ vẽ để vẽ nhanh hơn
painter.pensize(2)  # Đặt độ dày bút

# Vòng lặp để vẽ hoa văn
for angle in range(0, 360, 30):  # Góc từ 0 đến 360, bước nhảy là 30 độ
    painter.setheading(angle)  # Đặt hướng bút vẽ
    for color in colors:       # Lặp qua các màu
        painter.pencolor(color)  # Chọn màu
        painter.circle(100)      # Vẽ hình tròn bán kính 100

# Hoàn tất vẽ
turtle.done()
