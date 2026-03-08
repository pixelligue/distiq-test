import os
import subprocess

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY") # Загружаем из переменных окружения
DB_PASSWORD = os.environ.get("DB_PASSWORD") # Загружаем из переменных окружения

def run_command(command_parts: list[str]) -> int:
    """Исполняет команду, безопасно используя список аргументов.

    Избегает shell=True для предотвращения Command Injection.
    """
    # Вместо этого используйте subprocess.run с list-формой для command_parts
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr: print(result.stderr)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return e.returncode
def get_user(user_id: int) -> tuple | None:
    """Возвращает пользователя по ID из базы данных, используя параметризованный запрос.

    Возвращает кортеж с данными пользователя или None, если пользователь не найден.
    """
    import sqlite3
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
# import logging # Предполагаем использование стандартного модуля logging как замену structlog для примера

# Настройка логирования, которая должна быть в отдельном файле или в инициализации приложения
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
def log_message(msg: str) -> None:
    """Логирует сообщение, используя настроенную систему логирования (например, structlog/logging)."""
    # В реальном приложении здесь будет использоваться structlog.get_logger()
    # Например: logger.info(msg)
    print(f"LOG: {msg}")