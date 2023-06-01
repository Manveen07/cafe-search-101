from dotenv import load_dotenv
load_dotenv()
import os
import pymysql
import ssl
connection = pymysql.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  database= os.getenv("DATABASE"),
ssl={'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}}
)
def to_dict(query):
  cursor = connection.cursor()
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  result = []
  columns = [column[0] for column in cursor.description]  # Get the column names
  for row in rows:
    row_dict = dict(zip(columns, row))
    result.append(row_dict)
  return result


def load_cafes_from_db():
  query='SELECT * FROM cafes'
  return to_dict(query)
def load_cafe_from_db(id):
  query=f"select * from cafes where id = {id}"
  return to_dict(query)
def add_cafe_to_db(id,data):
  query=f"INSERT  INTO cafes(id,name,map_url,img_url,location,has_sockets,has_toilet,can_take_calls,seats,coffee_price) values({id},{data['name']},{data['map_url']},{data['img_url']},{data['location']},{data['has_sockets']},{data['has_toilet']},{data['can_take_calls']},{data['seats']},{data['coffee_price']})"
  return to_dict(query)
def add_review_for_cafe_to_db(id,data):
  query=f"INSERT INTO review (id,name,email,review,rating) VALUES ({id},{data['full_name']},{data['email']},{data['review']},{data['rating']})"
  return to_dict(query)
