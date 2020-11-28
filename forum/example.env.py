# Keys, Debug, Host
SECRET_KEY = ''
DEBUG = True
ALLOWED_HOSTS = ['*', ]

# DB
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = 'localhost'  # localhost default
DB_PORT = ''  # postgres port 5432

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_USE_TLS = True

# For local testing
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "email/password_reset")
