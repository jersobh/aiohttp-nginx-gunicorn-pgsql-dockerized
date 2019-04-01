from controllers import controller

def routes(app):
    app.router.add_get('/', controller.index)
    app.router.add_get('/users', controller.users)
