from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name : str
    price : float
    in_stock: bool = True
    

product_one = Product(id =1, name = "Laptop", price = 500.98)

product_two = Product(id=2, name = "Camera", price = 999.99)

# product_three = Product(name="keyboard") will throw an error

print(product_one)
print(product_two)