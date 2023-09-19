
import pandas as pd
from math import isnan
from pathlib import Path
from pydantic import BaseModel, validator
# from pydantic.annotated_arguments import BeforeValidator
from typing import List, Optional, Any, TypeVar, Annotated
import numpy as np


# def coerce_nan_to_none(x: Any) -> Any:
#     if isnan(x):
#         return None
#     return x

# T = TypeVar("T")    

# NoneOrNan = Annotated[Optional[T], BeforeValidator(coerce_nan_to_none)]

# class BaseModel(PydanticBaseModel):
#     @validator('*')
#     def change_nan_to_none(cls, v, field):
#         if field.outer_type_ is float and isnan(v):
#             return None
#         return v

class SwitchInterface(BaseModel):
    switch: str
    if_name: str
    gs_if_name: str  # optional


class GenericSystemModel(BaseModel):
    blueprint: str
    system_label: str
    is_external: bool
    speed: str
    lag_mode: Optional[str] # mandatory in case of multiple interfaces
    label1: str
    ifname1: str
    gs_ifname1: Optional[str]
    label2: Optional[str]
    ifname2: Optional[str]
    gs_ifname2: Optional[str]
    label3: Optional[str]
    ifname3: Optional[str]
    gs_ifname3: Optional[str]
    label4: Optional[str]
    ifname4: Optional[str]
    gs_ifname4: Optional[str]
    untagged_vlan: Optional[str] = None
    tagged_vlans: Optional[str] = None
    ct_names: Optional[str] = None
    comment: Optional[str] = None


generic_system_data = {} # { blueprint: { generic_system: {....}}}



def procss_row(row):
    # print(f"{row=}")
    blueprint_label = row['blueprint']
    blueprint_data = generic_system_data.setdefault(blueprint_label, {})
    system_label = row['system_label']
    system_data = blueprint_data.setdefault(system_label,[])
    print(f"{generic_system_data}")
    pydantic_data = GenericSystemModel(**row)
    print(f"{pydantic_data=}")


def hello():
    print("Hello World!")
    input_file_path = Path("./tests/fixtures/ApstraProvisiongTemplate.xlsx") 
    # df = pd.read_excel(input_file_path, sheet_name="generic_systems", header=[0,1], index_col=[0,1])
    df = pd.read_excel(input_file_path, sheet_name="generic_systems", header=[1])
    df = df.replace({np.nan: None})
    # print("df=")
    # print(df)
    # print(f"{type(df)=}")
    input_data = {} # { blueprint: { generic_system: {....}}}
    # for column in df.columns:
    #     print(f"{column=}")
    # for index in df.index:
    #     print(f"{index=}")
    # for row in df.itertuples():
    #     print(f"{row=}")
    #     print(f"index {row[0]=}")
    #     print(f"{getattr(row, 'Index')=}")
    #     print(f"{df.loc[ row[0], ('switch1', 'label')]=}")
    #     blueprint = df.loc
    df.apply(procss_row, axis=1)
        # print(f"{row[('switch1', 'label')]=}")
        # print(f"{row['switch1', 'label']=}")
        # print(f"{row['switch1', 'label']=}")
                
    # data_list = df.to_dict(orient="records")
    # print(f"{data_list=}")
    # parsed_data = [GenericSystemModel(**data) for data in data_list]


