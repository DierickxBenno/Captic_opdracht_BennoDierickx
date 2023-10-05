# build image
FROM python:3.11.4-alpine3.18 as build-image

WORKDIR '/app'

RUN apk add --no-cache linux-headers g++

RUN apk add py3-opencv

COPY ./requirements.txt ./

RUN pip wheel --wheel-dir=/root/wheels -r requirements.txt



# production image
FROM python:3.11.4-alpine3.18 as production-image

WORKDIR '/app'

COPY --from=build-image /root/wheels /root/wheels

COPY --from=build-image /app/requirements.txt ./

RUN apk add py3-opencv

RUN pip install --no-index --find-links=/root/wheels -r requirements.txt

COPY ./ ./

RUN addgroup -S uwsgi && adduser -S uwsgi -G uwsgi

USER uwsgi

CMD ["uwsgi", "--ini", "app.ini"]