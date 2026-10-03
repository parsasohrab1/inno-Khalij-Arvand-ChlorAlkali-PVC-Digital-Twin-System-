# chain_health.py
# مدل داده سلامت زنجیره

from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ChainHealth(Base):
    __tablename__ = "chain_health"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cell_voltage_v = Column(Float)
    current_efficiency_percent = Column(Float)
    specific_energy_kwh_per_ton = Column(Float)
    jacket_heat_transfer_coeff = Column(Float)
    agitator_motor_power_kw = Column(Float)
    batch_cycle_time_min = Column(Float)
    vcm_purity_percent = Column(Float)
    pvc_k_value = Column(Float)
