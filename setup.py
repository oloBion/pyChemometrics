from setuptools import setup

setup(
    name='pyChemometrics',
    version='0.14',
    packages=['pyChemometrics'],
    url='https://github.com/oloBion/pyChemometrics/',
    documentation='http://pychemometrics.readthedocs.io/en/stable/',
    license='BSD 3-Clause License',
    author='Gonçalo Correia',
    setup_requires=['wheel'],
    author_email='gscorreia89@gmail.com',
    description='The pyChemometrics provides objects which wrap pre-existing '
                'scikit-learn PCA and PLS algorithms and adds model assessment metrics and functions '
                'common in the Chemometrics literature.'
)
