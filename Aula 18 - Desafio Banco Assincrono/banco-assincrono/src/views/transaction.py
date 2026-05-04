from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat

from schemas.transaction import TransactionType

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: PositiveFloat
    created_at: AwareDatetime | NaiveDatetime