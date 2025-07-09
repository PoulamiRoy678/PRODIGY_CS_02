import cv2
import numpy as np

def encrypt_image(image_path, key):
    img = cv2.imread(image_path)
    encrypted_img = cv2.bitwise_xor(img, key)
    return encrypted_img

def decrypt_image(encrypted_img, key):
    decrypted_img = cv2.bitwise_xor(encrypted_img, key)
    return decrypted_img

# Example usage
key = 123  # secret key
image_path = "input.jpg"

# Encrypt
encrypted = encrypt_image(image_path, key)
cv2.imwrite("encrypted.jpg", encrypted)

# Decrypt
decrypted = decrypt_image(encrypted, key)
cv2.imwrite("decrypted.jpg", decrypted)
