import winsound, json, time
import requests
import datetime as dt

# 581: Hyderabad
# 603: Rangareddy
dist_id = [581, 603]

today = dt.datetime.now()
if today.hour > 8:
    today = today + dt.timedelta(days=1)
today = today.strftime('%d-%m-%Y')
print(f"Searching for date: {today}")

while True:
    for id in dist_id:
        api_url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={id}&date={today}"
        # print(api_url)
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
                    print(f"pincode: {result['pincode']}")
                    print(f"Age: {result['min_age_limit']}")
                    print(f"~"*80)
                    # winsound.Beep(5000, 2000)
                    winsound.Beep(500, 500)
        else:
            print(f"Unexpected Response: {res.status_code}")

    print("* ", end='', flush=True)
    time.sleep(30)
