import logging
from logging.config import fileConfig


from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context


from sqlalchemy.dialects.postgresql import ENUM

# Import your Base and all models here
from config.database import Base # Import your Base class
from app.models.UserModel import  User # Replace 'your_module_name' with the actual module names
from app.models.ClientModel import  ClientModel # Replace 'your_module_name' with the actual module names



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config



# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support

# from app.models.ClientModel import Base as ClientBase
# target_metadata = mymodel.Base.metadata
# target_metadata = None
# target_metadata = [Base.metadata]
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.




def include_object(object, name, type_, reflected, compare_to):
    """
    A callable that controls which objects are included in autogenerate.
    """
    # Skip ENUM types to prevent duplicate creation
    if isinstance(object, ENUM):
        return False

    return True





def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata, 
            include_object=include_object  # Use the custom include_object function
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
