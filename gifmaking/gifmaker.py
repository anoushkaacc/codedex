import imageio.v3 as iio

#use actual full path in system while running this code
filenames = [r'cat_image1.jpg', r'cat_image2.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('cat.gif', images, duration = 100, loop = 0)
