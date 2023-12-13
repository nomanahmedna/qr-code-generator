import segno

qrcode = segno.make_qr("https://www.facebook.com/")
qrcode.save("basic_qrcode.png",scale=10)
