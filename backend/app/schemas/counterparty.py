from pydantic import BaseModel, ConfigDict
from typing import Optional

#Базовые поля
class CounterpartyBase(BaseModel):
    name: str
    inn: str
    kpp: Optional[str] = None
    address: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

#Схема создания (JSON клиента -> сервер). Наследование всех полей кроме id, который генерируется автоматически
class CounterpartyCreate(CounterpartyBase):
    pass

#Схема для чтения (JSON сервера -> клиент). Наследование всех полей включая id
class CounterpartyRead(CounterpartyBase):
    id: int
    #Настройка Pydantic для работы с SQLAlchemy
    model_config = ConfigDict(from_attributes=True)