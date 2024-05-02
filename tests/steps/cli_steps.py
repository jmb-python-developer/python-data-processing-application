from behave import *

import sys
import os
import logging

# This appends the project root to the sys.path.
# Assuming this file is within a subfolder of the project root, such as 'tests/steps/'
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.acquire import *

# Configure Logging for step definitions file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@given(u'the Anscombe Quartet data file exists in the "{dir}" directory with name "{filename}"') 
def file_exists(context, dir, filename):
    context.filename = filename
    context.filepath = f'../../{dir}/{filename}'
    logging.info(f'Checking data file exists in directory {context.filepath}')
    assert os.path.isfile(f'../../{dir}/{filename}'), f'File does not exist: {filename}'

@when(u'the app command with args "{args}" for the data file is run')
def run_app_command(context, args: str):
    parsed_args = args.split()
    parsed_args.append(f"data/{context.filename}")
    logging.info(f'Running CLI data parsing app with arguments: {parsed_args}')
    main(parsed_args)
