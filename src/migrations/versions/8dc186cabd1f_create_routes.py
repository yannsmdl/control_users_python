"""create routes

Revision ID: 8dc186cabd1f
Revises: 54dbbc839c59
Create Date: 2024-03-30 19:43:20.843904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dc186cabd1f'
down_revision = '54dbbc839c59'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("insert into route (name, path, method, tag, created_by) values ('Criar usuário','/user','POST','User',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Buscar todos os usuários','/user','GET','User',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Buscar usuário pelo id','/user/{id}','GET','User',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Alterar usuário','/user/{id}','PUT','User',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Deletar usuário','/user/{id}','DELETE','User',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Alterar senha usuário','/user','PATCH','User',1)")
    
    op.execute("insert into route (name, path, method, tag, created_by) values ('Copiar permissoes de usuário para colocar em outro','/permission_user_routes/copy','POST','Permission User Routes',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Criar permissoes de usuário','/permission_user_routes','POST','Permission User Routes',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Buscar uma permissão pelo ID','/permission_user_routes/{permission_user_route_id}','GET','Permission User Routes',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Buscar permissoes de um usuário','/permission_user_routes/{user_id}','GET','Permission User Routes',1)")
    op.execute("insert into route (name, path, method, tag, created_by) values ('Deletar uma permissão pelo ID','/permission_user_routes/{permission_user_route_id}','DELETE','Permission User Routes',1)")

def downgrade() -> None:
    op.execute('delete from route')