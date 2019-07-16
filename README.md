# docker_file_example

# Para crear el container
docker build -t my_python_process .

# para correr el container
docker run  --mount source=host_path_images,target=/images,type=bind my_python_process

# Para copiar la solucion del container a la maquina host
sacar el container_id haciendo docker ps -a
docker cp containerid:/solution.csv ./solution.csv
