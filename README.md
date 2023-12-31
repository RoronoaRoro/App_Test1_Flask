# App_Test1_Flask
## Description:
Flask-based web app developed using a public template for some design details as part of my coursework in the course "Desarrollo de Aplicaciones Web" during my fourth year at the university. Its purpose is to facilitate the process of requesting and donating items such as fruits and vegetables, with a focus on promoting sustainability.

## Information:
The design of this test web app was based on an existing template (https://templatemo.com/tm-564-plot-listing), but a lot of changes were done and the only thing that kept alive is the header. Versions and libraries used in the development are described in requirements.txt. About the project itself, in ```static -> css``` and ```static -> js``` there is a folder called 'OwnFiles' that is the one where every new aspect different than the ones in the original template are. Finally, on utils can be found server validations and tests of it.

## Project structure
The files are organized as follows:

* 'templates' folder contains all the HTML files.
* 'static' contains all design-related files.
* 'utils' contains everything related to the database and validations.
* 'Views' has images of all the various views of the application.
* Lastly, 'VIEWS.md' is relevant as it provides a detailed explanation of the logic behind all the interfaces.

## Important aspects to run:
Connection to the mysql database is in ```utils -> db.py```. There is all the database's connection info, and every file uploaded when someone adds a donation in the app, is stored in ```static -> uploads```. Now, to fulfill the requirements exposed in requirements.txt, this can be done:

1. First, open a pwsh terminal and create a virtual environment in parallel of the github project, this with:  
    ``` 
    python -m venv venv
    ```
2. Next, to activate the virtual environment:
    ```
    venv/bin/activate
    ```
3. Then, just install every necessary library:
    ``` 
    pip install flask  
    pip install flask_cors  
    pip install flask_paginate  
    pip install filetype  
    pip install pymysql  
    ```
4. Finally, to run the project, write this in the terminal at the level of the project:
    ```
    flask run --debug
    ```

## About database creation:
To run the project, it's useful to have MySQL WorkBench, and there using localhost as server create a new connection. Done that, to create the schema and tables needed, just running the sql sentence in ```utils -> db_creationSentences -> DBcreation.sql``` is enough. Now that the schema and tables are created, with the other sql sentence: region-comuna.sql, all regions and communes can be loaded in the database. The setup is ready, and the only thing that left is to create the user with the data that can be seen at the beginning of the db.py file. Anyway, it can be done running the last of the sentences, the one in 'user_creation.sql'.