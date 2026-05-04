from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat

from schemas.transaction import TransactionType

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: AwareDatetime | NaiveDatetime


class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: PositiveFloat
    timestamp: AwareDatetime | NaiveDatetime