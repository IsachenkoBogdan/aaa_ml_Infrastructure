from models.plate_reader import PlateReader
from flask import Flask

app = Flask(__name__)
IMAGES_LINK = "http://51.250.83.169:7878/images/"
PLATE_MODEL_FILE_PATH = "./model_weights/plate_reader_model.pth"
PLATE_READER = PlateReader.load_from_file(PLATE_MODEL_FILE_PATH)

