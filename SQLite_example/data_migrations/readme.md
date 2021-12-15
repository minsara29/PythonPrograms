#database_migration_scripts

## create env
conda env create -f environment.yml 

## activate env
conda activate database-migrations

## directory structure 

##alembic install 
pip install alembic

##alembic init
alembic init <schemaname>
alembic init demo

##create version
alembic version -m "<message>"

##alemic upgade
alembic upgrade head --sql #to see the sql comments before action 
alembic upgrade head #perform updates 


