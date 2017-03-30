import datetime
import os

import requests
import xlsxwriter

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Refer": "https://www.carnival.com/"
}
codes = ["A", "BH", "BM", "NN", "C", "H", "M", "T"]


def get_total_pages(this_code):
    count_url = "https://www.carnival.com/bookingengine/api/search?exclDetails=false&layout=grid&numAdults=1" \
                "&numChildren=0&pageNumber=1&pageSize=8&showBest=true&sort=FromPrice&dest=" + this_code + \
                "&useSuggestions=true "
    count_page = session.get(count_url, headers=headers)
    root = count_page.json()
    results = root['results']
    return results['totalResults']


def preformated(unformated):
    splitter = unformated.split('-')
    day = splitter[2]
    month = splitter[1]
    year = splitter[0]
    final_date = '%s/%s/%s' % (month, day, year)
    return final_date


itineraries = []
all_sailings = []
all_ports = set()
sailing_codes = []


def get_destination(param):
    if param == 'A':
        return ['Alaska', 'A']
    elif param == 'BH':
        return ['Bahamas', 'BH']
    elif param == 'BM':
        return ['Bermuda', 'BM']
    elif param == 'NN':
        return ['Canada & New England', 'NN']
    elif param == 'C':
        return ['Caribbean', 'C']
    elif param == 'H':
        return ['Hawaii', 'H']
    elif param == 'M':
        return ['Mexico', 'M']
    elif param == 'T':
        return ['Panama Canal', 'T']


def get_vessel_id(vessel_na):
    if vessel_na == "Carnival Conquest":
        return "405"
    if vessel_na == "Carnival Sunshine":
        return "808"
    if vessel_na == "Carnival Glory":
        return "416"
    if vessel_na == "Carnival Legend":
        return "406"
    if vessel_na == "Carnival Miracle":
        return "426"
    if vessel_na == "Carnival Pride":
        return "398"
    if vessel_na == "Carnival Spirit":
        return "29"
    if vessel_na == "Carnival Triumph":
        return "30"
    if vessel_na == "Carnival Valor":
        return "436"
    if vessel_na == "Carnival Victory":
        return "31"
    if vessel_na == "CarnivalCelebration":
        return "33"
    if vessel_na == "Carnival Ecstasy":
        return "34"
    if vessel_na == "Carnival Elation":
        return "35"
    if vessel_na == "Carnival Fantasy":
        return "37"
    if vessel_na == "Carnival Fascination":
        return "37"
    if vessel_na == "Carnival Holiday":
        return "39"
    if vessel_na == "Carnival Imagination":
        return "40"
    if vessel_na == "Carnival Inspiration":
        return "41"
    if vessel_na == "Carnival Jubilee":
        return "683"
    if vessel_na == "Carnival Paradise":
        return "45"
    if vessel_na == "Carnival Sensation":
        return "46"
    if vessel_na == "Carnival Liberty":
        return "441"
    if vessel_na == "Carnival Freedom":
        return "555"
    if vessel_na == "Carnival Splendor":
        return "662"
    if vessel_na == "Carnival Dream":
        return "694"
    if vessel_na == "Carnival Magic":
        return "724"
    if vessel_na == "Carnival Breeze":
        return "739"
    if vessel_na == "Carnival Sunshine":
        return "808"
    if vessel_na == "Carnival Vista":
        return "930"

for code in codes:
    limit = get_total_pages(code)
    start_page = 1
    counter = 0
    url = "https://www.carnival.com/bookingengine/api/search?exclDetails=false&layout=grid&numAdults=2&numChildren=0&pageNumber=1&pageSize=" + str(
        limit) + "&showBest=true&sort=FromPrice&dest=" + code + "&useSuggestions=true"
    page = session.get(url, headers=headers)
    cruise_results = page.json()['results']
    print("Downloading sailings for destination:", code)
    for line in cruise_results['itineraries']:
        itineraries.append(line)
        counter += 1
    counter = 0
    for line in itineraries:
        brochure_name = line['regionName'] + " from " + line['departurePortName']
        cruise_line_name = "Carnival US"
        vessel_name = line['shipName']
        number_of_nights = line['dur']
        destination = get_destination(code)
        destination_name = destination[0]
        destination_code = destination[1]
        vessel_id = get_vessel_id(vessel_name)
        cruise_id = "2"
        itinerary_id = ""
        for sailing in line['sailings']:
            if sailing['sailingId'] in sailing_codes:
                continue
            else:
                sailing_codes.append(sailing['sailingId'])
            counter += 1
            departure_split = sailing['departureDate'].split('T')[0]
            arrival_split = sailing['arrivalDate'].split('T')[0]
            sail_date = preformated(departure_split)
            return_date = preformated(arrival_split)
            rooms = sailing['rooms']
            interior_bucket_price = str(rooms['interior']['price']).split('.')[0]
            oceanview_bucket_price = str(rooms['oceanview']['price']).split('.')[0]
            balcony_bucket_price = str(rooms['balcony']['price']).split('.')[0]
            suite_bucket_price = str(rooms['suite']['price']).split('.')[0]
            if interior_bucket_price == "0":
                interior_bucket_price = 'N/A'
            if oceanview_bucket_price == "0":
                oceanview_bucket_price = 'N/A'
            if balcony_bucket_price == "0":
                balcony_bucket_price = 'N/A'
            if suite_bucket_price == "0":
                suite_bucket_price = 'N/A'
            temp = [destination_code, destination_name, vessel_id, vessel_name, cruise_id, cruise_line_name,
                    itinerary_id, brochure_name, number_of_nights, sail_date, return_date, interior_bucket_price,
                    oceanview_bucket_price, balcony_bucket_price, suite_bucket_price]
            if temp in all_sailings:
                pass
            else:
                all_sailings.append(temp)


