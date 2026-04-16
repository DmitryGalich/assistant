FROM python:3.14-slim

WORKDIR /model_handler
COPY . /model_handler

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install langchain===1.2.27
RUN pip install langchain-community===0.4.1
