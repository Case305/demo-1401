class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.username = "admin"
        self.password = "admin123"

    def connect(self):
        print("Connecting to database...")
        print(f"Host: {self.host}")
        print(f"User: {self.username}")
        print(f"Password: {self.password}")

def main():
    db = DatabaseConfig()
    db.connect()

main()
