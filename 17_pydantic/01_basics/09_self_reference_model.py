from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None


Comment.model_rebuild()

comment = Comment(
    id= 1,
    content="First Comment",
    replies=[
        Comment(id=2, content="Reply 1"),
         Comment(id=3, content="Reply 2"),
          Comment(id=4, content="Reply 3")
    ]
)