from io import BytesIO
from typing import List, TypeGuard, Any
from functools import singledispatch
import traceback
import requests
import logging
from dependencies import IMAGES_LINK, PLATE_READER


def get_image_binary(image_id: str) -> BytesIO:
    response = requests.get(IMAGES_LINK + image_id)

    if response.status_code >= 500:
        logging.error(
            f"Downloading image {image_id} "
            f"crashed with status {response.status_code}"
        )
        raise ConnectionError(f"downloading image "
                              f"crashed, {response.status_code}")

    if (400 <= response.status_code) and (response.status_code < 500):
        logging.error(
            f"invalid image-id {image_id} "
            f"crashed with status {response.status_code}"
        )
        raise ConnectionError(f"invalid image-id, {response.status_code}")

    return BytesIO(requests.get(IMAGES_LINK + image_id).content)


def is_str_list(elements: List[Any]) -> TypeGuard[List[str]]:
    return all(isinstance(element, str) for element in elements)


@singledispatch
def get_image_from_id(image_id_obj):
    logging.info(f"got result for non-correct image_id object {image_id_obj}")
    return "image_id must be a string", 400


@get_image_from_id.register(str)
def _(image_id: str):
    try:
        img = get_image_binary(image_id)
        result = PLATE_READER.read_text(img)

    except ConnectionError as e:
        message, code = str(e).split(",")
        return message, int(code)

    except Exception:
        logging.error(traceback.format_exc())
        return "something went wrong", 501

    logging.info(f"got result {result} for image_id {image_id}")
    return result, 200


@get_image_from_id.register(list)
def _(image_ids: list):
    results, codes = map(
        list, zip(*[get_image_from_id(image_id) for image_id in image_ids])
    )
    logging.info("got result for list of image ids")
    return results, max(codes) if any(code != 200 for code in codes) else 200

