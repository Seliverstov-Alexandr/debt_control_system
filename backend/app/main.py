from fastapi import FastAPI
from backend.app.api.routes import counterparties

app = FastAPI(
    title="Debt Control API",
    description="API для системы контроля дебиторской задолженности",
    version="1.0.0"
)
app.include_router(counterparties.router)

@app.get("/")
def root():
    return {"message": "Debt Control API работает!"}