from distutils.core import setup
# from setuptools import setup


setup(
    name='google_trans',
    version='0.1',
    description='google-translate cli',
    author='jongwony',
    author_email='lastone9182@gmail.com',
    scripts=['google_trans', 'parameter.py'],
    install_requires=['hyper', 'BeautifulSoup4'],
)
