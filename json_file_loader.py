from geekshop.settings import BASE_DIR
import json


JSON_DATAFILE = 'db.json'


def _load_datafile():
    try:
        with open(BASE_DIR / JSON_DATAFILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print('JSON load error:', e)


def load_json_data(section, default):
    data = _load_datafile()
    if data is not None:
        return data.get(section, default)
    return default
