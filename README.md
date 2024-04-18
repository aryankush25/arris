# Arris Dashboard

This project is an AI-powered, Reflex-based dashboard application for generating and managing pages in Shopify stores. Reflex is a powerful, open-source platform for building web applications. It provides a user-friendly interface for store owners to streamline their operations.

## Installation

Follow these steps to install the project:

1. Setup a virtual environment for Python. You can refer to these resources for guidance:
   - [Introduction to Pyenv](https://realpython.com/intro-to-pyenv/)
   - [Differences between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
2. Install Reflex by running `pip install reflex`.
3. Install the required Python packages by running `pip install -r requirements.txt`.

## Database Setup

Reflex uses Alembic for database migrations. To set up the database for this project:

1. Create a new Python file in the `/models` directory.
2. Define your database schema in the newly created file.
3. Import the schema in `/models/__init__.py`.
4. After making changes to the schema, use `reflex db makemigrations --message 'your change description'` to generate a migration script in the `alembic/versions` directory. This script will update the database schema. It is recommended to inspect these scripts before applying them.
5. Use the `reflex db migrate` command to apply the migration scripts and bring the database up to date. If Reflex detects that the current database schema is not up to date during app startup, a warning will be displayed on the console.

## Environment Variables

The project requires several environment variables to run correctly. You can find an example in the `.env.example` file. Copy this file to `.env` and fill in the appropriate values.

## Setting Up a Shopify App

Follow these steps to set up a Shopify app:

1. **Access Shopify Partners:** Log in to your [Shopify Partners](https://partners.shopify.com/) account.

2. **Navigate to Apps:** Click on 'Apps' in the sidebar menu.

3. **Create a New App:** Click on 'Create app', then 'Create app manually'. Enter the 'App name' and click 'Create app'.

4. **Retrieve Client Credentials:** After the app is created, you'll be redirected to the app's overview page. Here, locate the 'Client ID' and 'Client secret' under the 'Client credentials' section. These keys are essential for the Shopify integration in this project. Copy them and set the `SHOPIFY_API_KEY` and `SHOPIFY_API_SECRET_KEY` environment variables in your .env file.

5. **Configure App Settings:** In the 'Configuration' section, enter the 'Allowed redirection URL(s)' and 'App URL' for your app. The 'App URL' should be the URL where your app is hosted. The 'Allowed redirection URL(s)' is where Shopify will redirect users after they authorize your app's installation. For this project, use `https://your-backend-domain/oauth/callback`.

6. **Finalize App Creation:** Click on 'Create app'.

> **Note:** Replace `https://your-backend-domain` with your application's actual backend domain. For local development, use `http://localhost:8000/`. You can find and set this value in the `BE_DOMAIN` environment variable in your .env file.

## Running the Application

To run the application, use the following command. This will start the Reflex application and serve it on a local web server.

```bash
reflex run
```

To verify that the application is running correctly, you can open the following URLs in your web browser:

- [http://localhost:3000](http://localhost:3000) - This is the URL where your app is served.
- [http://localhost:8000/ping](http://localhost:8000/ping) - This URL should return "pong" as a response, indicating that the server is running properly.

> **Note:** You can add these URLs to the `BE_DOMAIN` and `FE_DOMAIN` environment variables in your `.env` file.

Reflex prints logs to the terminal. To increase log verbosity to help with debugging, use the --loglevel flag:

```bash
reflex run --loglevel debug
```

Reflex will hot reload any code changes in real time when running in development mode. Your code edits will show up on <http://localhost:3000> automatically.

## Contributing

Contributions to this project are welcome. Please ensure that any changes do not break existing functionality and that all code is properly formatted and documented.

## License

This project is licensed under the terms of the included LICENSE file.
