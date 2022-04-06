# type pip install qrcode to install qrcode in your terminal(cmd)
import qrcode
import time
print("==========QR Code Generator==========")
url = input("Enter URL: ")
qr = qrcode.make(f'{url}')
qrcode_name = input("Enter QR Code Name: ")
qr.save(f'{qrcode_name}.png')
for i in range(1, 100, 10):
    print(f"QR Code Generating...{i}")
    time.sleep(0.1)
print("\nQR Code Generated Successfully!")
print("QRcode will be saved in the same directory as this program.")
qr.show()


# ===================================
# Code by: John Reygun Danag