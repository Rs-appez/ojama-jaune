import requests
import json


API_KEY = "AIzaSyBztEJZa5C-jBMvhk9ru-BKcR6gqDJvO_A"
URL = "https://sheets.googleapis.com/v4/spreadsheets/"
def main():

    sheets_name = []

    res = requests.get(URL+"12dhcPy3Z4DoVNZHV7EJOQN4DlwaSxF0aK1Nim4BJSgo"+f"?includeGridData=true&key={API_KEY}")

    # res_json = res.json()

    print(res)
    # for sheet in res_json["sheets"] :
    #     sheets_name.append(sheet['properties']['title'])

    # print(sheets_name)

    with open('test.json','w') as fp:

        json.dump(res.json(), fp)

if __name__ == '__main__':
    main()