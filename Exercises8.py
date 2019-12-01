import statistics as st
import random
import math
from PIL import Image, ImageFilter, ImageDraw

# =============================================================================
#                                   Exercise 1
# =============================================================================

x = [3, 1.5, 4.5, 6.75, 2.25, 5.75, 2.25]

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))


# =============================================================================
#                                   Exercise 2
# =============================================================================

print( random.random())
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khalid', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('Orange Academy') )

items = [1, 5, 8, 9, 2, 4]
random.shuffle(items)
print(items)

print ( random.randint(20, 30) )
print ( random.randrange(1000, 2111, 5) )
print  ( random.uniform(10000, 11000))


# =============================================================================
#                                   Exercise 3
# =============================================================================

n= math.pi
print(n)

print(math.cos(200))
print(math.sin(30))
print(math.tan(180))

print(math.floor(10.8))
print(math.ceil(10.8))


# =============================================================================
#                                   Exercise 4
# =============================================================================

image1=Image.open("cat1.jpg")
print(image1.format, image1.size, image1.mode)
image1.show()
#------------------------------------------------------#

image_flip = image1.transpose(Image.FLIP_TOP_BOTTOM)
image_flip.show()

#----------------------------------------------------#

grayscale_image = image1.convert('L')
grayscale_image.show()

#---------------------------------------------------#

croped = image1.crop((0, 0, 50, 50))
croped.show()

#---------------------------------------------------#

draw = ImageDraw.Draw(image1)
draw.line((0, 0) + image1.size, fill=(255, 255, 255))
draw.line((0, image1.size[1], image1.size[0], 0), fill=(255, 255, 255))
draw.text((image1.size[0]/2 - image1.size[0]/2, image1.size[1]/2 + 20), "MoHaMeD", fill=(255, 255, 0))
image1.show()

#------------------------------------------------------#

newimage = image1.filter(ImageFilter.EDGE_ENHANCE)
newimage.show()

newimage1 = image1.filter(ImageFilter.FIND_EDGES)
newimage1.show()

newimage2 = image1.filter(ImageFilter.SMOOTH)
newimage2.show()

newimage3 = image1.filter(ImageFilter.SHARPEN)
newimage3.show()

#--------------------------------------------------------#

alpha = 0.5
imag1 = Image.open('cat1.jpg')
imag2 = Image.open('ball1.jpg').resize(imag1.size)
Image.blend(imag1, imag2, alpha).save("new.jpg".format(alpha))
im = Image.open("new.jpg")
im.show()

#----------------------------------------------------------#


newimage4 = image1.filter(ImageFilter.BLUR)
newimage4.show()

#----------------------------------------------------------#


sizes = (128, 128)

image1.thumbnail(sizes)

image1.show()


#-----------------------------------------------------#

image_rot_90 = image1.rotate(90)
image_rot_90.show()


#------------------------------------------------------#

img1 = Image.open('cat1.jpg')
img2 = Image.open('ball1.jpg')
mask = Image.open('mask.jpg')
mask = mask.resize(img1.size)

Image.composite(img1, img2, mask).save("image_composite.jpg")

img = Image.open("image_composite.jpg")
img.show()








































