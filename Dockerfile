# build image
FROM python:3.11.4-alpine3.18 as build-image

WORKDIR '/app'

RUN apk add --no-cache linux-headers g++

# RUN apk --no-cache add g++ opencv

# RUN apk --no-cache add g++ py3-opencv

# RUN apk info py3-opencv

COPY ./requirements.txt ./

RUN pip wheel --wheel-dir=/root/wheels -r requirements.txt



# production image
FROM python:3.11.4-alpine3.18 as production-image

WORKDIR '/app'

COPY --from=build-image /root/wheels /root/wheels

COPY --from=build-image /app/requirements.txt ./

RUN apk --no-cache add opencv

RUN apk --no-cache add py3-opencv

RUN pip install --no-index --find-links=/root/wheels -r requirements.txt

COPY ./ ./

RUN addgroup -S uwsgi && adduser -S uwsgi -G uwsgi

USER uwsgi

#CMD ["uwsgi", "--ini", "app.ini"]
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
