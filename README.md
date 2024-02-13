# Source
This was copied from Stelios's repo -> https://github.com/cajal/at-image.git

# To extract
The function in the pipeline that runs a rigid, affine, and nonrigid slice to volume registration. should be here -> (https://github.com/cajal/pipeline/blob/55a68e7404490a730bddba6051ef51aaced76a4e/python/pipeline/stack.py#L1637)

# at-image
image processing and registration utilities of the Tolias Lab

Requirements
- Docker [link](https://www.docker.com/)
- docker compose [link](https://docs.docker.com/compose/)

To deploy image and launch into jupyterlab:

1. clone repository
2. navigate to the deploy folder
3. in terminal run:
```bash
docker compose build jupyterlab
```
On the first time it will take several minutes to download the Docker image and build. 

4. in the deploy folder add an empty file called `.env`

5. Optional

    In the .env file the following environment variables can be added:

        `JUPYTER_PORT_CONTAINER=8888` # desired port w/o this variable the default is 8888
        `JUPYTER_PASSWORD=some password` # desired password for jupyterlab
6. in terminal run:
```bash
docker compose up -d jupyterlab
```
7. In browser, navigate to `localhost:8888` or to whatever port set with `JUPYTER_PORT_CONTAINER` if changed from the default
