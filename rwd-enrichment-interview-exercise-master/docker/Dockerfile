FROM python:3.8-slim

RUN apt-get update
RUN apt-get install make

WORKDIR /

COPY requirements.txt setup.py Makefile /
RUN make init

COPY rwd_enrichment_interview_exercise rwd_enrichment_interview_exercise

COPY docker/entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]