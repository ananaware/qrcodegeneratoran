# Import the library
import qrcode

# Enter the URL you want to encode
input_data = "https://www.bioxsystems.com/"

# Generate QR code
qr = qrcode.make(input_data)

# Save the QR code as an image file
qr.save("biox_qrcode.png")

# Show QR code on screen (optional)
qr.show()
