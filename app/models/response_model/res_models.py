from pydantic import BaseModel, Field
from typing import Optional, List


class Comment(BaseModel):
    id: int
    company_id: int