# web crawler for gathering URLs
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(target_url):
    pre_output = subprocess.getoutput(
        f"waybackurls {target_url}"
    
    )
    print("WaybackURLS Loaded Successfully")
    if pre_output != "":
        result = pre_output.split("\n")
        return result

    else:
        return None
        
        
        
def get_(target_url):
    pre_output = subprocess.getoutput(
        f"echo {target_url} | hakrawler > {BASE_DIR}/webapp/hakrawler.txt"
    
    )
    print("Hakrawler Loaded Successfully")
    if pre_output != "":
        result = pre_output.split("\n")
        return result

    else:
        return None