def write_file_to_excell(data_array):
    userhome = os.path.expanduser('~')
    now = datetime.datetime.now()
    path_to_file = userhome + '/Dropbox/XLSX/For Assia to test/' + str(now.year) + '-' + str(now.month) + '-' + str(
        now.day) + '/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '- Carnival US.xlsx'
    if not os.path.exists(userhome + '/Dropbox/XLSX/For Assia to test/' + str(now.year) + '-' + str(
            now.month) + '-' + str(now.day)):
        os.makedirs(
            userhome + '/Dropbox/XLSX/For Assia to test/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day))
    workbook = xlsxwriter.Workbook(path_to_file)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 25)
    worksheet.set_column("C:C", 10)
    worksheet.set_column("D:D", 25)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 30)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 50)
    worksheet.set_column("I:I", 20)
    worksheet.set_column("J:J", 20)
    worksheet.set_column("K:K", 20)
    worksheet.set_column("L:L", 20)
    worksheet.set_column("M:M", 25)
    worksheet.set_column("N:N", 20)
    worksheet.set_column("O:O", 20)
    worksheet.write('A1', 'DestinationCode', bold)
    worksheet.write('B1', 'DestinationName', bold)
    worksheet.write('C1', 'VesselID', bold)
    worksheet.write('D1', 'VesselName', bold)
    worksheet.write('E1', 'CruiseID', bold)
    worksheet.write('F1', 'CruiseLineName', bold)
    worksheet.write('G1', 'ItineraryID', bold)
    worksheet.write('H1', 'BrochureName', bold)
    worksheet.write('I1', 'NumberOfNights', bold)
    worksheet.write('J1', 'SailDate', bold)
    worksheet.write('K1', 'ReturnDate', bold)
    worksheet.write('L1', 'InteriorBucketPrice', bold)
    worksheet.write('M1', 'OceanViewBucketPrice', bold)
    worksheet.write('N1', 'BalconyBucketPrice', bold)
    worksheet.write('O1', 'SuiteBucketPrice', bold)
    row_count = 1
    money_format = workbook.add_format({'bold': True})
    ordinary_number = workbook.add_format({"num_format": '#,##0'})
    date_format = workbook.add_format({'num_format': 'm d yyyy'})
    centered = workbook.add_format({'bold': True})
    money_format.set_align("center")
    money_format.set_bold(True)
    date_format.set_bold(True)
    centered.set_bold(True)
    ordinary_number.set_bold(True)
    ordinary_number.set_align("center")
    date_format.set_align("center")
    centered.set_align("center")
    for ship_entry in data_array:
        column_count = 0
        for en in ship_entry:
            if column_count == 0:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 1:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 2:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 3:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 4:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 5:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 6:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 7:
                worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 8:
                try:
                    worksheet.write_number(row_count, column_count, en, ordinary_number)
                except TypeError:
                    worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 9:
                try:
                    date_time = datetime.datetime.strptime(str(en), "%m/%d/%Y")
                    worksheet.write_datetime(row_count, column_count, date_time, money_format)
                except TypeError:
                    worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 10:
                try:
                    date_time = datetime.datetime.strptime(str(en), "%m/%d/%Y")
                    worksheet.write_datetime(row_count, column_count, date_time, money_format)
                except TypeError:
                    worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 11:
                try:
                    worksheet.write_number(row_count, column_count, int(en), money_format)
                except ValueError:
                    worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 12:
                try:
                    worksheet.write_number(row_count, column_count, int(en), money_format)
                except ValueError:
                    worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 13:
                try:
                    worksheet.write_number(row_count, column_count, int(en), money_format)
                except ValueError:
                    worksheet.write_string(row_count, column_count, en, centered)
            if column_count == 14:
                try:
                    worksheet.write_number(row_count, column_count, int(en), money_format)
                except ValueError:
                    worksheet.write_string(row_count, column_count, en, centered)
            column_count += 1
        row_count += 1
    workbook.close()
    pass


write_file_to_excell(all_sailings)
print(len(all_sailings))
input("Press Enter to continue...")
