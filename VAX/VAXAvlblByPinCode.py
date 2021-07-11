import winsound, json, time
import requests
import datetime as dt

pincodes = ['500033', '500034', '500082', '500019', '500081']

today = dt.datetime.now()
if today.hour > 8:
    today = today + dt.timedelta(days=1)
today = today.strftime('%d-%m-%Y')
print(f"Searching for date: {today}")

while True:
    for pincode in pincodes:
        api_url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={today}"
        try:
            res = requests.get(api_url)

            if res.status_code == 200:
                results = res.json()
                for result in results['sessions']:
                    if (result['available_capacity_dose1'] > 1) \
                        and (result['min_age_limit'] == 18):
                        print("\n")
                        print(f"{dt.datetime.now()}")
                        print(f"name: {result['name']}")
                        print(f"Available: {result['available_capacity_dose1']}")
                        print(f"Vaccine: {result['vaccine']}")
                        print(f"{pincode = }")
                        print(f"~"*80)
                        winsound.Beep(1000, 2000)
            else:
                print(f"Unexpected Response: {res.status_code}")
        except Exception as e:
            print(e)
            
    print("* ", end='', flush=True)
    time.sleep(30)
