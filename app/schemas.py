from pydantic import BaseModel

class GameBase(BaseModel):
    id: int

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int
    player_id: int
    
    class Config:
        orm_model = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    games: list[Game] = []

    class Config:
        orm_mode = True
