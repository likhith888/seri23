FROM python:3.11
RUN apt-get update && apt-get -y install vim && \
     apt-get clean && \
     apt-get autoremove 
WORKDIR /code 
COPY . /code 
USER root 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 
EXPOSE 7878 
RUN chown -R root:root /code && \
     chgrp -R 0 /code && \     
     chmod -R 777 /code  
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port","7878"]