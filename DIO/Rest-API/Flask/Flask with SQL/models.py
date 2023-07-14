from sqlalchemy import create_engine,Column,Integer,String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///atividadedio.db')
db_session = scoped_session(sessionmaker(autocommit = False, bind = engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Peoples(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key = True)
    nome = Column(String, index = True)
    idade = Column(Integer)
    
    def __repr__(self):
        return f'<people {self.nome}>'
    def save(self):
        db_session.add(self)
        db_session.commit()
        
    def delete(self):
        db_session.delete(self)
        db_session.commit()
    
class Activities(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key = True)
    nome = Column(String(80))
    people_id = Column(Integer, ForeignKey('peoples.id'))
    people = relationship("Peoples")
    
    def init_db():
        Base.metadata.create_all(bind = engine)
        
    if __name__ == '__main__':
        init_db()