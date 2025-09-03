from orfdb.base import Base, engine

def create_database():
    """Create all tables defined in the SQLAlchemy models."""
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    create_database() 