FROM python:3.9.9-slim

WORKDIR /app

COPY . .

## set timezone to asia jakarta
RUN apt update -y && apt install make -y && apt install locales -y

RUN export LC_ALL=C

RUN ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN echo "Asia/Jakarta" > /etc/timezone

RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN python3 -m pip install -r requirements.txt

ENV PORT=5000

CMD ["make", "run"]