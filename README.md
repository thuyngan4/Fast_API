# To-Do List API - FastAPI

## Mô tả dự án

Đây là một RESTful API đơn giản để quản lý danh sách công việc (To-Do List) được xây dựng bằng **FastAPI**.  
Dữ liệu được lưu trữ trong file JSON (`tasks_data.json`) giúp giữ dữ liệu bền vững mà không cần database.

## Các chức năng chính

- Tạo công việc mới
- Xem danh sách công việc với lọc trạng thái, sắp xếp theo độ ưu tiên và phân trang
- Xem chi tiết công việc theo ID
- Cập nhật công việc (title, mô tả, độ ưu tiên, trạng thái)
- Xóa công việc

## Công nghệ sử dụng

- Python 3.10+
- FastAPI
- Pydantic (validate dữ liệu)
- Uvicorn (server chạy API)
- JSON file (lưu trữ dữ liệu)

## Cài đặt và chạy project

1. Clone repo:

```bash
git clone <link-repo-github>
cd <tên-thư-mục>

2. Tạo môi trường ảo và cài dependencies:

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install fastapi uvicorn

3. Chạy server:   uvicorn main:app --reload
Server mặc định chạy tại: http://localhost:8000
