import qrcode
data = input("Enter text or URL to generate QR code: ")
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "White")

img.save("my_qr_code.png")
print("QR code generated successfully")
print("Saved as: my_qr_code.py")
     