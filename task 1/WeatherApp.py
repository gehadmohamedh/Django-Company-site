import requests
class weather_clt:
    def get_current_temperature(self ,city):
        api_str = f"http://api.weatherapi.com/v1/current.json?key= 3ab4cc4ec197481e994115022230205&q={city}&aqi=no"
        response = requests.get(f"{api_str}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            res = response.json()
            return res.temp_c , res.temp_f
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
            
    def get_temperature_after(self ,city, days, hour=None):
        api_str=f"http://api.weatherapi.com/v1/forecast.json?key= 3ab4cc4ec197481e994115022230205&q={city}&days={days}&hour={hour}&aqi=no&alerts=no"
        response = requests.get(f"{api_str}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            res = response.json()
            return res["forecast"]["forecastday"][0]["hour"][0]["temp_c"] ,res["forecast"]["forecastday"][0]["hour"][0]["temp_f"] 
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
            
    def get_lat_and_long(self ,city):
        api_str = f"http://api.weatherapi.com/v1/current.json?key= 3ab4cc4ec197481e994115022230205&q={city}&aqi=no"
        response = requests.get(f"{api_str}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            res = response.json()
            return res.lang , res.lat
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

clt = weather_clt()
print (clt.get_temperature_after("London", 2, 5))