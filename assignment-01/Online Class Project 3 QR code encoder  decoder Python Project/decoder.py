import cv2

def read_qr():
    filename = input("Enter the QR code image filename (example: myqr.png): ")

    # Image read karo
    img = cv2.imread(filename)
    if img is None:
        print("\n❌ Error: File not found ya incorrect filename.")
        return

    # QR Code Detector use karo
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print(f"\n✅ Decoded Data: {data}")
    else:
        print("\n❌ No QR code detected in the image.")

if __name__ == "__main__":
    read_qr()
