from setuptools import find_packages, setup


setup(
    name='cosmic-ray-engine-rq',
    version='1.0.0a1',
    author="Ulrich Petri",
    author_email="python@ulo.pe",
    description='Cosmic Ray execution engine that distributes execution via RQ.',
    url='https://github.com/ulope/cosmic-ray-engine-rq',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'rq<1.0',
    ],
    entry_points={
        'cosmic_ray.execution_engines': [
            'rq = cosmic_ray_engine_rq.engine:RQExecutionEngine',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    platforms='any',
)
