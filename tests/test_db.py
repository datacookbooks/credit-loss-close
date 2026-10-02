"""Tests for connection settings and an explicitly selected database check."""

import pytest
from sqlalchemy import text

from src.db import build_database_url, create_db_engine


def example_settings():
    return {
        "POSTGRES_HOST": "127.0.0.1",
        "POSTGRES_PORT": "5432",
        "POSTGRES_DB": "test_database",
        "POSTGRES_USER": "test_user",
        "POSTGRES_PASSWORD": "example@password:with/symbols",
    }


def test_password_characters_are_preserved():
    settings = example_settings()
    url = build_database_url(settings)

    assert url.password == settings["POSTGRES_PASSWORD"]
    assert url.drivername == "postgresql+psycopg"
    assert url.port == 5432


def test_missing_password_is_rejected():
    settings = example_settings()
    del settings["POSTGRES_PASSWORD"]

    with pytest.raises(ValueError, match="POSTGRES_PASSWORD"):
        build_database_url(settings)


@pytest.mark.database
def test_database_connection():
    engine = None
    try:
        engine = create_db_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).scalar_one()
    except Exception as error:
        pytest.fail(
            "Database connection failed "
            f"({type(error).__name__}). "
            "Check Docker health and local .env settings.",
            pytrace=False,
        )
    finally:
        if engine is not None:
            engine.dispose()

    assert result == 1
