from transformers import AutoProcessor, AutoModelForCausalLM
import requests
from PIL import Image

def score(image: bytes):
    processor = AutoProcessor.from_pretrained("./../model/git-base-textcaps")
    model = AutoModelForCausalLM.from_pretrained("./../model/git-base-textcaps")

    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_caption

def retrieve_image(url: str):
    try:
        return Image.open(requests.get(url, stream=True).raw)
    except Exception as e:
        raise e