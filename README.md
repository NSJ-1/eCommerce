# Django eCommerce Application

This project is a Django REST API for managing stores and products. 
The application allows users to add stores, add products, retrieve products, and view external products.


## 1. Clone Project

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd ecommerce_project
```


## 2. Create Virtual Environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment.

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```


## 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```


## 4. Create Database

Open MySQL or MariaDB:

```bash
mysql -u root -p
```

Create the database:

```sql
CREATE DATABASE ecommerce;
```

Exit MySQL:

```sql
exit
```


## 5. Update Settings

Open the settings file:

```
ecommerce_project/settings.py
```

Ensure the database configuration looks like:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```


## 6. Configure Email Backend

In `settings.py`, add the following email configuration:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@example.com"
```

This allows for emails to be printed in the console during development.


## 7. Apply Migrations

Run migrations to create database tables:

```bash
python manage.py migrate
```


## 8. Run Development Server

Start the Django server:

```bash
python manage.py runserver
```


## 9. Open Application

Open your browser and search:

```
http://127.0.0.1:8000/
```

Should see the default landing page of the eCommerce app.

## Testing the API

After running the development server, the landing page will open at:

http://127.0.0.1:8000/

The API endpoints listed below can be tested directly in the browser.

## API Endpoints

| Endpoint | Method | Description |
|--------|--------|--------|
| `/get/stores/` | GET | Retrieve all stores |
| `/add/store/` | POST | Add a store |
| `/get/products/` | GET | Retrieve all products |
| `/add/product/` | POST | Add a product |
| `/external/products/` | GET | Retrieve external products |


## Author

Nadia
