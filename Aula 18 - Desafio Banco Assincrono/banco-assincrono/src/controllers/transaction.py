from fastapi import FastAPI, APIRouter, status, Cookie, Header, Response, Depends
from controllers.security import login_required
from services.transaction import TransactionService
from views.transaction import TransactionOut
from schemas.transaction import TransactionIn, TransactionType

router = APIRouter(prefix="/transactions", tags=["transactions"], dependencies=[Depends(login_required)])

transaction_service = TransactionService()

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    return await transaction_service.create(transaction)