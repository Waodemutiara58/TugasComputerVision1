import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat gambar
fig, ax = plt.subplots()

# Menambahkan latar belakang hitam
ax.add_patch(patches.Rectangle((0, 0), 1, 1, color='black'))  # Latar belakang hitam

# Menambahkan tiga persegi panjang untuk bendera
ax.add_patch(patches.Rectangle((0, 0.66), 1, 0.33, color='white'))  # Warna putih
ax.add_patch(patches.Rectangle((0, 0.33), 1, 0.33, color='blue'))   # Warna biru
ax.add_patch(patches.Rectangle((0, 0), 1, 0.33, color='red'))      # Warna merah

# Mengatur batas dan menghilangkan sumbu
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Menampilkan bendera
plt.show()