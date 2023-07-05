import numpy as np
import pandas as pd
from read_parquet import read_parquet
 
from pathlib import Path
 
 
#-----------------------------------------------------------------
# Select parquet files
#-----------------------------------------------------------------
path = Path(r'C:/Git/HonoursProject/ipw-classifier/ipw_classifier/data/')
 
table_names = [
    'case',
    'efficiency',
    'efficiency_cost',
    'efficiency_expense',
    'stream',
]
 
table_paths = {
    table_name: path / f"{table_name}.parquet"
    for table_name in table_names
}
  
 
#-----------------------------------------------------------------
# PD read Parquetfiles
#-----------------------------------------------------------------
tables = {
    table_name: read_parquet(table_paths[table_name])
    for table_name in table_names
}
 
#-----------------------------------------------------------------
# Add suffixes to columns (except for case_table)
#-----------------------------------------------------------------
case_table = tables['case']
efficiency = tables['efficiency'].add_suffix("_e")
efficiency_cost = tables['efficiency_cost'].add_suffix("_ec")
efficiency_expense = tables['efficiency_expense'].add_suffix("_ee")
stream = tables['stream'].add_suffix("_s")
