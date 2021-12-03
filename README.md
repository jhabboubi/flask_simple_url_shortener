# Simple Flask Application 
## Creating a simple URL Shortener Flask Application
- Technologies:
  - Python 3.9.7
  - pip 21.2.4 
  - Basic HTML

|MacOs/Linux|Windows|
|:---:|:---:|
|Terminal|Command Prompt|
|`ls`|`dir`|
|`pwd`|`echo %cd%`|
|`export FLASK_APP=hello`|`set FLASK_APP=hello`|
|path use `/`|path use `/`|


## Installing flask and pipenv
- change directory to flask_simple_url_shortener 
- mac and linux users in terminal `pip3 install pipenv`
- windows users in gitbash or powershell `pip install pipenv`
- `pipenv install` to create pipfile.lock to hold all packages
- to enter virtual environment `pipenv shell` and to exit the virtual environment `exit` to go back to your terminal
- make sure you are in the virtual environment by again the command `pipenv shell` if you are already in the virtual environment then the console will print `already activated.` message
- to install flask on the virtual environment `pipenv install flask`
- ensure flask installed by simply running the command `flask`

## Create first route in a flask app
- create hello.py and write some code
- to run the project in the virtual environment type for mac users `export Flask_APP=hello` / windows users `set FLASK_APP=hello` then `flask run` and that will run the server on http://127.0.0.1:5000/ or http://localhost:5000
- Note: if you change code in hello.py now then you should CTRL + C to exit the server then in terminal `flask run` so the server refreshes the content
- instead of stopping the server every time the code changes we could change the environment from production to development. Stop the server by hitting CTRL + C and type `export FLASK_ENV=development` and that will refresh the server automatically each time the code changes and file is saved. 
- Note: opening a new terminal session means you must redefine `FLASK_ENV=development` and `FLASK_APP=hello` but we could save a step by just renaming the application to `app.py` and flask will recognize  
## Page templates in flask with Jinja
  - create templates folder on same path of project, this folder will be looked up by flask to render html pages
  - `import render_template` in app.py then specify render_template('HTML_FILE.html')
  - to pass variables to jinja add variables as a argument after HTML file e.g. `return render_template('HTML_FILE.html', name='jafer')` in the function desired at app.py
  - make a form with two fields for url and code(shortener) to the url using POST method