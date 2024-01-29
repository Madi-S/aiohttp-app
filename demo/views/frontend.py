import aiohttp
from sqlalchemy import select
from sqlalchemy.sql import text
from aiohttp_jinja2 import template

from .. import db


@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}
    # return aiohttp.web.Response(text='Ok')


@template('contact_section.html')
async def contact_section(request):
    return {}


async def post(request):
    async with request.app['db'].acquire() as conn:
        query = select([db.post.c.id, db.post.c.title])
        print(query)
        # query = select([db.post])
        # query = text('select * from post;')
        result = await conn.fetch(query)

    return aiohttp.web.Response(body=str(result))
