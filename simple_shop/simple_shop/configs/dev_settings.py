from configs.base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=r0k=b3w+#u^kp#(d!bbx&f!9v!^h7gy&!^_cjdjhsw+vx3&&1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simple_shop_dev',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
