import cv2
import numpy as np

# Load Encrypted Image
encrypted_image_path = "encryptedImage.png"
img = cv2.imread(encrypted_image_path)

if img is None:
    print("Error: Encrypted image not found.")
    exit()

# Read lengths from first 6 pixels
msg_length = (img[0, 0, 0] << 16) + (img[0, 0, 1] << 8) + img[0, 0, 2]
pass_length = (img[0, 1, 0] << 16) + (img[0, 1, 1] << 8) + img[0, 1, 2]

# Sanity check
if msg_length == 0 or pass_length == 0 or msg_length + pass_length > 10000:
    print("Error: Data length incorrect. Decryption failed.")
    exit()

# Flatten image for easier extraction
flat_img = img.flatten()

# Extract password and message bytes
pass_bytes = bytes(flat_img[9:9 + pass_length])  # Skip first 9 bytes (length storage)
msg_bytes = bytes(flat_img[9 + pass_length:9 + pass_length + msg_length])

# Convert bytes back to string
saved_password = pass_bytes.decode("utf-8")
decrypted_msg = msg_bytes.decode("utf-8")

# Ask for the passcode
password = input("Enter passcode for Decryption: ")

if password != saved_password:
    print("YOU ARE NOT AUTHORIZED")
    exit()

print("Decryption message:", decrypted_msg)
