from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User bases class which has details like username and email id as they will be used in multiple places.
class UserBase(BaseModel):
    username: str
    email: EmailStr

# UserCreate Class which inherits from UserBase and has password field as well which is required for creating a user.
class UserCreate(UserBase):
    password: str

# UserResponse class which inherits from UserBase to show the feilds for user
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True} # SQLAlchemy returns data like Object but Pydantic by default expects dict format

# UserUpdate class which inherits from UserBase to update the feilds
class UserUpdate(UserBase):
    username: Optional[str] = None
    is_active: Optional[bool] = None
    email: Optional[EmailStr] = None