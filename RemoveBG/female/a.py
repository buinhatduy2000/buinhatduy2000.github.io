import os
import rembg
from tqdm import tqdm

# Đường dẫn thư mục chứa các hình ảnh
input_dir = "D:\\_MixiCorp-Data\\GTA V\\buinhatduy2000.github.io\\mixicity\\female\\bracelet"

# Tạo thư mục đầu ra với tên tương tự như thư mục đầu vào nhưng có thêm "_output" ở cuối
output_dir = input_dir.rstrip(os.sep) + "_output" + os.sep

# Tạo thư mục đầu ra nếu chưa tồn tại
os.makedirs(output_dir, exist_ok=True)

# Lặp qua từng tệp trong thư mục đầu vào
for filename in tqdm(os.listdir(input_dir), desc="Processing images"):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Xác định đường dẫn đầy đủ của hình ảnh đầu vào và đầu ra
        input_image_path = os.path.join(input_dir, filename)
        output_image_path = os.path.join(output_dir, filename)
        
        # Loại bỏ nền và lưu hình ảnh mới vào thư mục đầu ra
        with open(input_image_path, "rb") as f_in:
            with open(output_image_path, "wb") as f_out:
                f_out.write(rembg.remove(f_in.read()))

print("Đã xử lý tất cả các hình ảnh!")
