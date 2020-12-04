import auth

SPREADSHEET_ID = '1BkeZPUWZ87pGjaAkgoRSOeBhuOSn0Nw9V856wOgWZsM'
RHYME_NAME = "rhymes"
COMPLAINT_NAME = "complaints"
RANGE = 'B1:B100'
INDEX_COL = "A"
INDEX_ROW = "1"
DATA_COLUMN = "B"

def get_cell(sheet, cell : str) -> str:
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=cell).execute()
    vales = result.get("values")
    return str(vales[0][0])

def get_free_index(sheet, name : str) -> int:
    try:
        idx = get_cell(sheet, name + "!" + INDEX_COL + INDEX_ROW)
    except TypeError:
        return 1
    return int(idx)

def get_free_range(sheet, name : str) -> str:
    return name + "!" + DATA_COLUMN + str(get_free_index(sheet, name))

def increment_idx(sheet, name):
    idx = get_free_index(sheet, name)
    update_cell(sheet, idx+1, name + "!" + INDEX_COL + INDEX_ROW)

def update_cell(sheet, value, range_):
    update_body = {"values": [[value]]}
    respond = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=range_, body=update_body, 
                                    valueInputOption="USER_ENTERED").execute()
    return respond

def add_text(text, name):
    sheet = auth.get_service().spreadsheets()
    range_ = get_free_range(sheet, name)

    respond = update_cell(sheet, text, range_)
    increment_idx(sheet, name)
    return respond

def add_rhyme(rhyme):
    return add_text(rhyme, RHYME_NAME)

def add_complaint(complaint):
    return add_text(complaint, COMPLAINT_NAME)


if __name__=="__main__":
    pass

    # result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
    #                             range=RANGE).execute()
    # values = result.get('values')
    # up = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range="A1:B2", body=update_body, valueInputOption="USER_ENTERED")
    # print(up.execute())
    # if not values:
    #     print('No data found.')
    # else:
    #     for row in values:
    #         print(row)