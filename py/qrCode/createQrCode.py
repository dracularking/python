# import the module
import pyqrcode

# define the data
data = 'oh man, this is amazing!'

# create qrcode
img = pyqrcode.create(data)

# save the qrcode in png format with proper scaling
img.png('qrCode.png', scale=10)


