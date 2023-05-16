

# Where to Go - Moscow through the eyes of Artem

A website [Точки притяжения](http://taiga.pythonanywhere.com/) about the most interesting places in Moscow. Artem's author's project.

## Launch

- Download the code

- Install dependencies 

```
pip install -r requirements.txt
```

- Create a database file and immediately apply all migrations using 

```
python3 manage.py migrate
```

- Start the server:

```
python3 manage.py runserver
```
or setup your (a/w)sgi
and deploy, but i think you already knew this without me, he-he..


## Environment variables

Some project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and write data in this format: `VARIABLE = value`.

There are several variables available:
- `SECRET_KEY` - the secret key of the project - this var required.
- `DEBUG` - debug mode. Set to True to see debugging information in case of an error.

if `DEBUG`  is False, then you have to provide your own DBMS with following variables required:  

`DATABASE_ENGINE`   - mysql, postgres etc  
`DATABASE_NAME`     - database name  
`DATABASE_USER`     - user  
`DATABASE_PASSWORD` - password  
`DATABASE_HOST`     - host  
`DATABASE_PORT`     - port  

## Adding places

To display a place on the map, a [json-file](https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json) with a description is required.

For quick loading of locations on the map, you can use the command `python3 manage.py load_place <link>`.

## Project Goals

The code is written for educational purposes.
