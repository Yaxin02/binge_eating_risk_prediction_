from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from database import Base

class BingePrediction(Base):
    __tablename__ = "binge_predictions"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Float, nullable=False)
    gender = Column(Integer, nullable=False)
    bmi = Column(Float, nullable=False)
    weight_kg = Column(Float, nullable=False)
    waist_cm = Column(Float, nullable=False)
    education = Column(Integer, nullable=False)
    alcohol = Column(Integer, nullable=False)
    t2d = Column(Integer, nullable=False)
    sleep_apnea_syndrome = Column(Integer, nullable=False)
    gastroesophageal_reflux_disease = Column(Integer, nullable=False)
    ede_q_per_operation = Column(Float, nullable=False)
    prediction = Column(Integer, nullable=False)
    probability = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)