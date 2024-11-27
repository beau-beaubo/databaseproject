# Non-profit Organization
Our website serves as a hub for managing and sharing insight information about nonprofit events. 
We collect event, volunteers, and organizations.


## Installation
1. Clone the repository
```commandline
git clone https://github.com/beau-beaubo/databaseproject.git
```

2. Navigate to the project directory
```commandline
cd nonprofit
```

3. Create a virtual environment
```commandline
python3 -m venv env
```

4. Activate the virtual environment
    * On MS Window use
   ```commandline
    \env\Scripts\activate
   ```
   * On macOS and Linux use
   ```commandline
    source env/bin/activate
   ```

5. Run migrations
```commandline
python3 manage.py migrate
```

6. Install data from data fixtures
```commandline
python3 manage.py loaddata data/nonprofit-v4.json
```

## Running the Application

default server is [localhost:8000](http://localhost:8000/)
```commandline
python3 manage.py runserver
```

## Demo Admin
| username | password  |
|---------|-----------|
| admin   | admin1234 |
