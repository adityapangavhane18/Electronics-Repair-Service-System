import gspread
from oauth2client.service_account import ServiceAccountCredentials

def push_to_sheet(data_dict):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open('ServiceRequests').worksheet('Requests')
        sheet.append_row([
            data_dict.get('name'),
            data_dict.get('serial_number'),
            data_dict.get('product_name'),
            data_dict.get('date_of_purchase'),
            data_dict.get('fault_description'),
            data_dict.get('status'),
            data_dict.get('submitted_at')
        ])
    except Exception as e:
        print("Google Sheets Error:", e)