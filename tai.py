import numpy as np
import random
import cv2

#TACHE TAMAZOUZT ABDERRAHMANE
def sp_noise(image,prob):
  
    image_noise = np.zeros(image.shape,np.uint8) #salt and pepper noise
    rest = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x = random.random()
            if x < prob:
                image_noise[i][j] = 0
            elif x > rest:
                image_noise[i][j] = 255
            else:
                image_noise[i][j] = image[i][j]
    return image_noise

image = cv2.imread('image1.tif',0) # au niveau du gris
noise_img = sp_noise(image,0.07) #0.05 est la probabilité du bruit
cv2.imwrite('image_noise.tif', noise_img)
#FIN DU TACHE