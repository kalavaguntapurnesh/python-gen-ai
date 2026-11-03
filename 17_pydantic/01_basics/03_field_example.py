from pydantic import BaseModel

from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items : List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url : Optional[str] = None
    

cart_data = {
    "user_id" : 222,
    "items": ["Laptop", "Mouse", "Keyboard", "Speakers"],
    "quantities": {"laptop": 1, "mouse": 1, "keyboard": 1, "speakers": 2}
}

cart = Cart(**cart_data)

print(cart)