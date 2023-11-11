# 1. Корректно оформлен репозиторий – 1 балл
        # 2. Реализован путь / – 1 балл
        # 3. Реализован путь /post – 1 балла
        # 4. Реализована запись собак – 1 балл
        # 5. Реализовано получение списка собак – 1 балл
        # 6. Реализовано получение собаки по id – 1 балл
        # 7. Реализовано получение собак по типу – 1 балл
        # 8. Реализовано обновление собаки по id – 1 балл
# 9. Сервис открывается по ссылке – 1 балл
# 10. Документация совпадает с заданием – 1 балл


from enum import Enum
from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


# 2. Реализован путь / – 1 балл
@app.get('/', summary='Root')
async def root():
    # ваш код здесь
    return Response(status_code=200)


# 3. Реализован путь /post – 1 балла
@app.post('/post', summary='Get Post')
async def post(item: Dog) -> Dog:
    return item


# 4. Реализована запись собак – 1 балл
@app.post('/dog/add', summary='Add Dog')
async def post_dog(name: str, kind: DogType):
    pk = len(dogs_db)
    dogs_db.update({pk: Dog(name=name, pk=pk, kind=kind)})
    return Response(status_code=200)


# 5. Реализовано получение списка собак – 1 балл
@app.get('/dog', summary='Get All Dogs')
async def get_dogs():
    return [dogs_db[i] for i in dogs_db]


# 6. Реализовано получение собаки по id – 1 балл
@app.get('/dog/{pk}', summary='Get dog by ID')
async def get_dog_by_id(pk: int) -> Dog:
    return dogs_db[pk]


# 7. Реализовано получение собак по типу – 1 балл
@app.get('/dog/', summary='Get dog by type')
async def get_dog_by_type(kind: DogType):
    return [dogs_db[i] for i in dogs_db if dogs_db[i].kind == kind]


# 8. Реализовано обновление собаки по id – 1 балл
@app.patch('/dog/{pk}', summary='Update Dog')
async def get_dog_by_type(pk: int, name: str, kind: DogType):
    dogs_db.update({pk: Dog(name=name, pk=pk, kind=kind)})
    return Response(status_code=200)
