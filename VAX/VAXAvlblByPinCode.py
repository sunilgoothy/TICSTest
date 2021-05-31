import winsound, json, time
import requests

pincodes = ['500033', '500034', '500082', '500019']

while True:
    for pincode in pincodes:
        api_url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date=01-06-2021"
        res = requests.get(api_url)

        if res.status_code == 200:
            results = res.json()
            for result in results['sessions']:
                if (result['available_capacity_dose1'] > 0) \
                    and (result['min_age_limit'] == 18):
                    print("\n")
                    print(f"name: {result['name']}")
                    print(f"Available: {result['available_capacity_dose1']}")
                    print(f"Vaccine: {result['vaccine']}")
                    print(f"{pincode = }")
                    print(f"~"*80)
                    winsound.Beep(1000, 2000)
        else:
            print(f"Unexpected Response: {res.status_code}")

    print("* ", end='', flush=True)
    time.sleep(30)
