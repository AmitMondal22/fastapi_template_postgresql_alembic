# Alembic Environment Configuration

This `env.py` file is part of the Alembic migration tool for SQLAlchemy. It configures the migration environment for your database schema changes. This document provides an overview of the `env.py` script and instructions on how to use it.

## Overview

The `env.py` script sets up the Alembic migration environment, including configuration, metadata handling, and migration execution modes.

### Components

- **Logging Configuration:**
  The script sets up logging based on the configuration file specified in `config.config_file_name`. Logging helps to debug and trace migration operations.

- **Metadata:**
  The `target_metadata` is set to the metadata of your SQLAlchemy `Base` class. This is used by Alembic to detect changes in your models and generate migration scripts.

- **Include Object Function:**
  The `include_object` function determines which database objects are included in migrations. It skips `ENUM` types to prevent duplication.

- **Migration Modes:**
  - **Offline Mode:** Runs migrations by configuring the context with a URL. No database connection is required.
  - **Online Mode:** Runs migrations by creating an `Engine` and associating a connection with the context. This is used for executing migrations with a live database.

### Functions

- `run_migrations_offline()`
  Configures the context for offline migration mode and runs migrations.

- `run_migrations_online()`
  Configures the context for online migration mode and runs migrations.

### Configuration

- **SQLAlchemy URL:**
  The `sqlalchemy.url` option in your Alembic configuration file (`alembic.ini`) specifies the database URL.

- **Metadata:**
  Ensure that the `Base` class from your `models` module is imported and assigned to `target_metadata`.

- **Include Object Function:**
  Customize the `include_object` function to control which database objects are included in the migration process.

## Usage

1. **Initialize Alembic:**
   If you haven't already, initialize Alembic in your project with `alembic init`.

2. **Generate Migrations:**
   Use `alembic revision --autogenerate -m "description"` to create a new migration script based on changes in your models.

3. **Apply Migrations:**
   Run `alembic upgrade head` to apply migrations to your database.

4. **Downgrade Migrations:**
   Use `alembic downgrade -1` to revert the last migration if needed.

## Customization

- Modify the `include_object` function if you need to include or exclude specific database objects from the migration process.
- Update `target_metadata` if your `Base` class or models are in different modules.

## Troubleshooting

- Ensure that all model imports are correct.
- Verify that the `sqlalchemy.url` is properly configured in `alembic.ini`.
- Check the logs for any errors during migration execution.

For more information, refer to the [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/).
