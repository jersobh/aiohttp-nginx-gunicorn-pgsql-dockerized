from aiohttp import web
from core.router import routes
from core.conf import *

async def factory():
    app = web.Application()
    routes(app)
    return app
    # web.run_app(app, host='0.0.0.0', port=APP_PORT)

