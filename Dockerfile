FROM python:3.7-alpine
LABEL version="1.0.0"
LABEL maintainer="@Joinher"

ENV MYHOME=/home/artis
# create user
RUN adduser -S -h ${MYHOME} -s /bin/bash -g root -u 1000 artis
USER artis

# Create home
WORKDIR ${MYHOME}
RUN mkdir ${MYHOME}/app
COPY ./ ${MYHOME}/app

#install requirements 
WORKDIR ${MYHOME}/app
RUN pip install --user -r requirements.txt

#expose
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]