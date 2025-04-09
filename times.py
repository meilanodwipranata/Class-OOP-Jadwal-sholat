import requests
import typing
import loguru
from requests import Response
from typing import Tuple

class Get_Location:
  '''mendapatkan (latitide , longitude) berdasarkan dari kota'''

  def __init__(self,):
    self.kota = "https://nominatim.openstreetmap.org/search?city="
    self.jadwal = "https://api.aladhan.com/v1/timings?latitude="

  def Latlon (self,city):
    url = self.kota+city+"&format=json"
    response = requests.get(url,headers={"User-Agent":"chrome"})
    data = response.json()
    return data[0]['lat'], data[0]['lon']
  
  def Jadwal(self,latitude:str ,longitude:str)-> dict:
    url = self.jadwal+latitude+"&longitude="+longitude +"&method=2"
    response = requests.get(url,headers={"User-Agent":"chrome"})
    data = response.json()
    return data["data"]["timings"]
  
  def Display_Jadwal(self, timings ):
        """
        Menampilkan waktu sholat ke layar.
        """
        print(f"Subuh: {timings['Fajr']} AM")
        print(f"Dzuhur: {timings['Dhuhr']} PM")
        print(f"Ashar: {timings['Asr']} PM")
        print(f"Maghrib: {timings['Maghrib']} PM")
        print(f"Isya: {timings['Isha']} PM")

class menjalankan:
  
    def __init__(self):
        self.finder = Get_Location()

    def run(self):
        again = True
        while again:
            try:
                city = input("Masukkan Nama Kota: ")
                lat, lon = self.finder.Latlon(city)
                timings = self.finder.Jadwal(lat, lon)
                self.finder.Display_Jadwal(timings)
                

            except Exception as e:
                print("ERROR")

            finally:
                repeat = input("Ingin mengulangi lagi? (y/n): ").lower()
                again = repeat in ["y", "yes"]
                

                

        print("Terima kasih telah menggunakan program ini.")
        print(Get_Location.jadwal(lat, lon))
        print(Get_Location.display_jadwal(timings))


if __name__ == "__main__":
    app = menjalankan()
    app.run()
