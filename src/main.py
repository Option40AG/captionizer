import validators

import scoring

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
    try:
        # Validate that the URL is valid
        if not (validate_url(url)):
            raise HTTPException(status_code=400, detail="Bad URL provided")
        
        # Retrieve the image from the URL as 'bytes'
        try:
            image = scoring.retrieve_image(url)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to retrieve image")
        
        # Score the image
        try:
            return scoring.score(image)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to score image")
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")