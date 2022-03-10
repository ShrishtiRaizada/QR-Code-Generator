
from textwrap import fill

#importing qrcode module
import qrcode 

#google python course

#object of class QRCode is created
qr=qrcode.QRCode(
    version=1,          #atttributes of objects
    box_size=30,
    border=10
)

#link of the site whose qrcode has to be created

data="https://developers.google.com/edu/python"

#data=input("Enter the url " )
#conversion of link into the qrcode
qr.add_data(data)
qr.make(fit=True)

#describing the features of qr code
img=qr.make_image(fill="black",back_color="white")
#saving qrcode in .png format
img.save('image.png')

#python projects

qr=qrcode.QRCode(
    version=1,         
    box_size=30,
    border=10
)


data1="https://www.dataquest.io/blog/python-projects-for-beginners/"

qr.add_data(data1)
qr.make(fit=True)

img=qr.make_image(fill="black",back_color="white")
img.save('image1.png')

#python questions

qr=qrcode.QRCode(
    version=1,         
    box_size=30,
    border=10
)


data2="https://www.javatpoint.com/python-interview-questions"

qr.add_data(data2)
qr.make(fit=True)

img=qr.make_image(fill="black",back_color="white")
img.save('image2.png')



