from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.counterparty import Counterparty
from backend.app.schemas.counterparty import CounterpartyCreate, CounterpartyRead

# Создание роутера для работы с контрагентами 
router = APIRouter(
    prefix="/counterparties",
    tags=["counterparties"])

@router.post("/",response_model=CounterpartyRead, status_code=status.HTTP_201_CREATED)
def create_counterparty(counterparty_in: CounterpartyCreate, db: Session = Depends(get_db)):
    """
    Создание нового контрагента
    """

    # Проверка на существование контрагента с таким же ИНН
    existing_counterparty = db.query(Counterparty).filter(Counterparty.inn == counterparty_in.inn).first()
    if existing_counterparty:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Контрагент с таким ИНН уже существует")

    # Превращение Pydantic модели в SQLAlchemy модель
    new_counterparty = Counterparty(**counterparty_in.model_dump())

    # Сохранение нового контрагента в базе данных
    db.add(new_counterparty)
    db.commit()
    db.refresh(new_counterparty)

    return new_counterparty