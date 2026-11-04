from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city : str
    postal_code: str


class User(BaseModel):
    id: int
    name : str
    address: Address


address = Address(
    street='123 Street',
    city = "Tirupati",
    postal_code="517501"
)


user = User(
    id= 12,
    name = "Purnesh",
    address=address,
)


user_data = {
    "id" : 1,
    "name" : "Hitesh",
    "address": {
        "street": "Sundarayyar Street",
        "city" : "Chittoor",
        "postal_code": "517001"
    }
}


user = User(**user_data)
print(user)