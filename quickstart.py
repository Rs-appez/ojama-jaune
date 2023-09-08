import requests
import json
import config


def get_json_sheet(id_sheet,include_grid_data=True):
    url_request = f"{config.URL_SHEET_API}{id_sheet}?includeGridData={include_grid_data}&key={config.GOOGLE_API_KEY}"
    res = requests.get(url_request)
    return res.json()

def update_json_sheet(id_sheet,include_grid_data=True):
    res_json = get_json_sheet(id_sheet,include_grid_data)
    with open('test.json','w') as fp:
        json.dump(res_json, fp)

def read_json_sheet(json_name):
    with open(json_name) as json_file:
        data = json.load(json_file)
    return data

def main():
    id_sheet = "12dhcPy3Z4DoVNZHV7EJOQN4DlwaSxF0aK1Nim4BJSgo"
    include_grid_data = True
    sheets_name = []

    # update_json_sheet(id_sheet,include_grid_data)

    res_json = read_json_sheet('test.json')

    for sheet in res_json["sheets"] :
        sheets_name.append(sheet['properties']['title'])
        for d in sheet['data']:
            for r in d['rowData']:
                print(r['values'])
                break
                for s in r['values']:
                    if 'effectiveValue' in s:
                        if 'stringValue' in s['effectiveValue']:
                            print(s['effectiveValue']['stringValue'])

                print('------------------')

    print(sheets_name)


if __name__ == '__main__':
    main()