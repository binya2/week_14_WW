import io

import numpy as np
import pandas as pd
from fastapi import UploadFile
from numpy._core.numeric import nan

from core.errors import CSVFormatError
from db.repository import insert_weapon, insert_weapons
from models import WeaponsDB


async def data_processing(file: UploadFile) -> pd.DataFrame:
    try:
        content = await file.read()
        csv_string = content.decode('utf-8')
        df_weapon = pd.read_csv(io.StringIO(csv_string))
        bins = [-1, 20, 100, 300, np.inf]
        labels = ['low', 'medium', 'high', 'extreme']
        df_weapon['risk_level'] = pd.cut(df_weapon['range_km'], bins=bins, labels=labels, right=True)
        df_weapon['manufacturer'] = df_weapon['manufacturer'].replace(nan, 'Unknown')
        return df_weapon
    except Exception as e:
        raise CSVFormatError(f"Failed to process CSV: {str(e)}")


async def save_to_db(df_weapon):
    deta = df_weapon.to_dict(orient='records')
    list = [dic for dic in deta if insert_weapon(WeaponsDB(**dic))]
    count = insert_weapons(list)
    # for item in deta:
    #     print(item)
    #     if insert_weapon(WeaponsDB(**item)):
    #         count += 1
    return {"status": "success", "records_added": count}
