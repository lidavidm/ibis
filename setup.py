# -*- coding: utf-8 -*-
from setuptools import setup

packages = [
    'ibis',
    'ibis.backends',
    'ibis.backends.base',
    'ibis.backends.base.sql',
    'ibis.backends.base.sql.alchemy',
    'ibis.backends.base.sql.compiler',
    'ibis.backends.base.sql.registry',
    'ibis.backends.clickhouse',
    'ibis.backends.clickhouse.tests',
    'ibis.backends.dask',
    'ibis.backends.dask.execution',
    'ibis.backends.dask.tests',
    'ibis.backends.dask.tests.execution',
    'ibis.backends.datafusion',
    'ibis.backends.datafusion.tests',
    'ibis.backends.duckdb',
    'ibis.backends.duckdb.tests',
    'ibis.backends.impala',
    'ibis.backends.impala.tests',
    'ibis.backends.mysql',
    'ibis.backends.mysql.tests',
    'ibis.backends.pandas',
    'ibis.backends.pandas.execution',
    'ibis.backends.pandas.tests',
    'ibis.backends.pandas.tests.execution',
    'ibis.backends.postgres',
    'ibis.backends.postgres.tests',
    'ibis.backends.pyarrow',
    'ibis.backends.pyspark',
    'ibis.backends.pyspark.tests',
    'ibis.backends.sqlite',
    'ibis.backends.sqlite.tests',
    'ibis.backends.tests',
    'ibis.common',
    'ibis.common.tests',
    'ibis.expr',
    'ibis.expr.datatypes',
    'ibis.expr.operations',
    'ibis.expr.types',
    'ibis.tests',
    'ibis.tests.benchmarks',
    'ibis.tests.expr',
    'ibis.tests.sql',
    'ibis.udf',
]

package_data = {'': ['*']}

install_requires = [
    'atpublic>=2.3,<4',
    'multipledispatch>=0.6,<0.7',
    'numpy>=1,<2',
    'packaging>=21.3,<22',
    'pandas>=1.2.5,<2',
    'parsy>=1.3.0,<3',
    'pydantic>=1.9.0,<2',
    'regex>=2021.7.6',
    'rich>=12.4.4,<13',
    'toolz>=0.11,<0.13',
]

extras_require = {
    'all': [
        'clickhouse-cityhash>=1.0.2,<2',
        'clickhouse-driver[numpy]>=0.1,<0.3',
        'dask[dataframe,array]>=2021.10.0,<2022.8.0',
        'datafusion>=0.6,<0.7',
        'duckdb>=0.3.2,<1',
        'duckdb-engine>=0.1.8,<1',
        'fsspec>=2022.1.0',
        'GeoAlchemy2>=0.6.3,<0.13',
        'geopandas>=0.6,<0.12',
        'graphviz>=0.16,<0.21',
        'impyla[kerberos]>=0.17,<0.19',
        'lz4>=3.1.10,<5',
        'psycopg2>=2.8.4,<3',
        'pyarrow>=1,<10',
        'pymysql>=1,<2',
        'pyspark>=3,<4',
        'requests>=2,<3',
        'Shapely>=1.6,<1.8.5',
        'sqlalchemy>=1.4,<2.0',
        'sqlglot>=4.5.0,<7',
    ],
    'clickhouse': [
        'clickhouse-cityhash>=1.0.2,<2',
        'clickhouse-driver[numpy]>=0.1,<0.3',
        'lz4>=3.1.10,<5',
        'sqlglot>=4.5.0,<7',
    ],
    'dask': ['dask[dataframe,array]>=2021.10.0,<2022.8.0', 'pyarrow>=1,<10'],
    'datafusion': ['datafusion>=0.6,<0.7'],
    'duckdb': [
        'duckdb>=0.3.2,<1',
        'duckdb-engine>=0.1.8,<1',
        'pyarrow>=1,<10',
        'sqlalchemy>=1.4,<2.0',
        'sqlglot>=4.5.0,<7',
    ],
    'geospatial': [
        'GeoAlchemy2>=0.6.3,<0.13',
        'geopandas>=0.6,<0.12',
        'Shapely>=1.6,<1.8.5',
    ],
    'impala': [
        'fsspec>=2022.1.0',
        'impyla[kerberos]>=0.17,<0.19',
        'requests>=2,<3',
        'sqlalchemy>=1.4,<2.0',
        'sqlglot>=4.5.0,<7',
    ],
    'mysql': ['pymysql>=1,<2', 'sqlalchemy>=1.4,<2.0', 'sqlglot>=4.5.0,<7'],
    'postgres': [
        'psycopg2>=2.8.4,<3',
        'sqlalchemy>=1.4,<2.0',
        'sqlglot>=4.5.0,<7',
    ],
    'pyspark': ['pyarrow>=1,<10', 'pyspark>=3,<4'],
    'sqlite': ['sqlalchemy>=1.4,<2.0', 'sqlglot>=4.5.0,<7'],
    'visualization': ['graphviz>=0.16,<0.21'],
}

