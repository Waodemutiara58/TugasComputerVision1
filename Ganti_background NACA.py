import cv2
import numpy as np

# Cek versi OpenCV
print(f"OpenCV version: {cv2.__version__}")

# Load gambar
image = cv2.imread('/Users/user/afrizall/Naca gambar.jpg')

if image is None:
    print("Gambar tidak ditemukan. Periksa jalur file.")
else:
    # Ubah gambar ke ruang warna HSV untuk memudahkan deteksi warna biru
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Rentang untuk deteksi warna biru dalam ruang warna HSV
    lower_blue = np.array([100, 150, 0])   # Rentang bawah untuk biru
    upper_blue = np.array([140, 255, 255])  # Rentang atas untuk biru

    # Buat mask untuk warna biru
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Buat latar belakang merah (warna merah dalam format BGR)
    red_background = np.full_like(image, (0, 0, 255))  # Warna merah dalam format BGR

    # Mask untuk objek yang bukan latar belakang biru (foreground)
    non_blue_mask = cv2.bitwise_not(blue_mask)

    # Gabungkan gambar dengan latar belakang merah hanya pada area biru (background)
    background_part = cv2.bitwise_and(red_background, red_background, mask=blue_mask)  # Latar belakang merah
    foreground_part = cv2.bitwise_and(image, image, mask=non_blue_mask)  # Gambar asli untuk objek

    # Gabungkan latar belakang merah dengan objek yang tidak terpengaruh
    result = cv2.add(foreground_part, background_part)

    # Tampilkan hasil tanpa resizing (ukuran asli)
    cv2.imshow("Gambar dengan Latar Belakang Merah (Ukuran Normal)", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

