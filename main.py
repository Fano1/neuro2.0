import models.ConverseText as ct
import models.codingModel as cm
import models.GenerationRecon as gr

from protocol.protocol import ProtocolExecuteFile, ProtocolExecuteLink, ProtocolHardwareAccess

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

async def Run(stateR: bool):
    await ct.main(stateR)

@app.post("/main")
async def index(*, state: Optional[bool] = False, exitTextr :Optional[str] = None):
    if (state == True):
        Run(state)
        #asyncio.run(ct.main()) holy fuck dont use this way (FastApi already makes a event loops, using async.run makes 2 event loops fuking crashes everything after first use)
        return "successful"
    

@app.post("/coding-model")
def index(*,text: Optional[str] = None, state: Optional[bool] = None):
    cm.code(text, state)


@app.post("/generation-recon")
def index(*, text: Optional[str] = None, mode: Optional[str] = None, pathR: Optional[str] = None):
    executer = gr.ProtocolGenerateContent(text, pathR)
    rizen = f"executer.{mode}"
    pass #on hold, google image generator sucks

@app.post("/load-link")
def index(*, content: Optional[str] = None):
    executer = gr.ProtocolGenerateContent(content, "pp")
    linkr = executer.generateLink()
    executerA = ProtocolExecuteLink(linkr)
    executerA.loadLink()