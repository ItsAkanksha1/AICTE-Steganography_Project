import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found.")
    exit()

# Get passcode from user
pas = input("Enter passcode for decryption: ")

# Load stored passcode
try:
    with open("passcode.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Error: Passcode file not found.")
    exit()

# Character mapping
c = {i: chr(i) for i in range(255)}

# Verify passcode
if pas == stored_password:
    message = ""
    n, m, z = 0, 0, 0
    while True:
        char_val = img[n, m, z]
        if char_val == 0:  # Stop at delimiter '\0'
            break
        message += c[char_val]
        z = (z + 1) % 3  # Cycle through RGB channels
        if z == 0:
            m += 1
        if m >= img.shape[1]:
            n += 1
            m = 0
        if n >= img.shape[0]:  # Prevents infinite loops if image is too small
            break

    print("Decrypted message:", message)
else:
    print("Authentication failed: Incorrect passcode.")
