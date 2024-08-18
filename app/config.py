import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://task4p_4ocs_user:RNomcRh19vUpP4UGRWKqYen8oHpYQmXw@dpg-cr0qspbqf0us73fearn0-a.oregon-postgres.render.com/task4p_4ocs")

settings = Settings()
