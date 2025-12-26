import qrcode

website_url = input("Enter the website URL you want to create a QR code for: ")

version_number = input("Enter a number between 1-40 for the qr code verison: ")
box_size_number = input("Enter a number between 1-10 for the pixels in each 'box' of the qr code: ")
border_number = input("Enter a number between 1-10 for the border size of the qr code: ")
background_color = input("Enter a color name or hex code for the background color of the qr code: ")
filler_color = input("Enter a color name or hex code for the filler color of the qr code: ")

qr = qrcode.QRCode(version = version_number, box_size = box_size_number, border = border_number)
qr.add_data(website_url)
qr.make()

img = qr.make_image(fill_color = filler_color, back_color = background_color)
img.save('myqrcode.png')