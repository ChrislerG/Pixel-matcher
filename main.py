from tkinter import *

from PIL import Image, ImageFilter

from PIL import ImageTk 

def calcDistance(tuple1,tuple2):

  x1 = tuple1[0]

  y1 = tuple1[1]

  z1 = tuple1[2]

  x2 = tuple2[0]

  y2 = tuple2[1]

  z2 = tuple2[2]

  d = ((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

  return d 

print(calcDistance((1,2,3),(6,7,8)))

im1 = Image.open('image_A.jpeg','r')

print('Image A is an ocean')

width, height = im1.size

pixel_values = list(im1.getdata())

im1.close()

print() 

lengthA = len(pixel_values) 
print(lengthA) 

print(pixel_values[0:100])  

root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open("image_A.jpeg"))  

canvas.create_image(20, 20, anchor=NW, image=img)




root.after(5000,lambda:root.destroy())

root.mainloop() 


#Repeat Steps 4 and 5 for Image B.  

im2 = Image.open('image_B.jpeg','r')

print('Image B is an Forest')

width, height = im2.size

pixel_values2 = list(im2.getdata())

im2.close()

print()

lengthB = len(pixel_values2) 
print(lengthB) 

print(pixel_values2[0:100])  

root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open("image_B.jpeg"))  

canvas.create_image(20, 20, anchor=NW, image=img)




root.after(5000,lambda:root.destroy())

root.mainloop()


print('Would you like to have the computer guess mystery.jpeg or mystery2.jpeg?') 

image_C = input()


im3 = Image.open(image_C,'r')

width, height = im3.size

pixel_values3 = list(im3.getdata())

im3.close()

print()

lengthC = len(pixel_values3) 
print(lengthC) 

print(pixel_values3[0:100])  





lengths = [lengthA, lengthB, lengthC]

minimum = min(lengths)

pics = [pixel_values, pixel_values2, pixel_values3]

print(minimum) 


##############

holder = []

for i in range(len(pics)):
  holder = []
  for j in range(len(pics[i])): 
    if len(holder) < minimum:
    

      holder.append(pics[i][j])

  pics[i] = holder

    






#Step 11:Copy and paste the code below to test if all of the images now have the same amount of pixels. All three numbers printed should be the same.


for i in range(len(pics)):

  print(len(pics[i]))


#Step 12: Calculate the distances between Image A’s and the mystery image’s pixels, then the distance between Image B’s and the mystery image’s pixels. Add these distances to their respective lists. Do this by unscrambling the code below.


AC = [] 
BC = []

for i in range(len(pics[2])):

  dA = calcDistance(pics[2][i],pics[0][i]) 
  
  AC.append(dA)


  dB = calcDistance(pics[2][i],pics[1][i])

  

  BC.append(dB)







#Step 13: Determine if the distance between Image A and the mystery image is the shortest or the longest for each pixel. If the distance between Image A and the mystery image is the shortest, add a 1 to the AC_shortest list. Do this by unscrambling the code below.

AC_shortest = []

for i in range(len(AC)):

  if AC[i] < BC[i]:

    AC_shortest.append(0) 

  else:

    AC_shortest.append(1) 






#Step 14: Next, calculate the ratio of AC being the shortest distance to the total number of pixels. Do this by copying and pasting the code below:



result = sum(AC_shortest)/len(AC_shortest)


round(result)
print(result)
#Step 15: Using the result, write an if/else statement to determine if the image is an ocean or a forest. Your code should produce the two possible outputs below:

#Possible Output 1:

#Mystery Image is a forest because its pixels are  70 % similar to Image B


#Possible Output 2:

#Mystery Image is an ocean because its pixels are  96 % similar to Image A

if result - .6 > 0: 
  print('Mystery Image is an forest because its pixels are  96 % similar to Image A')

elif result - .6 < 0: 
  print('Mystery Image is a ocean because its pixels are  70 % similar to Image B')


#Step 16:

#Write code to display the Mystery Image. 

root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open(image_C))  

canvas.create_image(20, 20, anchor=NW, image=img)




root.after(5000,lambda:root.destroy())

root.mainloop()