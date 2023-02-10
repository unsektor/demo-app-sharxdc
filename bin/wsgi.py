import application.fastapi.wsgi

__all__ = (
    'app',
)

app = application.fastapi.wsgi.create_application()
