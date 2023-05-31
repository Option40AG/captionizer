from transformers import AutoProcessor, AutoModelForCausalLM
import requests
import torch
from PIL import Image

def score(image: bytes):

    # Use assets of the model from the local filesystem
    processor = AutoProcessor.from_pretrained("./../model/git-base-textcaps")

    if torch.cuda.is_available():
        print("Running on cuda")
        device = torch.device("cuda")
        model = AutoModelForCausalLM.from_pretrained("./../model/git-base-textcaps").to(device)
    else:
        print("Running on cpu")
        device = torch.device("cpu")
        model = AutoModelForCausalLM.from_pretrained("./../model/git-base-textcaps").to(device)

    pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

    generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_caption

def retrieve_image(url: str):
    try:
        return Image.open(requests.get(url, stream=True).raw)
    except Exception as e:
        raise e