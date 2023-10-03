FROM python:3.11

RUN sed -i "s#Components: main#Components: main contrib non-free#g" /etc/apt/sources.list.d/debian.sources

RUN apt update
RUN apt install -y gcc python3-dev libsnmp-dev snmp-mibs-downloader
RUN mkdir /usr/src/csr_reporter
WORKDIR /usr/src/csr_reporter
COPY . /usr/src/csr_reporter
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "reporter.py"]
