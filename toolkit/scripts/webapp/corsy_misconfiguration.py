# web crawler for gathering URLs
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(target_url):
    pre_output = subprocess.getoutput(
        f"python3 {BASE_DIR}/webapp/Corsy/corsy.py -u '{target_url}'"
    
    )
    
    print("CORSY Loaded")
    if pre_output != "":
        result = pre_output.split("\n")
        return result

    else:
        return None
        
