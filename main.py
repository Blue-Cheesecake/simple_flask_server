from typing import Dict
from flask import Flask
from flask_restful import Api, Resource, reqparse
from db import users, videos

# Create App and API
app = Flask(__name__)
api = Api(app)
usersData = users.data
videosData = videos.data


class HelloWorld(Resource):
  """The Resource which can use get, put, post, delete method

  Args:
      Resource (_type_): 
  """

  def get(self):
    return {
        "data": "Hello World"
    }


class HelloName(Resource):
  def get(self, name: str):

    if name in usersData:

      return {
          "name": name,
          "data": usersData.get(name),
      }

    return {"message": "fail"}


# Create parameters for passing input to PUT, POST
video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="<Name> of the video is required", required=True,)
video_put_args.add_argument(
    "views", type=int, help="<Views> of the video is required", required=True)
video_put_args.add_argument(
    "likes", type=int, help="<Likes> on the video is required", required=True)


class Video(Resource):
  def get(self, video_id: int) -> Dict:
    if video_id not in videosData:
      return {"result": "fail"}
    # Response
    return {
        "result": "success",
        "data": {
            "id": video_id,
            "info": videosData[video_id],
        }
    }

  # Putting and Posting work same thing

  def put(self, video_id: int) -> Dict:
    # Passing received arguments
    args = video_put_args.parse_args()

    videosData[video_id] = args
    # Response
    return {"result": "success"}

  def post(self, video_id: int) -> Dict:
    args = video_put_args.parse_args()

    # if video_id in videosData:
    #   return {"result": "fail"}

    videosData[video_id] = args
    return {"result": "success"}


# Register new Resource to URL
api.add_resource(HelloWorld, "/helloworld")
api.add_resource(HelloName, "/helloname/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
  app.run(debug=True)
