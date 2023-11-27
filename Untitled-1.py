import cv2
import matplotlib.pyplot as plt
# Resim Yükleme
image_path = 'C:/Users/KaraogLaN/Desktop/Yüksek Lisans/kara.png'
image = cv2.imread(image_path)
# Gauss düşük geçiren filtre uygulama
kernel_size = 4000  # Filtre boyutu
sigma = 200  # Standart sapma
# Gaussian filtreyi oluştur
gaussian_filter = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_filter = gaussian_filter * gaussian_filter.T 
filtered_image = cv2.filter2D(image, -1, gaussian_filter)
# Görüntü ve filtre çizimi
plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(1, 3, 3), plt.imshow(gaussian_filter, cmap='gray'), plt.title('Gaussian Filter')
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
# Resim Yükleme
image_path = '/Users/ufukdemirtas/Desktop/GoruntuIisleme/04/processed_image.png'
image = cv2.imread(image_path)
# Gauss düşük geçiren filtre uygulama
kernel_size = 4000  # Filtre boyutu
sigma = 200  # Standart sapma
# Gaussian filtreyi oluştur
gaussian_filter = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_filter = gaussian_filter * gaussian_filter.T 
filtered_image = cv2.filter2D(image, -1, gaussian_filter)
# Görüntü ve filtre çizimi
plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(1, 3, 3), plt.imshow(gaussian_filter, cmap='gray'), plt.title('Gaussian Filter')
plt.show()