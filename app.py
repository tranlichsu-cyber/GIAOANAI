import eel
import sys
import os

# 1. Xác định đường dẫn thư mục chứa ứng dụng (quan trọng cho file .exe)
if getattr(sys, 'frozen', False):
    # Nếu đang chạy từ file .exe (đã đóng gói)
    app_folder = sys._MEIPASS
else:
    # Nếu đang chạy bằng lệnh python thường
    app_folder = os.path.dirname(os.path.abspath(__file__))

# 2. Khởi tạo Eel với thư mục gốc
eel.init(app_folder)

# 3. Chạy ứng dụng
if __name__ == '__main__':
    try:
        # Tên file HTML của bạn (phải để cùng thư mục với file này)
        file_html = 'tro-ly-giao-an-34-tinh.html'
        
        print(f"Đang khởi động ứng dụng từ: {app_folder}")
        
        # Bắt đầu mở giao diện web
        # mode='chrome' sẽ ưu tiên dùng Chrome/Edge có sẵn
        eel.start(file_html, size=(1200, 800))
        
    except Exception as e:
        print(f"Lỗi khởi động: {e}")
        # Giữ màn hình đen lại để đọc lỗi nếu có
        input("Nhấn Enter để thoát...")