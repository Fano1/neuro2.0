from time import sleep, strftime
import flightradar24 as fl
from bs4 import BeautifulSoup
import requests
import webbrowser
from colorama import Fore, Back, Style
from speechRecog import RECORD_PPR as hear
import speech


api=fl.Api()


def get_key(val,dict):
    for key, value in dict.items():
         if val in value:
             return key
 
    return None

def get_aiport_iata(country):

    all_airports = api.get_airports()
    data = []

    for airport in all_airports['rows']:
        if airport["country"].lower() == country.lower():
            temp = {}
            temp["name"] = airport["name"]
            temp["iata"] = airport['iata']

            data.append(temp)
    return data



def get_airline_code(airline_name):
    all_airlines = api.get_airlines()
    results = []
    code = ''
    for airline in all_airlines['rows']:
        if airline["Name"].lower() == airline_name.lower():
            code = airline['Code']
    
    for airline in all_airlines['rows']:
        if airline["Name"].lower().find(airline_name.lower()) != -1:
            results.append(airline)

    if code != '':
        return code
    else:
        return results



def list_flights(arr_iata,dep_iata,year,month,date,hour):
    flights = []
    departure_time = []
    arrival_time = []
    base_url=f'https://www.flightstats.com/v2/flight-tracker/route/{arr_iata}/{dep_iata}/?year={year}&month={month}&date={date}&hour={hour}'
        
    res=requests.get(base_url)
    soup=BeautifulSoup(res.content,'html.parser')

    flights_data = soup.find_all('h2',class_='flights-list-bold-text flights-list-margined leftText')
    dept_time_data = soup.find_all('h2',class_='flights-list-bold-text flights-list-margined departureTimePadding')
    arr_time_data = soup.find_all('h2',class_='flights-list-light-text flights-list-margined')
           
    if len(flights_data) and len(dept_time_data) and len(arr_time_data) != 0:
        for flight in flights_data:
            flights.append(flight.text)

        for dep_time in dept_time_data:
            departure_time.append(dep_time.text)

        for arr_time in arr_time_data:
            arrival_time.append(arr_time.text)

        return flights, departure_time, arrival_time, base_url
    
    else:
        return None

def flight_status(flight_id,year,month,date):
    airline = flight_id.split()[0]   
    id = flight_id.split()[1]
    base_url=f'https://www.flightstats.com/v2/flight-tracker/{airline}/{id}?year=20{year}&month={month}&date={date}'
    print(base_url)
    res=requests.get(base_url)
    soup=BeautifulSoup(res.content,'html.parser')
    try:
        status=soup.find("div",class_='text-helper__TextHelper-sc-8bko4a-0 iicbYn').text
    except:
        status=soup.find("div",class_='text-helper__TextHelper-sc-8bko4a-0 iicbYn').text

            
    dep_city=soup.find_all("div",class_='text-helper__TextHelper-sc-8bko4a-0 efwouT')[0].text
    dep_airport=soup.find_all('div',class_='text-helper__TextHelper-sc-8bko4a-0 cHdMkI')[0].text
    
    arr_city=soup.find_all("div",class_='text-helper__TextHelper-sc-8bko4a-0 efwouT')[1].text
    arr_airport=soup.find_all('div',class_='text-helper__TextHelper-sc-8bko4a-0 cHdMkI')[1].text

    scheduled_dep_time=soup.find_all("div",class_='text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[0].text
    actual_dep_time=soup.find_all("div",class_='text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[1].text

    scheduled_arr_time=soup.find_all("div",class_='text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[2].text
    actual_arr_time=soup.find_all("div",class_='text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[3].text

    terminal_dep = soup.find_all("div",class_='ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[0].text
    gate_dep = soup.find_all("div",class_='ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[1].text

    terminal_arr = soup.find_all("div",class_='ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[2].text
    gate_arr = soup.find_all("div",class_='ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx')[3].text

    return status,arr_city,arr_airport,dep_city,dep_airport,scheduled_arr_time,actual_arr_time,scheduled_dep_time,actual_dep_time,terminal_arr,gate_arr,terminal_dep,gate_dep    
    

def main():
    print()
    print('''███████╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     
██╔════╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    
█████╗  ██║     ██║██║  ███╗███████║   ██║          ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝    
██╔══╝  ██║     ██║██║   ██║██╔══██║   ██║          ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    
██║     ███████╗██║╚██████╔╝██║  ██║   ██║          ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║    
╚═╝     ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
                                                                                                            ''')

    print()
    print(Fore.GREEN+"--"*40+Fore.RESET)
    
    print(Fore.CYAN+"""Tool By: Madhav :)"""+Fore.RESET)
    
    # print(Fore.GREEN+"--"*40+Fore.RESET)
    
    
   

        
    airline_name = "Air India"
    flight_id = 151
    result = get_airline_code(airline_name)
    if type(result) == str:
        code = result
    else:
        print(Fore.GREEN+"--"*40+Fore.RESET)
        print(Fore.GREEN+f"                    List Of Airlines Containing {airline_name}"+Fore.RESET)
        print(Fore.GREEN+"--"*40+Fore.RESET)
        for i in result:
            print(Fore.GREEN+f"Airline: {i['Name']}"+Fore.RESET)

    webbrowser.open(f"https://www.flightradar24.com/{code}{flight_id}")
    sleep(3)

            
        
if __name__=="__main__":
    text = hear()
    print(text)
    speech.speak("Certainly, Master Here is the live map update of the Flight 151")
    main()
