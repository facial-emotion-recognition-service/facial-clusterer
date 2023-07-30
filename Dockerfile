FROM python:3.10-buster

RUN apt-get -y update && apt-get install -y build-essential cmake libgl1

ADD facial_clusterer ./facial_clusterer

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip
RUN pip install .

EXPOSE 8000

WORKDIR /facial_clusterer
RUN mkdir -p input_images/faces
RUN mkdir output_json

WORKDIR /facial_clusterer/interface
ENV IMAGE_INPUT_DIR="../input_images/"
ENV JSON_OUTPUT_DIR="../output_json/"
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
