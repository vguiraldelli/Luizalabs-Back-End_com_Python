import sqlalchemy as sa

from database import metadata

transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.Integer),
    sa.Column("type", sa.String(10), nullable=False),
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
