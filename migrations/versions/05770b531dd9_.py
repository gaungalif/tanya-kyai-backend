"""empty message

Revision ID: 05770b531dd9
Revises: 23ad7f7c5326
Create Date: 2022-11-28 10:50:13.650711

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '05770b531dd9'
down_revision = '23ad7f7c5326'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_table('user')
    op.drop_table('mahasiswa')
    op.drop_table('dosen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('nidn', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('nama', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=13), nullable=False),
    sa.Column('alamat', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('mahasiswa',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('nim', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('nama', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=13), nullable=False),
    sa.Column('alamat', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('dosen_satu', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('dosen_dua', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['dosen_dua'], ['dosen.id'], name='mahasiswa_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['dosen_satu'], ['dosen.id'], name='mahasiswa_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('user',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('level', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###
