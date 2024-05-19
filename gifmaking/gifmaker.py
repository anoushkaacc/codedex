import imageio.v3 as iio

filenames = [r'C:\Users\anoushka chatterjee\python programs\gifmaking\cat_image1.jpg', r'C:\Users\anoushka chatterjee\python programs\gifmaking\cat_image2.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('cat.gif', images, duration = 100, loop = 0)