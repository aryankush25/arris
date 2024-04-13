# Dashboard Template

This is a Reflex starter template for a dashboard app.

## How to setup database

1. Create a new file in `/models`.
2. Define the schema in the newly created file.
3. Import that schema in `/models/__init__.py`.
4. After making changes to the schema, use `reflex db makemigrations --message 'something changed'` to generate a script in the alembic/versions directory that will update the database schema. It is recommended that scripts be inspected before applying them.
5. The `reflex db migrate` command is used to apply migration scripts to bring the database up to date. During app startup, if Reflex detects that the current database schema is not up to date, a warning will be displayed on the console.
