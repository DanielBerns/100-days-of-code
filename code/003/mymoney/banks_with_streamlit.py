"""Todo: use argparse, black, unittest and coverage
"""
import sys
import json
from pathlib import Path

import streamlit as st

import banks as bk


def show_original_dataframe(df, bank_name):
    st.title('Reporte')
    st.header(bank_name)
    st.subheader('Planilla original')
    st.write(df.style.format(
        {'Crédito': lambda x: f"{float(x/100.0):>10.2f}",
         'Débito': lambda x: f"{float(x/100.0):>10.2f}", 
         'Saldo': lambda x: f"{float(x/100.0):>10.2f}"}))


def show_month_dataframe(df, bank_name, month):
    credit, debit, moves, df_month = bk.evaluate_month(df, month)
    st.subheader('Movimientos por mes')
    st.write(df_month.style.format({'Crédito': lambda x: f"{(x/100.0):>10.2f}", 'Débito': lambda x: f"{(x/100.0):>10.2f}"}))
    st.subheader('Movimientos por lugar')
    st.write(moves.style.format({'Crédito': lambda x: f"{float(x):>10.2f}", 'Débito': lambda x: f"{float(x):>10.2f}"}))
    return credit, debit, moves


def show_bank_by_month(bank_df, bank_identifier, bank_month):
    show_original_dataframe(bank_df, bank_identifier)
    credit, debit, moves = show_month_dataframe(bank_df, bank_identifier, bank_month)
    return credit, debit, moves


config = bk.load_config(sys.argv[1])
load_df_by_bank = {"patagonia": loaders.load_Patagonia, "chubut": loaders.load_Chubut}


if config:
    info = []
    for key, configs_by_bank in config.items():
        load_df = load_df_by_bank[key]
        for config in configs_by_bank:
            df = load_df(str(Path('~', config["source"]).expanduser()))
            credit, debit, moves = show_bank_by_month(df, config["identifier"], config["month"])
            info.append((credit, debit, credit-debit, key))
    st.header('Totales')
    totals = bk.get_totals(info)
    st.write(totals.style.format(
        {'Crédito': lambda x: f"{float(x):>10.2f}", 
         'Débito': lambda x: f"{float(x):>10.2f}", 
         'Saldo': lambda x: f"{float(x):>10.2f}"}))
        
else:
    print('Error: no config')
