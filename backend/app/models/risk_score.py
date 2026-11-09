from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from backend.app.core.database import Base

class RiskScore(Base):
    __tablename__ = "risk_scores"
    id: Mapped[int] = mapped_column(primary_key=True)
    counterparty_id: Mapped[int] = mapped_column(ForeignKey("counterparties.id", ondelete="CASCADE"))
    score: Mapped[int] = mapped_column(Integer, nullable=False) #Будет от 0 до 100
    risk_level: Mapped[str] = mapped_column(String(20), nullable=False) #Будет "Низкий", "Средний" и "Высокий"
    calculated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    counterparty = relationship("Counterparty", backref="risk_scores")
