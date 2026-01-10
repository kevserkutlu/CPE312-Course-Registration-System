from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
import os

# Base sınıfı tüm modeller için
Base = declarative_base()

class DatabaseManager:
    """SQLAlchemy kullanarak veritabanı bağlantısını yönet"""
    
    def __init__(self, database_url=None):
        """
        Veritabanı yöneticisini başlat
        
        Args:
            database_url: Veritabanı bağlantı URL'si
                         Örnek: postgresql://user:password@localhost/dbname
        """
        if database_url is None:
            # Bağlantı bilgilerinden URL oluştur
            user = os.getenv('DB_USER', 'postgres')
            password = os.getenv('DB_PASSWORD', 'kvyu8dutx')
            host = os.getenv('DB_HOST', '127.0.0.1')
            port = os.getenv('DB_PORT', '5432')
            database = os.getenv('DB_NAME', 'postgres')
            
            database_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
        
        self.database_url = database_url
        self.engine = None
        self.SessionLocal = None
    
    def connect(self):
        """
        Veritabanına bağlan
        
        Returns:
            bool: Bağlantı başarılı ise True, değilse False
        """
        try:
            self.engine = create_engine(
                self.database_url,
                echo=False,  # SQL sorgularını görmek için True yapabilirsin
                pool_pre_ping=True,  # Bağlantının hala aktif olup olmadığını kontrol et
                pool_size=10,
                max_overflow=20
            )
            
            # Session fabrikası oluştur
            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
            
            # Bağlantıyı test et
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            
            print("PostgreSQL bağlantısı başarıyla kuruldu! ✅")
            return True
        
        except Exception as e:
            print(f"Veritabanına bağlanırken hata oluştu: ❌ {e}")
            return False
    
    def disconnect(self):
        """Bağlantıyı güvenli bir şekilde kapatır."""
        if self.engine:
            self.engine.dispose()
            print("Bağlantı kapatıldı. 🔌")
    
    def get_session(self):
        """
        Yeni bir session al
        
        Returns:
            Session: SQLAlchemy session nesnesi
        """
        if self.SessionLocal is None:
            raise RuntimeError("Veritabanına henüz bağlanılmamış")
        return self.SessionLocal()
    
    @contextmanager
    def session_scope(self):
        """
        Context manager kullanarak session yönet (otomatik kapatma)
        
        Örnek:
            with db.session_scope() as session:
                user = session.query(User).filter_by(id=1).first()
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Session hatası: {e}")
            raise
        finally:
            session.close()
    
    def create_tables(self):
        """Tüm tabloları oluştur"""
        if self.engine is None:
            raise RuntimeError("Veritabanına henüz bağlanılmamış")
        
        Base.metadata.create_all(bind=self.engine)
        print("✓ Tablolar oluşturuldu")
    
    def drop_tables(self):
        """Tüm tabloları sil (DİKKATLİ KULLAN!)"""
        if self.engine is None:
            raise RuntimeError("Veritabanına henüz bağlanılmamış")
        
        Base.metadata.drop_all(bind=self.engine)
        print("✓ Tablolar silindi")