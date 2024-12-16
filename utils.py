from database.db_session import Base


def table_fields(table: Base):
    fields: list = table.__mapper__.attrs.keys()

    try:
        fields.remove('id')
    except ValueError:
        pass

    return fields
