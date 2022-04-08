FROM python:3

RUN sed -i "s#deb http://deb.debian.org/debian bullseye main#deb http://deb.debian.org/debian bullseye main contrib non-free#g" /etc/apt/sources.list
RUN sed -i "s#deb http://deb.debian.org/debian bullseye-updates main#deb http://http.us.debian.org/debian bullseye-updates main contrib non-free#g" /etc/apt/sources.list
RUN sed -i "s#deb http://security.debian.org/debian bullseye/updates main#deb http://security.debian.org/debian bullseye/updates main contrib non-free#g" /etc/apt/sources.list
RUN apt update
RUN apt install -y gcc python-dev libsnmp-dev snmp-mibs-downloader
RUN mkdir /usr/src/csr_reporter
WORKDIR /usr/src/csr_reporter
COPY . /usr/src/csr_reporter
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "reporter.py"]
