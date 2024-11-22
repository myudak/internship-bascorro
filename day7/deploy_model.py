import roboflow
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")

rf = roboflow.Roboflow(api_key=API_KEY)
project = rf.workspace().project("red-ball-finder-bnjzk")

version = project.version(3)
version.deploy("yolov5", "training1", "model.pt")
