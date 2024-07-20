import qrcode


qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)


data = "https://oneiro.az/az/"


qr.add_data(data)


qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("veb-sayt.png")