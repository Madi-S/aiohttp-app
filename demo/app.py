import jinja2
import aiohttp_jinja2
import asyncpgsa
from aiohttp import web

from .routes import setup_routes

# Function that returns web application with all setups
async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    # Setup jinja
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    # Setup routes GET/POST /menu, /home, /contacts etc
    setup_routes(app)
    # Add functions that run on start
    app.on_startup.append(on_start)
    # Add functions that run in the end  (turn off)
    app.on_cleanup.append(on_shutdown)
    return app


# Function on start to connect to database
async def on_start(app):
    config = app['config']
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])


# Function on end to close the connection with database
async def on_shutdown(app):
    await app['db'].close()
