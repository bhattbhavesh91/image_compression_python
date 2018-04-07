from PIL import Image

filename = 'z1.jpg'
img = Image.open(filename)
dim = img.size

actualHeight = float(dim[1])
actualWidth  = float(dim[0])

if actualWidth > actualHeight:
    '''
    Image is horizontal
    '''
    maxHeight = 720.0
    maxWidth  = 1280.0
else:
	'''
	Image is vertical
	'''
    maxHeight = 1280.0
    maxWidth  = 720.0

imgRatio = actualWidth/actualHeight
maxRatio = maxWidth/maxHeight

if (actualHeight > maxHeight) or (actualWidth > maxWidth):
    if(imgRatio < maxRatio):
        imgRatio = maxHeight / actualHeight
        actualWidth = imgRatio * actualWidth
        actualHeight = maxHeight
        
    elif (imgRatio > maxRatio):
        imgRatio = maxWidth / actualWidth
        actualHeight = imgRatio * actualHeight
        actualWidth = maxWidth
    else:
        actualHeight = maxHeight
        actualWidth = maxWidth

resized_img = img.resize((int(actualWidth), int(actualHeight)), Image.ANTIALIAS)
resized_img.save(filename.split('.')[0]+'_resized'+filename.split('.')[1],optimize=True)
