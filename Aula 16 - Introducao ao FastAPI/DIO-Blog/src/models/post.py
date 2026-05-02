import sqlalchemy as sa
from database import metadata

posts = sa.Table("posts", metadata, 
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(150), nullable=False),
    sa.Column("content", sa.Text, nullable=False),
    sa.Column("author", sa.String(50), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=sa.func.now()),
    sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("published", sa.Boolean, nullable=False, default=False))