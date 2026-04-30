from dataclasses import dataclass


@dataclass
class AppSettings:
    debug: bool
    log_level: str

    def __post_init__(self):
        levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
        if self.log_level not in levels:
            print(f"log_level должен быть одним из: {levels}")
            self.log_level = 'INFO'


@dataclass
class DatabaseSettings(AppSettings):
    host: str
    port: int
    timeout: int

    def __post_init__(self):
        super().__post_init__()
        if not (1 <= self.port <= 65535):
            print("port должен быть в диапазоне от 1 до 65535")
            self.port = 5432


@dataclass
class APISettings(AppSettings):
    api_key: str
    rate_limit: int
    endpoint: str

    def __post_init__(self):
        super().__post_init__()
        if self.rate_limit <= 0:
            print("rate_limit должен быть больше 0")
            self.rate_limit = 100


if __name__ == "__main__":
    db = DatabaseSettings(debug=True, log_level='DEBUG', host='localhost', port=99999, timeout=30)
    api = APISettings(debug=False, log_level='INFO', api_key='secret_key', rate_limit=-5, endpoint='/v1')

    print(f"\nНастройки БД: {db}")
    print(f"Настройки API: {api}")
