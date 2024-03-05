"""added review table

Revision ID: 232f6be10866
Revises: 83ca2d16e878
Create Date: 2024-03-05 12:52:11.265419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232f6be10866'
down_revision = '83ca2d16e878'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_review',
    sa.Column('review_id', sa.String(), nullable=False),
    sa.Column('movie_title', sa.String(length=100), nullable=False),
    sa.Column('review_text', sa.String(length=1000), nullable=True),
    sa.Column('rating', sa.Numeric(precision=2, scale=1), nullable=False),
    sa.Column('reviewer_name', sa.String(length=50), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('movie_director', sa.String(length=100), nullable=True),
    sa.Column('movie_year', sa.String(length=4), nullable=True),
    sa.Column('movie_plot', sa.String(length=1000), nullable=True),
    sa.Column('movie_poster', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_review')
    # ### end Alembic commands ###