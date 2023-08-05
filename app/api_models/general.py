from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(description="Id of created object", example="63941df5987d017a2a38f762")


class OutputCreate(BaseModel):
    """
    Use this model to create method response_model
    """
    data: Item
    detail: str = Field(description="Note string")


class OutputOnlyNote(BaseModel):
    """
    Use this model to all methods with only a text a output for response_model
    """
    detail: str = Field(description="Note string")
