from PIL import Image
import cv2
import numpy as np
import requests

# Resmi URL'den alıp boyutlandırma işlemi yapıyorsunuz
image_url = 'https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg'
response = requests.get(image_url, stream=True)
image = Image.open(response.raw)
image = image.resize((450, 250))

# Resmi Numpy dizisine dönüştürüyorsunuz
image_arr = np.array(image)

# Görüntüyü gri tonlamalı formata çeviriyorsunuz
grey = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüye Gauss bulanıklığı uyguluyorsunuz
blur = cv2.GaussianBlur(grey, (5, 5), 0)

# Bulanıklaştırılmış görüntüye genişletme işlemi uyguluyorsunuz
dilated = cv2.dilate(blur, np.ones((3, 3)))

# Genişletilmiş görüntüye morfolojik kapanma işlemi uyguluyorsunuz
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

# Araba tespiti için CascadeClassifier kullanıyorsunuz
car_cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(car_cascade_src)
cars = car_cascade.detectMultiScale(closing, 1.1, 1)

# Otobüs tespiti için CascadeClassifier kullanıyorsunuz
bus_cascade_src = 'Bus_front.xml'
bus_cascade = cv2.CascadeClassifier(bus_cascade_src)
bus = bus_cascade.detectMultiScale(grey, 1.1, 1)

# Her tespit edilen araba için dikdörtgen çiz ve say
cnt = 0
for (x, y, w, h) in cars:
    cv2.rectangle(image_arr, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cnt += 1

# Her tespit edilen otobüs için dikdörtgen çiz ve say
bus_cnt = 0
for (x, y, w, h) in bus:
    cv2.rectangle(image_arr, (x, y), (x + w, y + h), (0, 255, 0), 2)
    bus_cnt += 1

# Toplam tespit edilen araba ve otobüs sayısını yazdır
print(cnt, " cars found")
print(bus_cnt, " buses found")

# Çerçevelenmiş görüntüyü PIL Image formatına dönüştürüp gösteriyorsunuz
annotated_image = Image.fromarray(image_arr)
annotated_image.show()

# Kullanıcı bir tuşa bastığında pencereyi kapat
cv2.waitKey(0)
cv2.destroyAllWindows()

# Yeni resmi URL'den alıp boyutlandırma işlemi yapıyorsunuz
image_url2 = 'https://qph.fs.quoracdn.net/main-qimg-b5c4e39dcd48dddd9e609e6022f74d85'
response2 = requests.get(image_url2, stream=True)
image2 = Image.open(response2.raw)
image2 = image2.resize((450, 250))

# Yeni resmi Numpy dizisine dönüştürüyorsunuz
image_arr2 = np.array(image2)

# Yeni resmi gri tonlamalı formata çeviriyorsunuz
grey2 = cv2.cvtColor(image_arr2, cv2.COLOR_BGR2GRAY)

# Otobüs tespiti için CascadeClassifier kullanıyorsunuz
bus_cascade_src = 'Bus_front.xml'
bus_cascade = cv2.CascadeClassifier(bus_cascade_src)
bus = bus_cascade.detectMultiScale(grey2, 1.1, 1)

# Her tespit edilen otobüs için dikdörtgen çiz ve say
cnt = 0
for (x, y, w, h) in bus:
    cv2.rectangle(image_arr2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cnt += 1

# Toplam tespit edilen otobüs sayısını yazdır
print(cnt, " buses found")

# Çerçevelenmiş görüntüyü PIL Image formatına dönüştürüp gösteriyorsunuz
annotated_image2 = Image.fromarray(image_arr2)
annotated_image2.show()
