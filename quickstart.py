import requests
import json
import config

def main():
    id_sheet = "12dhcPy3Z4DoVNZHV7EJOQN4DlwaSxF0aK1Nim4BJSgo"
    include_grid_data = False
    url_request = f"{config.URL_SHEET_API}{id_sheet}?includeGridData={include_grid_data}&key={config.GOOGLE_API_KEY}"
    sheets_name = []

    res = requests.get(url_request)

    # res_json = res.json()

    print(res)
    # for sheet in res_json["sheets"] :
    #     sheets_name.append(sheet['properties']['title'])

    # print(sheets_name)

    with open('test.json','w') as fp:

        json.dump(res.json(), fp)

if __name__ == '__main__':
    main()