# django-tutorial

this repo contains the files from the following django tutorial:

https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html

only difference is that iam building it with docker.

## usage
```
git clone https://github.com/mxkle/django-tutorial.git
cd django-tutorial
docker-compose up
```

### useful commands
```
docker-compose run web ...
docker-compose up -d
docker container ls
docker-compose logs [--follow, --timestamps, --tail=linenumber|all]
```
