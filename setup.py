try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='itsdangerous',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='0.14',
    url='http://github.com/mitsuhiko/itsdangerous',
    py_modules=['itsdangerous'],
    description='Various helpers to pass trusted data to untrusted environments.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
