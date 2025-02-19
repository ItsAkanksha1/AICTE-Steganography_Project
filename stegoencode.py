import cv2
import os

# Load the image
img = cv2.imread("mypic.png")  # Use PNG to avoid compression artifacts
if img is None:
    print("Error: Image not found. Make sure the image path is correct.")
    exit()

# Get message and passcode
msg = input("Enter secret message: ") + '\0'  # Add delimiter to mark end
password = input("Enter a passcode: ")

# Character to integer mapping
d = {chr(i): i for i in range(255)}

# Encoding message into image
n, m, z = 0, 0, 0
for char in msg:
    if n >= img.shape[0] or m >= img.shape[1]:  # Ensure we don't exceed image size
        print("Error: Image is too small for this message.")
        exit()
    img[n, m, z] = d[char]
    z = (z + 1) % 3  # Cycle through RGB channels
    if z == 0:
        m += 1
    if m >= img.shape[1]:
        n += 1
        m = 0

# Save encrypted image as PNG
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Open image on Windows

# Save passcode to a text file
with open("passcode.txt", "w") as f:
    f.write(password)

print("Message successfully hidden in 'encryptedImage.png'.")
