from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

users = [
    {'id' : 1 , 'name':'Makar'},
    {'id' : 2 , 'name':'Yuri'},
    {'id' : 3 , 'name':'Alex'}
]

@app.get('/users/{user_id}')
def get_username(user_id : int):
    return [user for user in users if user.get('id') == user_id]

@app.post('/users/{user_id}')
def change_username(user_id : int, new_name : str):
    current_user = list( filter( lambda user : user.get('id') == user_id, users ) )[0]
    current_user['name'] = new_name
    return {'status' : 200, 'data' : current_user}

@app.get('/hello')
def hello():
    return 'Hello world!'


fake_trades = [
    {'id' : 1, 'user_id':1, 'currency':'Nan1', 'line':'line1', 'price':20, 'amount':10},
    {'id' : 2, 'user_id':2, 'currency':'Nan2', 'line':'line2', 'price':19, 'amount':12}
]
class Trade(BaseModel):
    id : int
    user_id : int
    currency : str = Field(max_length=5)
    line : str
    price : float = Field(ge=0)
    amount : float

@app.post("/trades")
def traids(trades : List[Trade]):
    fake_trades.extend(trades)
    return {'status':200, 'data' : fake_trades}


