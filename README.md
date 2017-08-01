# CEA Fullstack Developer Trial Task
## Installation
These instructions are for macOS.
### Python
1.  Python 3.6
    `brew install python3`
2.  Setup your Vitual Environment
    ```
    cd /PATH/TO/gwwc
    virtualenv -p python3 venv
    . venv/bin/activate
    ```
3.  `requirements.txt` contains the Python packages we depend on.
    `pip install -r requirements.txt`
### Postgres
These instructions are for how I have it setup, see <https://gist.github.com/sgnl/609557ebacd3378f3b72> to maybe avoid a double install.
1.  Download postgres via GUI
    From here: <http://postgresapp.com/>
2.  Install cli tools
    `brew install postgresql`
## Secrets
1.  Ask me to send you a `secrets.yaml` to put in the top level directory.
## Setup your database
1.  Using the psql cli, create a new database, (and optionally new user and password).
2.  Edit the DATABASES entry in `gwwc_backend/gwwc_backend/settings.py` to reflect the database name, user and password that you have.
3.  Run the database migrations that shipped with this repo.
    ```
    cd gwwc_backend
    python manage.py migrate
    ```
## Load data
1.  Load dummy data.
    `python load_dummy_data.py dummy_data.yaml`
2.  Create admin, who can go to <url>/admin and edit data.
    `python manage.py createsuperuser`
## You're good to go!
`python manage.py runserver`
