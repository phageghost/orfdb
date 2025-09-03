from orfdb.base import Base, engine, Session
from sqlalchemy import inspect, text
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_connection():
    """Test database connection and table creation."""
    try:
        # Test connection and show connection details
        with engine.connect() as conn:
            logger.info("Successfully connected to database")
            # Get current database and schema
            result = conn.execute(text("SELECT current_database(), current_schema()"))
            db_name, schema = result.first()
            logger.info(f"Connected to database: {db_name}")
            logger.info(f"Current schema: {schema}")
            
        # Create tables
        logger.info("Creating tables...")
        Base.metadata.create_all(engine)
        logger.info("Table creation completed")
        
        # Verify tables were created
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        logger.info(f"Tables in database: {tables}")
        
        # Print table details
        for table_name in tables:
            columns = inspector.get_columns(table_name)
            logger.info(f"\nTable: {table_name}")
            for column in columns:
                logger.info(f"  Column: {column['name']} ({column['type']})")
                
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    test_connection() 