from views import render
import models
from playhouse.shortcuts import model_to_dict, dict_to_model

async def index(request):
    data = {}
    users = await models.objects.get(models.User.select().dicts())

    if users is None:
        user0 = await models.objects.create(models.User, username='test1', password='123', email='test1@test.com')
        user1 = await models.objects.create(models.User, username='test2', password='123', email='test2@test.com')
        user2 = await models.objects.create(models.User, username='test3', password='123', email='test3@test.com')
        users = await models.objects.get(models.User.select().dicts())

    print(users)
    status = 200
    return await render.json(data, status)


async def json_example(request):
    data = {}
    data['name'] = 'Jhonny'
    data['surname'] = 'test'
    status = 200
    return await render.json(data, status)

