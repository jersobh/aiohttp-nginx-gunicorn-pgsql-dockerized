from views import render

async def index(request):
    data = {}
    status = 200
    return await render.json(data, status)


async def jsonExample(request):
    data = {}
    data['name'] = 'Jhonny'
    data['surname'] = 'test'
    status = 200
    return await render.json(data, status)
