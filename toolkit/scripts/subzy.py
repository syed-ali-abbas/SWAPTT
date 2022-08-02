import os
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)




def subazy_():

    command = [
        "subzy",
        "--targes",
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



