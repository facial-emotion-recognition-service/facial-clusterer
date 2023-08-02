FROM python:3.10-buster

RUN apt-get -y update && apt-get install -y build-essential cmake libgl1

ADD facial_clusterer ./facial_clusterer

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip
RUN pip install .

# This section only applies when running the container in standalone mode.
# When docker-compose is used, the `environment` section of docker-compose.yml
# takes precendence over the `ENV` commands below.
WORKDIR /facial_clusterer
RUN mkdir -p input_images/faces
RUN mkdir output_json
ENV IMAGE_INPUT_DIR="../input_images/"
ENV JSON_OUTPUT_DIR="../output_json/"

EXPOSE 8000
WORKDIR /facial_clusterer/interface
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
