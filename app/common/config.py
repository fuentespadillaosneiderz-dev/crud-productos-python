import pymysql

class Config:
    USER = 'root'                       
    PASSWORD = ''                       # <-- Déjala vacía entre comillas simples para XAMPP
    HOST = 'localhost'                  
    DATABASE = 'db_products'            
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False