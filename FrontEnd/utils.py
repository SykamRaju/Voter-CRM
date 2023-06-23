import pandas as pd
import json

excel_file_name = "data/voterCRM.xlsx"
json_file_name = "data/voter_data.json"


def convert_excel_to_df(excel_file_name):
    df = pd.read_excel(excel_file_name)
    return df


def convert_df_to_json_str(df, orient="records"):
    """

    Converts pandas dataframe to Json string

    Parameters:
    df (dataframe): pandas dataframe
    orient(string): how to orient the json string

    Returns:
    json_str:Returning value
    """
    json_str = df.to_json(orient=orient)
    return json_str


def convert_df_to_json_file(df, file_name, orient="records"):
    """

    Converts pandas dataframe to Json file

    Parameters:
    df (dataframe): pandas dataframe
    file_name(string): json file name
    orient(string): how to orient the json string

    Returns:
    None
    """
    json_str = df.to_json(orient=orient)
    with open(json_file_name, "w") as outfile:
        json.dump(json_str, outfile)
    print(f"dataframe is saved as {file_name}")


def convert_json_file_to_df(json_file_name, orient="records"):

    """

    Converts Json file to pandas dataframe

    Parameters:
    json_file_name(string): json file name
    orient(string): how to orient the json string

    Returns:
    dataframe
    """
    with open(json_file_name, "r") as filectx:
        json_file = json.load(filectx)
        json_df = pd.read_json(json_file, orient=orient)
    return json_df


def convert_json_str_to_df(json_str, orient="records"):

    """

    Converts Json string to pandas dataframe

    Parameters:
    json_str(string): json string
    orient(string): how to orient the json string

    Returns:
    dataframe
    """
    json_df = pd.read_json(json_str, orient=orient)
    return json_df


### below is the example usage 

# df =convert_excel_to_df(excel_file_name)
# convert_df_to_json_file(df,json_file_name)
# json_str = convert_df_to_json_str(df)

# json_df = convert_json_file_to_df(json_file_name)
# convert_json_str_to_df(json_str)
 
