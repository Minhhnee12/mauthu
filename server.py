import socket
from threading import Thread
import memory_algorithms  # Nhớ thêm dòng này để import các thuật toán

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Nhận được yêu cầu: {request}")

    # Ví dụ xử lý yêu cầu đơn giản, bạn có thể phức tạp hơn bằng việc phân tích yêu cầu và gọi hàm tương ứng
    if request == 'best_fit':
        response = memory_algorithms.best_fit([100, 500, 200, 300, 600], [212, 417, 112, 426])
    elif request == 'first_fit':
        response = memory_algorithms.first_fit([100, 500, 200, 300, 600], [212, 417, 112, 426])
    elif request == 'worst_fit':
        response = memory_algorithms.worst_fit([100, 500, 200, 300, 600], [212, 417, 112, 426])
    else:
        response = "Yêu cầu không hợp lệ"

    client_socket.send(str(response).encode())
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)
print("Server bắt đầu trên cổng 9999")

while True:
    client_socket, addr = server.accept()
    print(f"Chấp nhận kết nối từ {addr}")
    client_handler = Thread(target=handle_client, args=(client_socket,))
    client_handler.start()