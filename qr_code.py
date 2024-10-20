import qrcode as qr
img= qr.make("https://google.com ")
img= qr.make("my name is pratiksha")
img.save("My_google.png")