entry_points = {
    'ibis.backends': [
        'clickhouse = ibis.backends.clickhouse',
        'dask = ibis.backends.dask',
        'datafusion = ibis.backends.datafusion',
        'duckdb = ibis.backends.duckdb',
        'impala = ibis.backends.impala',
        'mysql = ibis.backends.mysql',
        'pandas = ibis.backends.pandas',
        'postgres = ibis.backends.postgres',
        'pyspark = ibis.backends.pyspark',
        'spark = ibis.backends.pyspark',
        'sqlite = ibis.backends.sqlite',
    ]
}

setup_kwargs = {
    'name': 'ibis-framework',
    'version': '3.2.0',
    'description': 'Productivity-centric Python Big Data Framework',
    'long_description': '# Ibis: Expressive analytics in Python at any scale\n\n|        Service | Status                                                                                                                                                                                                |\n| -------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n|  Documentation | [![Documentation Status](https://img.shields.io/badge/docs-docs.ibis--project.org-blue.svg)](http://ibis-project.org)                                                                                 |\n| Conda packages | [![Anaconda-Server Badge](https://anaconda.org/conda-forge/ibis-framework/badges/version.svg)](https://anaconda.org/conda-forge/ibis-framework)                                                       |\n|           PyPI | [![PyPI](https://img.shields.io/pypi/v/ibis-framework.svg)](https://pypi.org/project/ibis-framework)                                                                                                  |\n|        Ibis CI | [![Build status](https://github.com/ibis-project/ibis/actions/workflows/ibis-main.yml/badge.svg)](https://github.com/ibis-project/ibis/actions/workflows/ibis-main.yml?query=branch%3Amaster)         |\n|     Backend CI | [![Build status](https://github.com/ibis-project/ibis/actions/workflows/ibis-backends.yml/badge.svg)](https://github.com/ibis-project/ibis/actions/workflows/ibis-backends.yml?query=branch%3Amaster) |\n|       Coverage | [![Codecov branch](https://img.shields.io/codecov/c/github/ibis-project/ibis/master.svg)](https://codecov.io/gh/ibis-project/ibis)                                                                    |\n\nIbis is a Python library to help you write expressive analytics at any scale,\nsmall to large. Its goal is to simplify analytical workflows and make you more\nproductive.\n\nInstall Ibis from PyPI with:\n\n```sh\npip install ibis-framework\n```\n\nor from conda-forge with\n\n```sh\nconda install ibis-framework -c conda-forge\n```\n\nIbis provides tools for interacting with the following systems:\n\n- [Apache Impala](https://ibis-project.org/docs/latest/backends/Impala/)\n- [Google BigQuery](https://github.com/ibis-project/ibis-bigquery)\n- [ClickHouse](https://ibis-project.org/docs/latest/backends/ClickHouse/)\n- [HeavyAI](https://github.com/heavyai/ibis-heavyai)\n- [Dask](https://ibis-project.org/docs/latest/backends/Dask/)\n- [DuckDB](https://ibis-project.org/docs/latest/backends/DuckDB/)\n- [MySQL](https://ibis-project.org/docs/latest/backends/MySQL/)\n- [Pandas](https://ibis-project.org/docs/latest/backends/Pandas/)\n- [PostgreSQL](https://ibis-project.org/docs/latest/backends/PostgreSQL/)\n- [PySpark](https://ibis-project.org/docs/latest/backends/PySpark/)\n- [SQLite](https://ibis-project.org/docs/latest/backends/SQLite/)\n\nLearn more about using the library at https://ibis-project.org.\n',
    'author': 'Ibis Contributors',
    'author_email': None,
    'maintainer': 'Ibis Contributors',
    'maintainer_email': None,
    'url': 'https://ibis-project.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
