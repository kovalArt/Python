# Kovalenko Artem OOP version of weather forecast programm
import requests
import json
import datetime

class weatherForecast():
    
    def __init__(self, city):
        self.city = city
        
    __api_key = "eaeb261fb7267eafacbf234205cb0bb9"
    __api_endpoint = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    url = 0
    response = 0
    data = 0
    date = 0
    dict_var = {}
    

    def convert_temp(self, temp):
        k_temp = 273.15
        c_temp = str(round(temp - k_temp, 2))
        return c_temp + "C"

    def calculations(self):

        temperature = self.convert_temp(self.data["main"]["temp"])
        feels_like = self.convert_temp(self.data["main"]["feels_like"])
        max_temp = self.convert_temp(self.data["main"]["temp_max"])
        min_temp = self.convert_temp(self.data["main"]["temp_min"])

        self.dict_var["temp"] = str(temperature) 
        self.dict_var["feels_like"] = str(feels_like) 
        self.dict_var["max_temp"] = str(max_temp) 
        self.dict_var["min_temp"] = str(min_temp) 

    def display_forecast(self):
            
        try:
            print(self.city)
            
            self.url = self.__api_endpoint.format(self.city, self.__api_key)
            self.response = requests.get(self.url)
            self.response.raise_for_status()
            self.data = json.loads(self.response.text)
            self.date = datetime.datetime.now()


            self.calculations()
            print("=======================================")
            
            print("City:", self.city)
            print("Date:", self.date.strftime("%A %D %B %Y"))
            print("Weather description:", self.data["weather"][0]["description"])
            print("Temperature:", self.dict_var["temp"])
            print("Feels like:", self.dict_var["feels_like"])
            print("Wind speed:", self.data["wind"]["speed"], "m/s")
            print("Max. temperature:", self.dict_var["max_temp"])
            print("Min. temperature:", self.dict_var["min_temp"])

            print("=======================================")
        
        except requests.exceptions.HTTPError:
            print("Something is bad with HTTP request or input data")

if __name__ == "__main__":
    
    city_name =  input("Enter the city name: ")

    programm = weatherForecast(city_name)
    programm.display_forecast()
  
    




