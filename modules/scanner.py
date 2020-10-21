import qrtools
import os

# scan QR code using a web cam
def scan_qr():
    # take an image
    os.system("fswebcam -r 1280x720 --no-banner temp.png")
    
    # decode QR
    qr = qrtools.QR()
    qr.decode("temp.png")
    
    return qr.data

scan_qr()
