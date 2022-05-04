import sqlalchemy
import sqlalchemy.orm

from test_agro.data.model_base import SqlAlchemyBase

import test_agro.data.customer
import test_agro.data.product
import test_agro.data.order

class DbSession:
    __session_factory = None

    @classmethod
    def global_init(cls):
        conn_str = 'postgresql+psycopg2://jnajlrpe:1d99vsCK-PU_cQILbnJ0QW3tBr9Ql6Jp@tai.db.elephantsql.com/jnajlrpe' 
        engine = sqlalchemy.create_engine(conn_str)

        SqlAlchemyBase.metadata.create_all(engine)

        cls.__session_factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @classmethod
    def create_session(cls):
        return cls.__session_factory()



