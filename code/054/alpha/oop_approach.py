import json
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    brand: Mapped[str]
    description: Mapped[str]    
    packaging: Mapped[str]    
    
    def __repr__(self) -> str:
        values = {"id":f"{self.id:d}", 
                  "code":f"{self.code:s}", 
                  "brand":f"{self.brand:s}", 
                  "description":f"{self.description:s}",
                  "packaging": f"{self.packaging:s}"
        }
        return json.dumps(values)


def main() -> None:
    Base.metadata.create_all(db)
    article = Article(
        code="7788987897", 
        brand="Nestle", 
        description="leche entera", 
        packaging="sachet"
    )

    with Session() as session:
        session.add(article)
        session.commit()
        print(session.query(Article).all())


if __name__ == "__main__":
    main()
