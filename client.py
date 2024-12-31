import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

# Gửi yêu cầu tới server (có thể thay đổi thành 'best_fit', 'first_fit' hoặc 'worst_fit')
request = 'best_fit'
client.send(request.encode())

# Nhận phản hồi từ server
response = client.recv(4096).decode()
print(f"Phản hồi từ server: {response}")