from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path(__file__).resolve(
).parent.parent.parent.parent / 'infra' / '.env')

DATABASE_URL = os.getenv("TASK_DATABASE_URL")
