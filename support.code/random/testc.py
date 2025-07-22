from fastapi import FastAPI
from protocol.protocol import ProtocolExecuteFile, ProtocolExecuteLink, ProtocolHardwareAccess
from pydantic import BaseModel

app = FastAPI()

class FileRunRequest(BaseModel):
    path: str
    file_type: str  # 'py' or 'c'
    output: str = None

class LinkRequest(BaseModel):
    url: str

class ToggleRequest(BaseModel):
    pin: int
    mode: str
    cycles: int
    delay: float

@app.post("/run-file")
def run_file(data: FileRunRequest):
    executor = ProtocolExecuteFile(data.path)
    if data.file_type == 'py':
        executor.execute_file_py()
    elif data.file_type == 'c' and data.output:
        executor.execute_file_c(data.output)
    else:
        return {"error": "Missing output for C file"}
    return {"status": "success"}

@app.post("/open-link")
def open_link(data: LinkRequest):
    ProtocolExecuteLink(data.url).load_link()
    return {"status": "link opened"}

@app.post("/toggle-pin")
def toggle_pin(data: ToggleRequest):
    hw = ProtocolHardwareAccess()
    hw.set_power_toggle(data.cycles, data.delay, data.pin, data.mode)
    return {"status": "pin toggled"}
