from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class TaskBase(BaseModel):
  title: Optional[str] = Field(None, json_schema_extra={ "example": "クリーニングをとりに行く" })

class TaskCreate(TaskBase):
  pass

class TaskCreateResponse(TaskCreate):
  id: int
  model_config = ConfigDict(from_attributes = True)

class Task(TaskBase):
  id: int
  done: bool = Field(False, json_schema_extra={ "description": "完了フラグ" })
  model_config = ConfigDict(from_attributes = True)