from pydantic import BaseModel, ConfigDict

from typing import List

from datetime import datetime


class Address(BaseModel):
    street:str
    city : str
    zip_code: str
    
class User(BaseModel):
    id: int
    name : str
    email : str
    is_active : bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime : lambda v : v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    


user = User(
    id = 1,
    name="Purnesh",
    email = "purnesh@ai.com",
    createdAt=datetime(2026, 11, 5, 14, 30),
    address = Address(
        street="Something",
        city="Tirupati",
        zip_code="517501"
    ),
    is_active = False,
    tags = ["premium", "subscriber"]
)
    

python_dict = user.model_dump()

print(python_dict)


json_str = user.model_dump_json()

print('-------------------------')

print(json_str)