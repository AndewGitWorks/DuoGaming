from datetime import datetime

from sqlalchemy import create_engine, column, Integer, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    @classmethod
    @property
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class User(Base):
    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    avatar_url: Mapped[str | None]
    bio: Mapped[str | None]
    website: Mapped[str | None]
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_active: Mapped[bool] = mapped_column(default=True)


class Tag(Base):
    name = Mapped[str]
    slug = Mapped[str]


class Post(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str]
    content: Mapped[str]
    image_url: Mapped[str | None]
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_published: Mapped[bool] = mapped_column(default=True)
    view_count: Mapped[int] = mapped_column(default=0)


class Post_tag(Base):
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))


class Like(Base):
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class Follower(Base):
    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    following_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class Comment(Base):
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    parent_comment: Mapped[int | None]
    content: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_edited: Mapped[bool] = mapped_column(default=False)