from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Forward reference for PacketData (no need to import from packet_capture)
PacketData = None  # Placeholder

# Replace with your actual database connection string
engine = create_engine('sqlite:///packets.db')

Base = declarative_base()

class PacketData(Base):
    __tablename__ = 'packets'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)  # Use DateTime for accurate timestamps
    source_ip = Column(String)
    destination_ip = Column(String)
    protocol = Column(String)  # New field for protocol
    source_port = Column(Integer)  # New field for source port
    destination_port = Column(Integer)  # New field for destination port

    def to_dict(self):
        """
        Convert the PacketData object to a dictionary for easy JSON serialization.
        """
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),  # Convert timestamp to ISO format
            "source_ip": self.source_ip,
            "destination_ip": self.destination_ip,
            "protocol": self.protocol,
            "source_port": self.source_port,
            "destination_port": self.destination_port,
        }

Base.metadata.create_all(engine)
