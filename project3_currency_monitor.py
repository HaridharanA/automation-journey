import requests 
import datetime as dt
import schedule as sc
import time 

API_KEY = "236a051230001118f3c76047"


url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/INR"



def get_currency_details():
     response = requests.get(url)
     data = response.json()

    
     currency_dict = {}
     print(dt.datetime.now().strftime("%I :%M : %S %p"))

     
     print("All currency values are against INR ")

     USD = round(1/data["conversion_rates"]["USD"],2)
     EUR = round(1/data["conversion_rates"]["EUR"],2)
     GBP = round(1/data["conversion_rates"]["GBP"],2)
     JPY = round(1/data["conversion_rates"]["JPY"],2)
     AED  = round(1/data["conversion_rates"]["AED"],2)

     currency_dict["USD"] = round(USD,2)
     currency_dict["EUR"] =  round(EUR,2)
     currency_dict["GBP"] = round(GBP,2)
     currency_dict["JPY"] = round(JPY,2)
     currency_dict["AED"] = round(AED,2) 

     print(f"1 USD = {USD} INR ")
     print(f"1 EUR = {EUR} INR")
     print(f"1 GBP = {GBP} INR")
     print(f"1 JPY = {JPY} INR")
     print(f"1 AED = {AED} INR")
     print()
     print("-"*55)
     print()
     timestamp = dt.datetime.now().strftime("%I :%M : %S %p")
     if USD > 95 or USD < 90:
        print("!!!Alert!!!")
        print(f"*** 1 USD = {USD} INR ", end =" ***") 
        print()

     with open("currency_log.txt","a") as f:
          f.write(f"\n {timestamp}")
          f.write(f"\n1 USD = {USD} INR ")
          f.write(f"\n1 EUR = {EUR} INR")
          f.write(f"\n1 GBP = {GBP} INR")
          f.write(f"\n1 JPY = {JPY} INR")
          f.write(f"\n1 AED = {AED} INR")
          f.write("\n")
          f.write("-"*15)
          f.write("\n")
          

     
                
     
          

get_currency_details()
sc.every(10).seconds.do(get_currency_details)

while True:
     sc.run_pending()
     time.sleep(1)     
     

    

