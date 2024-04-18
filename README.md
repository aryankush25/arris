# Arris Dashboard

This project is an AI-powered, Reflex-based dashboard application for generating and managing pages in Shopify stores. Reflex is a powerful, open-source platform for building web applications. It provides a user-friendly interface for store owners to streamline their operations.

## Installation

Follow these steps to install the project:

1. Install Reflex by running `pip install reflex`.
2. Setup a virtual environment for Python. You can refer to these resources for guidance:
   - [Introduction to Pyenv](https://realpython.com/intro-to-pyenv/)
   - [Differences between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
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

### Setting Up a Shopify App

1. Log in to your [Shopify Partners](https://partners.shopify.com/) account.
2. Click on 'Apps' in the sidebar menu.
3. Click on 'Create app' and then 'Create app manually'. Fill in the 'App name' and then create the app.
4. After the app is created, you will be redirected to the app's overview page. Here, you can find the 'Client ID' and 'Client secret' under the 'Client credentials' section. These keys are needed for the Shopify integration in this project. Copy them and set the `SHOPIFY_API_KEY` and `SHOPIFY_API_SECRET_KEY` environment variables respectively in your .env file accordingly.
5. Under the 'Configuration' section, fill in the 'Allowed redirection URL(s)' field with the redirect URI(s) and 'App URL' fields for your app. The App URL should be the URL where your app is hosted and Allowed redirection URL(s) is where Shopify will send users after they authorize the installation of your app. For this project, it would be `https://your-backend-domain/oauth/callback`.
6. Click on 'Create app'.

> **Note:** Please note that you need to replace `your-backend-domain` with the actual backend domain of your application. You can find this value in the `BE_DOMAIN` environment variable in your `.env` file.

## Running the Application

To run the application, use the following command. This will start the Reflex application and serve it on a local web server.

```bash
reflex run
```

Your app runs at <http://localhost:3000>.

Reflex prints logs to the terminal. To increase log verbosity to help with debugging, use the --loglevel flag:

```bash
reflex run --loglevel debug
```

Reflex will hot reload any code changes in real time when running in development mode. Your code edits will show up on <http://localhost:3000> automatically.

## Contributing

Contributions to this project are welcome. Please ensure that any changes do not break existing functionality and that all code is properly formatted and documented.

## License

This project is licensed under the terms of the included LICENSE file.
