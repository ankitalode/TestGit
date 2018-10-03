"""
    File name: tigera_test.py
    Author: Ankita Lode
    Date created: 10/03/2018
    Python Version: 3.6
"""

# standard library
import os

def setup_module(module):
    assert os.path.exists("test.log") == True

def test_status():
    """
     This function will return and assert status count
     :return: status count
     """
    status = {'INFO': 0, "WARNING": 0, "ERROR": 0}
    try:
        with open("test.log",'r') as log_file:
            for line in log_file:
                if "INFO :" in line:
                    status["INFO"]  += 1
                elif "WARNING :" in line:
                    status["WARNING"] += 1
                elif "ERROR :" in line:
                    status["ERROR"] += 1

    except FileNotFoundError as e:
        raise FileNotFoundError("File Not present with the given name")

    assert status["INFO"] == 50
    assert status["WARNING"] == 11
    assert status["ERROR"] == 3
    print (status)