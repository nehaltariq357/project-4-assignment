import qrcode

def generate_qr():
    data = input("Enter the text or URL you want to encode: ")
    filename = input("Enter the filename to save (example: myqr.png): ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"\n✅ QR Code generated and saved as '{filename}' successfully!")

if __name__ == "__main__":
    generate_qr()
