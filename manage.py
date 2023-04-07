def deploy():
    """Run deployment tasks."""

    # Import necessary modules
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from models import User

    # Create the Flask app instance
    app = create_app()

    # Push the app context to make it the current context
    app.app_context().push()

    # Create the database tables
    db.create_all()

    # Initialize the migration directory
    init()

    # Stamp the migration with the current revision
    stamp()

    # Migrate the database to the latest revision
    migrate()

    # Upgrade the database to the latest revision
    upgrade()


# Call the deploy function to run the deployment tasks
deploy()
