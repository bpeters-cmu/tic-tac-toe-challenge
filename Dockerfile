FROM continuumio/miniconda3

RUN conda update -y -n base conda && \
    git clone https://github.com/bpeters-cmu/Tornado-api.git && \
    conda install -y -c anaconda redis-py && \
    conda install -y -c anaconda tornado

WORKDIR /Tornado-api

EXPOSE 80
CMD python app.py
