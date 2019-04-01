from views import render
import models

async def index(request):
    data = []
    users = await models.objects.execute(models.User.select().dicts())
    print(users)
    if users is None:
        user0 = await models.objects.create(models.User, username='test1', password='123', email='test1@test.com')
        user1 = await models.objects.create(models.User, username='test2', password='123', email='test2@test.com')
        user2 = await models.objects.create(models.User, username='test3', password='123', email='test3@test.com')
        users = await models.objects.execute(models.User.select().dicts())

    for user in users:
        u={}
        u['username'] = user['username']
        u['email'] = user['email']
        data.append(u)
        
    status = 200
    return await render.json(data, status)


async def json_example(request):
    data = {}
    data['name'] = 'Jhonny'
    data['surname'] = 'test'
    status = 200
    return await render.json(data, status)

