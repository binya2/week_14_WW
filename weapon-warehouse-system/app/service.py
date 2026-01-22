import io
import numpy as np
import pandas as pd
from numpy._core.numeric import nan

from db.repository import insert_weapon
from fastapi import UploadFile

from models import WeaponsDB


async def data_processing(file: UploadFile) -> pd.DataFrame:
    content = await file.read()
    csv_string = content.decode('utf-8')
    df_weapon = pd.read_csv(io.StringIO(csv_string))
    bins = [-1, 20, 100, 300, np.inf]
    labels = ['low', 'medium', 'high', 'extreme']
    df_weapon['risk_level'] = pd.cut(df_weapon['range_km'], bins=bins, labels=labels, right=True)
    df_weapon['manufacturer'] = df_weapon['manufacturer'].replace(nan, 'Unknown')
    return df_weapon


async def save_to_db(df_weapon):
    deta = df_weapon.to_dict(orient='records')
    count = 0
    for item in deta:
        print(item)
        if insert_weapon(WeaponsDB(**item)):
            count += 1
    return {"status": "success", "records_added": count}
