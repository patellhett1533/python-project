import qrcode

qr = qrcode.QRCode(version=1, box_size=50, border=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L)

qr.add_data("https://github.com/patellhett1533")
qr.make(fit=True)

img = qr.make_image(fill_color="yellow", back_color="blue")
img.save("qrcode.png")
