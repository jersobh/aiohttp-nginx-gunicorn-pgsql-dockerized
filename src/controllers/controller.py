from views import render
import models

async def index(request):
    data = "Hello World!"
    status = 200
    return await render.raw(data, status)


async def users(request):
    data = []
    count_users = await models.objects.count(models.User.select())
    users = await models.objects.execute(models.User.select().dicts())

    if count_users == 0:
        user0 = await models.objects.create(models.User, username='test1', password='123', email='test1@test.com')
        user1 = await models.objects.create(models.User, username='test2', password='123', email='test2@test.com')
        user2 = await models.objects.create(models.User, username='test3', password='123', email='test3@test.com')
        users = await models.objects.execute(models.User.select().dicts())

    for user in users:
        u = {}
        u['username'] = user['username']
        u['email'] = user['email']
        u['created_on'] = user['created_on'].strftime("%d/%m/%Y, %H:%M:%S")
        u['last_login'] = user['last_login'].strftime("%d/%m/%Y, %H:%M:%S")
        data.append(u)

    status = 200
    return await render.json(data, status)
