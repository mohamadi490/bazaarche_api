
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    url: str
    alt: Optional[str] = None
    is_thumbnail: bool = False
    order: int

class ProductImage(ImageBase):
    id: int
    
class Image(ImageBase):
    id: int
    entity_type: str
    entity_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
    