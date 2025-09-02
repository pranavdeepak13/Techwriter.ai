from rich.console import Console
from rich.logging import RichHandler
import logging

console = Console()

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[RichHandler(console=console)]
)

logger = logging.getLogger("blog-writer")

def log_info(msg): logger.info(msg)
def log_warn(msg): logger.warning(msg)
def log_error(msg): logger.error(msg)
