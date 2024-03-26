import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL
url = 'https://www.carsome.id/beli-mobil-bekas/honda'

#Mengambil halaman web
response = requests.get(url)

#Test response success
if response.status_code == 20:
    print("Sukses memuat web")
else:
    print("Gagal memuat web")

#Parsing HTML
soup = BeautifulSoup(response.text, "html.parser")
print(type(soup))
print(soup.prettify())

# Akses tag yang menampung data nama dan harga kendaraan
cars = soup.find_all("div", class_="list-card__item")

# List informasi kendaraan
cars_data=[]

for car in cars:
    car_info=[]
    
    # Temukan semua tag <p> di dalam <div>
    p_tags = car.find_all('p')
    
    # Loop untuk mengambil teks dari setiap tag <p> di dalam <div>
    for p_tag in p_tags:
        text = p_tag.get_text(strip=True)  # Ambil teks dari tag <p> tanpa spasi tambahan
        car_info.append(text)  # Tambahkan teks ke dalam list car_info
    
    # Temukan tag <strong> di dalam <div>
    strong_tag = car.find('strong')
    
    # Cek apakah tag <strong> ditemukan
    if strong_tag:
        # Ambil teks dari tag <strong>
        price = strong_tag.get_text(strip=True)
    else:
        price = 'Harga tidak tersedia'
        
    # Tambahkan harga ke dalam list car_info
    car_info.append(price)
    
    # Tambahkan data mobil ke dalam list cars_data
    cars_data.append(car_info)

# Membuat dataframe dari list cars_data
df = pd.DataFrame(cars_data, columns=['Merek', 'Model', 'Harga'])

# Cetak dataframe
print(df)