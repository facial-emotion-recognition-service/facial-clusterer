# 1 Repo Outline
The code in this repo will, given a group of images containing people's faces, cluster faces of the same person together for all faces.

# 2 How to Use
In this section we go over how to deploy the face clusterer in a docker container and use it.  

1. Make sure Docker and Docker Compose are installed and that the Docker daemon is running.
2. Clone this repo.
3. `cd` into the project/repo directory and build the docker image using `docker build -t facial-clusterer .`.
4. Once the docker image is built successfully, run the container with `docker run -p 8000:8000 facial-clusterer`.
5. To use the clusterer, copy the images that you want clustered to the directory `/facial_clusterer/input_images/faces/` on the container.  
   **Note 1:** The images must be images of _isolated faces_.  
   **Note 2:** Files can be copied to a running container from the host using the `docker cp` command.  
   Example: `docker cp myface.jpg 4b09:/facial_clusterer/input_images/faces/` copies the file `myface.jpg` from the current directory on the host to the `/facial_clusterer/input_images/faces/` directory on the container with an ID that starts with `4b09`. (You can specify the full container ID or just the first few characters in docker commands). You can get the running container's ID with `docker container ls` or `docker ps`.  
   **Note 3:** `docker cp` can only copy one file or directory at a time. To copy multiple files, either copy the entire directory containing them, or use bash `for` loops. E.g. `for f in ./faces/*.jpg; do docker cp $f 4b09:/facial_clusterer/input_images/faces/; done`.
7. Navigate your browser to `http://0.0.0.0:8000/clusters`. If you get `None` in response, that means there were no errors. The results will be written to `/facial_clusterer/output_json/clusters.json` on the running container.
8. To stop the running container use the command `docker kill 4b09` (replacing `4b09` with the correct container ID).

**A note on environment variables:** The environment variables defined via the `ENV` directive in `Dockerfile` will be ignored and overridden by the `environment` section of the Docker Compose YAML file if you run the container via that route. Please do not edit the `Dockerfile`.
