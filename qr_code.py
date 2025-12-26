import qrcode

website_url = "https://youtu.be/gGmkCIeH3dY?si=jcPfc5kx-g5M1XPt"

version_number = input("Enter a number between 1-40 fort he qr code verison")
box_size_number = input("Enter a number between 1-10 for the pixels in each 'box' of the qr code")
border_number = input("Enter a number between 1-10 for the border size of the qr code")

qr = qrcode.QRCode(version = version_number, box_size = box_size_number, border = border_number)
qr.add_data(website_url)
qr.make()

img = qr.make/-image(fill_color = 'black', back_color = 'white')
img.save('youtube_qr.png')