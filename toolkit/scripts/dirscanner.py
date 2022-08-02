import subprocess
import time

from .checksum import check
from .ctpdf import convert_to_pdf
import os
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)

def dirscan_script(ip, user_name, function_name):

    command = [
        f"{PY_PATH}/venv/bin/python3",
        f"{BASE_DIR}/webapp/dirsearch/dirsearch.py",
        "-e",
        "txt,asp,php",
        "-t",
        "50",
        "--format=simple",
        "--no-color",
        "-q",
        "--exclude-status=500",
        "-u",
        f"{ip}",
    ]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = []
    for line in process.stdout:
        # sys.stdout.write(str(line))
        output.append(line.decode("utf-8"))
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)

    if check():
        convert_to_pdf(output, user_name, ip, function_name)
