# TESTING

## CODE

## USER STORIE

## BROWSER

## DEVICE

## ACCESSIBILITY

## PERFORMANCE

## BUGS
The issues listed in the table below were indentified during the development of the project.

1. Table django_session don't exists - solved by the following command:
python manage.py migrate sessions

2. After migration to codeanywhere,  Error: pg_config executable not found. --> install psycopg2-binary

3.  Error: pg_config executable not found.
      
      pg_config is required to build psycopg2 from source.  Please add the directory
      containing pg_config to the $PATH or specify the full executable path with the
      option:
      
          python setup.py build_ext --pg-config /path/to/pg_config build ...
      
      or with the pg_config option in 'setup.cfg'.
      
      If you prefer to avoid building psycopg2 from source, please install the PyPI
      'psycopg2-binary' package instead.
      --> pip install psycopg2-binary

4. Create virtual enviroment  - source virt/bin/activate
