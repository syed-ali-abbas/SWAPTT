import os
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)


def subzy():

    command = [
        "subzy",
        "--targets",
        f"{BASE_DIR}/webapp/output.txt",
    ]
  
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    output = []
    for line in process.stdout:
        output.append(line.decode("utf-8"))
        print(line)
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)
        
        
       

def knockpy(target_url):

    command = [
        "amass",
        "enum",
        "-d",
        f"{target_url}",
        "-o",
        f"{BASE_DIR}/webapp/output.txt",
    ]

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    output = []
    for line in process.stdout:
        # if (re.match(r"[\d\.]+.*[\w\.]+.*", line.decode("utf-8")) or 'times' in line.decode("utf-8")):
        # sys.stdout.write(str(line))
        output.append(line.decode("utf-8"))
        print(line)
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)


def sublister(target_url):
    command = [
        f"{PY_PATH}/venv/bin/python",
        f"{BASE_DIR}/webapp/sublist3r.py",
        "--no-color",
        "-d",
        f"{target_url}",
        "-o",
        f"{BASE_DIR}/webapp/output.txt",
    ]

    process = subprocess.run(
        command,
        capture_output=True,
        encoding="utf-8",
    )
    pre_output = process.stdout.split("\n")
    result = []
    for line in pre_output:
        print(line)

        if target_url in str(line) and "subdomains" not in str(line):
            result.append(str(line))
            
    
  
    return result
