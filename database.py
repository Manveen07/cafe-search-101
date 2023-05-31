from sqlalchemy import create_engine,text
import os
conect_string=os.environ["CONECTSTR"]

engine=create_engine(conect_string,connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }})

def load_cafes_from_db():
  row_as_dict = []
  with engine.connect() as conn:
    result = conn.execute(text("select * from cafes"))
    rows = result.fetchall()
    for row in rows:
      row_as_dict.append(dict(row))
    return row_as_dict
def load_cafe_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text("select * from cafes where id = :id"),id=id)
    return result.fetchall()
def add_cafe_to_db(data):
  with engine.connect() as conn:
    result=conn.execute(text("INSERT  INTO cafes(id,name,map_url,img_url,location,has_sockets,has_toilet,can_take_calls,seats,coffee_price) values(:id,:name,:map_url,:img_url,:location,:has_sockets,:has_toilet,:can_take_calls,L:seats,:coffe_price)"),id=id,name=data["name"],map_url=data["map_url"],img_url=data["img_url"],location=data["location"],has_sockets=data["has_sockets"],has_toilet=data["has_toilet"],can_take_calls=data["can_take_calls"],seats=data["seats"],coffe_price=data["coffee_price"])

def add_review_for_cafe_to_db(id,data):
  with engine.connect() as conn:
    result=conn.execute(text("INSERT INTO review (id,name,email,review,rating) VALUES (:id,:name,:email,:review,:rating)"),id=id,name=data["full_name"],email=data["email"],review=data["review"],rating=data['rating'])
result=load_cafes_from_db()
print(result)