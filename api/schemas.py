from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union
from typing_extensions import Annotated
from datetime import datetime
from datetime import date

# ----- Branches ----- #

class File(BaseModel):
    link: Union[str,None] = "Uploaded"