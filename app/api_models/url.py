from typing import List
from pydantic import BaseModel, Field

module_name = 'url'


class Base(BaseModel):
    f"""
    Base model for {module_name}
    """
    original_url: str = Field(description="url", example="http://www.google.com?id=1")


class Write(Base):
    f"""
    Use this model to create a {module_name}
    """

    class Config:
        validate_assignment = True


class Read(Base):
    f"""
    Use this model to read a {module_name}
    """
    id: str = Field(description="user_id of owner", example="62d7a781d8f8d7627ce212d5")
    url: str = Field(description="url", example="http://shrt.ir/1")
    order: int = Field(description="Ordinal number", example="1")
    created_at: str = Field(readOnly=True)
    updated_at: str = Field(readOnly=True)


class Update(Base):
    f"""
    Use this model to update a {module_name}
    """


ListRead = List[Read]
