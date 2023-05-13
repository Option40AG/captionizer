# Intro

This is the sample code used inthe blog post:

# Prerequisites

Ensure you have LFS installed so you can also get the fully-trained GIT model from Microsoft.

Then, initialize LFS:

```
git lfs install
```

# Build Docker image

You will need your own Azure Container Registry to do this. Substitute the names below as required:

```
docker build . -t option40.captionizer
docker tag option40.captionizer o4images.azurecr.io/option40.captionizer:latest
docker push o4images.azurecr.io/option40.captionizer:latest
```

# Run the Docker Image

```
docker run -p 8000:8000 option40.captionizer
```

Once this is running, send a request to it like this:

```
GET http://127.0.0.1:8000/captionize?url=https://option40.com/uploads/pexels-photo-4968660.jpeg

Response: "a woman holds up a fan of money that says \" 20 cents \"."
```

# Publish the Docker image to an Azure Container app

See the content of [IAC file](iac/provision.azcli)