"""empty message

Revision ID: 444fe1258063
Revises: 
Create Date: 2025-07-12 16:05:13.523854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '444fe1258063'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('listings',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('uploader_id', sa.String(length=36), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('size', sa.String(length=10), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('point_value', sa.Integer(), nullable=False),
    sa.Column('is_approved', sa.Boolean(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.CheckConstraint("category IN ('Men', 'Women', 'Kids')", name='check_category'),
    sa.CheckConstraint("size IN ('S', 'M', 'L', 'XL')", name='check_size'),
    sa.CheckConstraint("status IN ('Available', 'Swapped', 'Redeemed')", name='check_status'),
    sa.CheckConstraint("type IN ('Shirt', 'Pants', 'Dress', 'Others')", name='check_type'),
    sa.CheckConstraint('point_value >= 0', name='check_point_value_positive'),
    sa.ForeignKeyConstraint(['uploader_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('swaps',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('requester_id', sa.String(length=36), nullable=False),
    sa.Column('requested_item_id', sa.String(length=36), nullable=False),
    sa.Column('offered_item_id', sa.String(length=36), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('swap_type', sa.String(length=50), nullable=False),
    sa.Column('points_used', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.CheckConstraint("status IN ('Pending', 'Accepted', 'Rejected', 'Cancelled')", name='check_status'),
    sa.CheckConstraint("swap_type IN ('direct_swap', 'point_redemption')", name='check_swap_type'),
    sa.CheckConstraint('points_used >= 0', name='check_points_used_positive'),
    sa.ForeignKeyConstraint(['offered_item_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['requested_item_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['requester_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('swaps')
    op.drop_table('listings')
    op.drop_table('users')
    # ### end Alembic commands ###
