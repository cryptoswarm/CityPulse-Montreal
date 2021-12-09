"""correction name of table

Revision ID: ea8d55a4577d
Revises: 
Create Date: 2021-12-09 16:02:17.074118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea8d55a4577d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arrondissement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('cle', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cle'),
    sa.UniqueConstraint('name')
    )
    op.create_table('coordinates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('point_x', sa.String(length=255), nullable=False),
    sa.Column('point_y', sa.String(length=255), nullable=False),
    sa.Column('longitude', sa.String(length=255), nullable=False),
    sa.Column('latitude', sa.String(length=255), nullable=False),
    sa.Column('position_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('position_hash')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('complete_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('glissade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('date_maj', sa.DateTime(timezone=True), nullable=False),
    sa.Column('ouvert', sa.Boolean(), nullable=False),
    sa.Column('deblaye', sa.Boolean(), nullable=False),
    sa.Column('condition', sa.String(length=255), nullable=False),
    sa.Column('arrondissement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrondissement_id'], ['arrondissement.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('installation_aquatique',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom_installation', sa.String(length=255), nullable=False),
    sa.Column('type_installation', sa.String(length=255), nullable=False),
    sa.Column('adress', sa.String(length=255), nullable=False),
    sa.Column('propriete_installation', sa.String(length=255), nullable=False),
    sa.Column('gestion_inst', sa.String(length=255), nullable=False),
    sa.Column('equipement_inst', sa.String(length=255), nullable=False),
    sa.Column('aqua_hash', sa.String(length=255), nullable=False),
    sa.Column('arron_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arron_id'], ['arrondissement.id'], ),
    sa.ForeignKeyConstraint(['position_id'], ['coordinates.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('aqua_hash')
    )
    op.create_table('patinoire',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom_pat', sa.String(length=255), nullable=False),
    sa.Column('arron_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arron_id'], ['arrondissement.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nom_pat')
    )
    op.create_table('profile_arrondissement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patinoir_condition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_heure', sa.DateTime(), nullable=False),
    sa.Column('ouvert', sa.Boolean(), nullable=False),
    sa.Column('deblaye', sa.Boolean(), nullable=False),
    sa.Column('arrose', sa.Boolean(), nullable=False),
    sa.Column('resurface', sa.Boolean(), nullable=False),
    sa.Column('patinoire_id', sa.Integer(), nullable=True),
    sa.Column('pat_hash', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['patinoire_id'], ['patinoire.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pat_hash')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patinoir_condition')
    op.drop_table('profile_arrondissement')
    op.drop_table('patinoire')
    op.drop_table('installation_aquatique')
    op.drop_table('glissade')
    op.drop_table('profile')
    op.drop_table('coordinates')
    op.drop_table('arrondissement')
    # ### end Alembic commands ###