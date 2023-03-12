from dependencies import app
from flask import request
from helper_functions import get_image_from_id
import logging


@app.route("/api/ReadNumber", methods=["GET", "POST"])
def get_image():  # {"image_id" : str}
    if ["image_id"] != list(request.json.keys()):
        logging.info(
            f"got result for non-correct query with keys {request.json.keys()}"
        )
        return {
            "text": "invalid format, json must look like "
            '{"image_id" : id-string or list of id-strings}'
        }, 400

    logging.info(f"got image-id from correct json ({request.json})")
    result, code = get_image_from_id(request.json["image_id"])
    return {"text": result}, code


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] [%(asctime)s] %(message)s", level=logging.INFO
    )

    app.config["JSON_AS_ASCII"] = False
    app.run(host="0.0.0.0", port=8080, debug=True)

