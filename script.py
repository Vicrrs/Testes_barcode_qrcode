import qrcode

img = qrcode.make("Testando o pacote")
img.save("Teste_script.png")

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4,)

qr.add_data("https://github.com/Vicrrs")
qr.make(fit=True)
img2 = qr.make_image(fill_color='black', back_color='white')
img2.save("arquivo02.png")
