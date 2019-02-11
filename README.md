En Mac OS hay que correr sobre docker machine

https://stackoverflow.com/questions/44084846/cannot-connect-to-the-docker-daemon-on-macos

Teniendo instalado virtualbox y dockers en macos, se ejecuta para crear una vm

docker-machine create --driver virtualbox default

luego se setea el entorno (es como configurarlo en el ambiente actual de dockers)

eval "$(docker-machine env default)"

y luego vemos si está corriendo

docker ps

Construyendo la imagen del proyecto

Esta imagen se basa en Linux Alpine y Python, se pondrà el còdigo en un directorio /code y luego se ejecuta el app.py, hay que estar situado dentro del directorio del proyecto:

docker build -t inukisoft/crud-angular-ionic-example .

Luego corriendo la imagen, asociando al puerto 3000 (interior del contenedor) con un puerto 6666 de nuestro host, tendríamos: 

docker run -p 6666:3000 --name crud-angular-ionic-example inukisoft/crud-angular-ionic-example

Usar localhost en vez de la ip de la máquina.

Ya que se corre dentro de una imagen virtualbox, hay que hacer un 2do reenvío de puertos ... el primero es del aplicativo a dockers, y ahora es de dockers a virtualbox, el tercero es de virtualbox hacia el host (macosx)

Según el sitio https://www.jhipster.tech/tips/020_tip_using_docker_containers_as_localhost_on_mac_and_windows.html , primero se baja dockers, luego se baja máquina virtual y se abre virtual box, se agregan los port forwarding requeridos. La ip de host debe ir 0.0.0.0 para que tome 'localhost', si pone 127.0.0.1 localhost serà ignorado. 

docker-machine stop default     # Your Docker machine name may not be default, in this case change the name accordingly

Luego se inicia

docker-machine start default

eval $(docker-machine env default)

Y se vuelve a ejecutar la imagen (docker run)

Pasamos de esto http://192.168.99.100:8888/test-ds-eap5/nuble001/PE/1/1 a esto http://localhost:8888/test-ds-eap5/nuble001/PE/1/1

