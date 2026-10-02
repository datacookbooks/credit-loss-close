"""Connection settings for the project's local PostgreSQL database."""

import os
from collections.abc import Mapping
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, URL


def build_database_url(settings: Mapping[str, str]) -> URL:
    """Validate settings and construct a URL without manual escaping."""
    required = (
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
    )
    missing = [name for name in required if not settings.get(name)]
    if missing:
        raise ValueError(
            "Missing database settings: " + ", ".join(missing)
        )

    try:
        port = int(settings["POSTGRES_PORT"])
    except ValueError:
        raise ValueError("POSTGRES_PORT must be an integer.") from None

    if not 1 <= port <= 65535:
        raise ValueError("POSTGRES_PORT must be between 1 and 65535.")

    return URL.create(
        drivername="postgresql+psycopg",
        username=settings["POSTGRES_USER"],
        password=settings["POSTGRES_PASSWORD"],
        host=settings["POSTGRES_HOST"],
        port=port,
        database=settings["POSTGRES_DB"],
    )


def create_db_engine() -> Engine:
    """Load local settings and create an engine; connect only when used."""
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env", override=False)

    return create_engine(
        build_database_url(os.environ),
        pool_pre_ping=True,
        connect_args={"connect_timeout": 5},
        hide_parameters=True,
    )
