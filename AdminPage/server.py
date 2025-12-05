from admin_page import settings
from admin_page.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # noqa S104
        port=settings.PORT,
        debug=settings.DEBUG,
    )
