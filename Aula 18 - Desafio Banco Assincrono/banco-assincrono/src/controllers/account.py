from fastapi import FastAPI, APIRouter, status, Cookie, Header, Response, Depends
from controllers.security import login_required
from services.account import AccountService
from services.transaction import TransactionService
from views.account import AccountOut
from views.transaction import TransactionOut
from schemas.account import AccountIn

router = APIRouter(prefix="/accounts", tags=["accounts"], dependencies =[Depends(login_required)])

account_service = AccountService()
transaction_service = TransactionService()

@router.get("/", response_model=list[AccountOut])
async def read_accounts(limit: int, skip: int = 0):
    return await account_service.read_all(limit=limit, skip=skip)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(account: AccountIn):
    return await account_service.create(account)

@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0):
    return await transaction_service.read_by_account(id, limit=limit, skip=skip)