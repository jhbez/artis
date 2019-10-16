FROM python:3.7-alpine
LABEL version="1.0.0"
LABEL maintainer="@Joinher"

ENV MYHOME=/artis
# create user
RUN adduser -S -h ${MYHOME} -s /bin/bash -g root -u 1000 artis
USER artis

# Create home
WORKDIR ${MYHOME}
COPY ./ ${MYHOME}

RUN pip install --user -r requirements.txt

#expose
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]