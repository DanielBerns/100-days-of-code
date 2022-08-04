"""Todo: use argparse, black, unittest and coverage
"""
import pandas as pd
from pathlib import Path
import json      


def get_data_folder():
    return Path('~', 'Data', 'Banks').expanduser()


def create_config(names, attributes):
    config = {}
    for n in names:
        config[n] = create_config_node(attributes)
    return config


def create_config_node(attributes):
    config_node = {}
    for a in attributes:
        config_node[a] = ''
    return config_node


def load_config(file_identifier):             
    config = None
    with open(file_identifier, 'r') as config_file:
        config = json.load(config_file)
    return config 


def save_config(config):             
    data_folder = get_data_folder()
    file_identifier = Path(data_folder, 'config.json')
    with open(file_identifier, 'w') as config_file:
        json.dump(config, config_file)


def evaluate_month(df, month):
    mask = (df['AAAA-MM'] == month)
    df_month = df[mask]
    df_month = df_month[['Concepto', 'Débito', 'Crédito']]
    moves = df_month.groupby(by=['Concepto']).sum() 
    debit = moves['Débito'].sum() / 100.0
    credit = moves['Crédito'].sum() / 100.0
    moves = moves / 100.0
    return credit, debit, moves, df_month


def get_totals_by_bank(credit, debit):
    data = [credit, debit, credit - debit]
    df = pd.DataFrame(data, columns=['Crédito', 'Débito', 'Saldo'])
    return df

        
def get_totals(info):
    rows = []
    index = []
    credit_total = debit_total = balance_total = 0
    for key, value in info.items():
        credit, debit = value[0], value[1]
        balance = credit - debit
        rows.append((credit, debit, balance))
        index.append(key)
        credit_total += credit
        debit_total += debit
        balance_total += balance
    rows.append((credit_total, debit_total, balance_total))
    index.append('total')
    df = pd.DataFrame(rows, columns = ['Crédito', 'Débito', 'Saldo'], index=index)
    return df

# References
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
