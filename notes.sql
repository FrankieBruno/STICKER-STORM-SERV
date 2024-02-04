/*Starting a server from scratch


INITIAL SETUP
make directory for application
install/run a pipenv shell
install pylint, autopep8, and django
django admin start project

pylint file and select interpereter
create .vscode and <project_name>api directories

gitignore & update settings
base django tables



WORKFLOW
Models - templates for how your data will be represented
    migrate models
        this creates empty tables for when it's time to "seed" the data
    - when loading a "user" object into your model its a foriegn key relationship

Fixtures - dummy data
    loaddata - self explanitory: they load your dummy data into the empty
    tables we made in migrations
        .fixture <-- needs to match the model classname (singular or plural [in my case, singular]) 

Tokens
    When the user first registers on the client a unique token is created for that user. The client uses the token in all fetch calls to the server to identify the user making the request.


Views
    these modules hanbdle the retrieve/list/create/update/destroy
    functionality of whatever view/resource we want to manipulate

(WITHIN VIEW)

The {{retrieve}} method will get a single object from the database based on the pk (primary key) in the url. We’ll use the ORM to get the data, then the serializer to convert the data to json. Add the following code to the retrievemethod, making sure the code is tabbed correctly:

The {{list}} method is responsible for getting the whole collection of objects from the database. The ORM method for this one is all. Here’s the code to add to the method:

The {{serializer}} class determines how the Python data should be serialized to be sent back to the client. Put the following code at the bottom of the same module as above. !!Make sure it is outside of the view class!!

{Adding the URL} So far we’ve set up the view and serializer but not which url to use for the view. We need to add a /gametypes resource to the Django application. If a client sends a GET request to either http://localhost:8000/gametypes or http://localhost:8000/gametypes/1, we want the server to respond with the appropriate method. You will use a built-in class in Django Rest called the DefaultRouter. The DefaultRouter sets up the resource for each method that is present on the view. For now, it will only respond to the GET requests to the game type resource. Add the following import statements at the top of the urls module in the level folder.

ON CLIENT SIDE:

- The StickerForm.js does the following:

It first calls in its other functions at the top. Then we call in through an {export const} that contains {use states} the functions that we want the different sections of code below to use.

in the {use effect} we are allowing our stickerForm to bring in the functions in the stickerManager that contain fetches that directly allow us to reach into the server and grab information from our databases