FROM python:3.6

WORKDIR /app
RUN  apt-get -y update && apt-get install -y python-mysqldb libsasl2-dev libsasl2-2 libsasl2-modules-gssapi-mit nginx
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
ADD requirements.txt /app
RUN pip install -r requirements.txt

# Nginx
COPY ./config/nginx.conf /etc/nginx/nginx.conf
RUN nginx -t
RUN service nginx restart
RUN update-rc.d nginx enable

COPY . /app
EXPOSE 80

ENTRYPOINT ["/app/entrypoint.sh"]