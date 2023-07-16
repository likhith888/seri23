pip install virtualenv 
virtualenv venv
call venv/Scripts/activate

pip install -r requirements.txt

to run

uvicorn app:app --reload

