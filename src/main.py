import validators
from transformers import AutoProcessor, AutoModelForCausalLM
import requests
from PIL import Image

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

def validate_url(url):
    if validators.url(url):
        return True
    else:
        return False
    
app = FastAPI()
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="GET",
    allow_headers=["*"]
)

@app.get("/captionize")
def get_endpoint(url: str):
    if not (validate_url(url)):
        raise HTTPException(status_code=400, detail="Bad URL provided")
    
    caption = inference(url)
    return caption
    
def inference(url: str):
    try:
        processor = AutoProcessor.from_pretrained("./model/git-base-textcaps")
        model = AutoModelForCausalLM.from_pretrained("./model/git-base-textcaps")

        image = Image.open(requests.get(url, stream=True).raw)

        pixel_values = processor(images=image, return_tensors="pt").pixel_values

        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_caption
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")