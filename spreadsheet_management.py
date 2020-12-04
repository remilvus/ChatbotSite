import auth
import threading
from random import randint

SPREADSHEET_ID = '1BkeZPUWZ87pGjaAkgoRSOeBhuOSn0Nw9V856wOgWZsM'
RHYME_NAME = "rhymes"
COMPLAINT_NAME = "complaints"
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
    t = threading.Thread(target=add_text, args=[rhyme, RHYME_NAME])
    t.deamon = True
    t.start()

def _save_rhyme_to_file():
    sheet = auth.get_service().spreadsheets()
    free_idx = get_free_index(sheet, RHYME_NAME)

    rhyme = ""
    if free_idx <= 1:
        rhyme = "Niestety, ale nic nie mam :/" 
    else:
        idx = randint(1, free_idx-1)
        rhyme = get_cell(sheet, RHYME_NAME + "!" + DATA_COLUMN + str(idx))

    with open("rhyme.txt", 'w') as f:
        f.write(rhyme)

def save_rhyme_to_file(wait=False):
    t = threading.Thread(target=_save_rhyme_to_file, args=[])
    t.deamon = True
    t.start()
    if wait:
        t.join()

def load_rhyme_from_file():
    rhyme = ""
    with open("rhyme.txt", 'r') as f:
        rhyme = f.read()

    return rhyme

def add_complaint(complaint):
    t = threading.Thread(target=add_text, args=[complaint, COMPLAINT_NAME])
    t.deamon = True
    t.start()


if __name__=="__main__":
    pass