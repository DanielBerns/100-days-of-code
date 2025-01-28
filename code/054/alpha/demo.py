import hashlib
import typing
import sqlalchemy as sa
from sqlalchemy.orm import (
    declarative_base,
    mapped_column,
    relationship,
    sessionmaker,
    Mapped,
)

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = sa.Column(sa.String)
    brand: Mapped[str] = sa.Column(sa.String)
    description: Mapped[str] = sa.Column(sa.String)   
    packaging: Mapped[str] = sa.Column(sa.String)   

class State(Base):
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = sa.Column(sa.String)
    name: Mapped[str] = sa.Column(sa.String)   
    cities: Mapped[typing.List["City"]] = relationship(
        "City", back_populates="states"
    )
    
def main() -> None:
    Base.metadata.create_all(db)

    with Session.begin() as session:
        article = Article(
            code="567567567576", 
            brand="Nestle", 
            description="password",
            packaging="sachet"
        )
        session.add(article)



    with Session.begin() as session:
        user = session.query(User).first()
        print(user)
        print(user.auth)
        print(user.posts)

        print(f"Password check: {user.auth.check_password('password')}")
        print(f"Password check: {user.auth.check_password('wrongpassword')}")

        posts = session.query(UserPost).filter(UserPost.user == user).all()
        print(posts)


if __name__ == "__main__":
    main()
    


class City(Base):
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    state_id: int = sa.Column(
        sa.Integer, sa.ForeignKey("states.id"), nullable=False, index=True
    )
    points_of_sale: Mapped[typing.List["PointOfSale"]] = relationship(
        "PointOfSale", back_populates="cities"
    )


class PointOfSale(Base):
    __tablename__ = "points_of_sale"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    name: Mapped[str]
    address: Mapped[str]    
    city_id: int = sa.Column(
        sa.Integer, sa.ForeignKey("cities.id"), nullable=False, index=True
    )    


class Timestamp(Base):
    __tablename__ = "timestamps"
    id: Mapped[int] = mapped_column(primary_key=True)
    prices: Mapped[typing.List["Price"]] = relationship(
        "Price", back_populates="timestamps"
    )

    
class Price(Base):
    __tablename__ = "prices"
    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp_id: int = sa.Column(
        sa.Integer, sa.ForeignKey("timestamps.id"), nullable=False, index=True
    )
    article_id: int = sa.Column(
        sa.Integer, sa.ForeignKey("articles.id"), nullable=False, index=True
    )        
    point_of_sale_id: int = sa.Column(
        sa.Integer, sa.ForeignKey("points_of_sale.id"), nullable=False, index=True
    )        
