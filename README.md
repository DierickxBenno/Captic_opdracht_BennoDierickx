# Captic_opdracht_BennoDierickx

### In this project i have to make a dockerized environement to get metadata from pictures.
=======
In this project I have to make a dockerized environement to get metadata from pictures.

## test code
### to run main.py (outside docker) run ```uvicorn main:app --reload```

## docker
### build image: ```docker build -t [tag] .```
### run image: ```docker run -p 8000:8000 [tag]``` note that 8000 is the default port for uvicorn to run on
### you might have to disable other containers running on port 8000 or change the port in the dockerfile (to 80 for example)
=======
to run main.py (outside docker) run ```uvicorn main:app --reload```

