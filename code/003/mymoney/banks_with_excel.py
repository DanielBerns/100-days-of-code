"""Todo: use argparse, black, unittest and coverage
"""
import sys
import json
from pathlib import Path

import banks as bk
from loaders import get_load_df
import pandas as pd

len_argv = len(sys.argv)

if len_argv == 2:

    argument = sys.argv[1]
    
    if argument == '--start':
        load_df = get_load_df()
        config = bk.create_config(load_df.keys(), ['source', 'month', 'title', 'report'])
        bk.save_config(config)
    elif argument == '--help':
        pass
    else:
        print('Goodbye!')
        
elif len_argv == 3:
    
    argument = sys.argv[1]
    
    if argument == '--config':
        config_file_identifier = sys.argv[2]
        
        config = bk.load_config(config_file_identifier)
        if config:
            load_df = get_load_df()
            data_stem = bk.get_data_folder()
            sources = config["sources"]
            targets = {}
            for bank, config_node in sources.items():
                df_bank = load_df[bank](Path(data_stem, bank, config_node['source']))
                credit_bank, debit_bank, moves_bank, month_bank = bk.evaluate_month(df_bank, config_node['month'])
                targets[bank] = [credit_bank, debit_bank]        
            totals = bk.get_totals(targets)
            bank_report = pd.DataFrame.from_dict(totals)
            bank_report.to_excel(Path(data_stem, config['target']))                
        else:
            print('Error: no config')
    else:
        print(f'Unknown command line argument: {argument:s}')

else:
    print('No command line arguments')
