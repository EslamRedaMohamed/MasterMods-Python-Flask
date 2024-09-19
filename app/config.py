class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@localhost:5432/flask_cars" # postgresql
    

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@localhost:5432/flask_cars"


config_options = {
    "dev":DevelopmentConfig,
    'prd':ProductionConfig
}