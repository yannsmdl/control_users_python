"""create user adm

Revision ID: 54dbbc839c59
Revises: 975d7d55fa5c
Create Date: 2024-03-30 19:42:42.605622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54dbbc839c59'
down_revision = '975d7d55fa5c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""insert into "user" (name, password, email, birth_date, created_by) values ('adm','$2b$08$Ban8tttwEuAsoKUymzo1.OspSepYILFWPTgmotdi1Asx2XI4VZ4.y','adm@adm','2000-01-01',1)""")
    ### senha 123456


def downgrade() -> None:
    op.execute('delete from "user"')