import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:")
connection = engine.connect()

metadata = sa.MetaData()

article_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("code", sa.String),    
    sa.Column("brand", sa.String),
    sa.Column("description", sa.String),
    sa.Column("packaging", sa.String),    
)


def insert_article(
    code: str, 
    brand: str, 
    description: str, 
    packaging: str
    ) -> None:
    query = article_table.insert().values(
        code=code,
        brand=brand, 
        description=description,
        packaging=packaging
    )
    connection.execute(query)


def select_article_by_code(code: str) -> sa.engine.Result:
    query = article_table.select().where(article_table.c.code == code)
    result = connection.execute(query)
    return result.fetchone()

def select_article_by_brand(brand: str) -> sa.engine.Result:
    query = article_table.select().where(article_table.c.brand == brand)
    result = connection.execute(query)
    return result.fetchone()

def main() -> None:
    metadata.create_all(engine)
    insert_article("7787887890", "Nestle", "Leche", "Sachet")
    insert_article("7787887980", "Arcor", "Leche", "Sachet")
    insert_article("7788787980", "Tregar", "Crema", "Pote")        
    print(select_article_by_code("7787887890"))
    print(select_article_by_brand("Tregar"))    
    connection.close()


if __name__ == "__main__":
    main()
