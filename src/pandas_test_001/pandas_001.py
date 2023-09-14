
import pandas as pd
from pathlib import Path


def hello():
    print("Hello World!")
    input_file_path = Path("./tests/fixtures/ApstraProvisiongTemplate.xlsx") 
    df = pd.read_excel(input_file_path, sheet_name="generic_systems", header=[0,1])
    print(f"{df=}")
    print(f"{type(df)=}")
    for column in df.columns:
        print(f"{column=}")
    for index in df.index:
        print(f"{index=}")
    for row in df.itertuples():
        print(f"{row=}")
        print(f"index {row[0]=}")
        print(f"{getattr(row, 'Index')=}")
        print(f"{df.loc[ row[0], ('switch1', 'label')]=}")
        # print(f"{row[('switch1', 'label')]=}")
        # print(f"{row['switch1', 'label']=}")


