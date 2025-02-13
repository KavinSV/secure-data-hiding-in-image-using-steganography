import cv2
import numpy as np

# Load Image
image_path = "boat.png"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Convert message and password to bytes
msg_bytes = msg.encode("utf-8")
pass_bytes = password.encode("utf-8")

# Store message length and password length
msg_length = len(msg_bytes)
pass_length = len(pass_bytes)

# Ensure data fits inside the image
max_capacity = (img.shape[0] * img.shape[1] * 3) - 6  # Reserve space for lengths
if msg_length + pass_length > max_capacity:
    print("Error: Data too large for this image.")
    exit()

# Store lengths in first 6 pixels (3 pixels for message length, 3 for password length)
img[0, 0] = [(msg_length >> 16) & 255, (msg_length >> 8) & 255, msg_length & 255]
img[0, 1] = [(pass_length >> 16) & 255, (pass_length >> 8) & 255, pass_length & 255]

# Flatten image for easier encoding
flat_img = img.flatten()

# Encode password first, then message
for i, byte in enumerate(pass_bytes):
    flat_img[i + 9] = byte  # Skip first 9 bytes (used for lengths)

for i, byte in enumerate(msg_bytes):
    flat_img[i + 9 + pass_length] = byte  # Skip password storage

# Reshape back to image format
img = flat_img.reshape(img.shape)

# Save Encrypted Image
cv2.imwrite("encryptedImage.png", img)

print("Message and passcode encrypted inside encryptedImage.jpg")
