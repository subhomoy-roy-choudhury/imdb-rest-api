# IMDB RestAPI Clone

IMDB RestAPI Clone is a set of restapi similar to IMDB APIs

## Tech Stack
- python : 3.9.12
- Django 
- Heroku (Deployment)

## Features

- Search movies based on their their names
- Customised Admin Panel 

##  Setup :- 
- Cloning the repository
`git clone https://github.com/subhomoy-roy-choudhury/imdb-rest-api.git`
- Creating Virtual Environment
`python -m virtualenv my-environment-name`
- Activate Virtual Environment
`./my-environment-name/Scripts.activate`(for Windoes Users)
`my-environment-name/bin/activate`(for linux/mac users)
- Installing requirements
`python -m pip install -r requirements.txt`
- heroku deployment
`git push heroku master`
`heroku ps:scale web=1`

## API Functionality
- ### Admin :- 
```
Admin URL :- https://imdb-rest-api-v2.herokuapp.com/admin/backend/genre/
Swagger URL :- https://imdb-rest-api-v2.herokuapp.com/swagger/
--> From here admin can add, remove or edit movies 
```
- ## User :- 
```
https://imdb-rest-api-v2.herokuapp.com/api/movie (for viewing all movies)
https://imdb-rest-api-v2.herokuapp.com/api/movie?search_query={name/director}&limit=10&offset=0 (search movie by name/director)
```
