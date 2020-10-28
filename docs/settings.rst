Settings
========

To setup application your can use environment variables or .env file.

You can setup next given variables:

.. envvar:: DEBUG

    Flag run application in Debug.
    Default: True

.. envvar:: SECRET_KEY

    Salt used for hash generation.

    Default: &43a$!xv3gsfds(41+1=rh3mt1*gi5wc3c$_wnj_)j7c%lf&#1

.. envvar:: AUTH_URL

    Host to `trood-auth` rest API.

    Default: http://auth:8000/

.. envvar:: SENTRY_ENABLED

    Enable Sentry.io error collector.

    Default: False

.. envvar:: SENTRY_DSN

    Sentry.io DSN.

    Required if `SENTRY_ENABLED` is `True`.

    Default: https://b929140809d441b98f4ba197b2560d0e:8929448bcde043e48d712dbcd11d0794@sentry.tools.trood.ru/4

.. envvar:: SENTRY_ENV

    Sentry.io project environment.

    Required if `SENTRY_ENABLED` is `True`.

    Default: dev

