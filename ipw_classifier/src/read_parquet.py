import logging
import pyarrow.dataset as ds
from uuid import UUID

logging.basicConfig(level=logging.DEBUG)

# Read_Parquet function
#-----------------------------------------------------------------
def read_parquet(parquet_file):
    dataset = ds.dataset(parquet_file)
    df = dataset.to_table().to_pandas()
    for column_name in df.columns:
        try:
            if "_id" in column_name:
                df[column_name] = df[column_name].apply(lambda x: str(UUID(int=int.from_bytes(x, 'little'))))
            if column_name == "id":
                df[column_name] = df[column_name].apply(lambda x: str(UUID(int=int.from_bytes(x, 'little'))))
        except:
            logging.info(f'Column {column_name} could not be cast to a UUID')
    return df