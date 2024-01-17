FROM public.ecr.aws/docker/library/python:3.10-slim-bullseye
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y --no-install-recommends \
         build-essential \
         wget \
         ca-certificates \
         git \
         gcc \
         curl \
    && rm -rf /var/lib/apt/lists/*
 
# Install required Python packages
RUN pip install --upgrade pip
RUN pip install sagemaker-training==4.7.4
 
# Specify encoding
ENV LC_ALL=C.UTF-8
 
# Set some environment variables
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV SOLUTION_PIPELINE_MODE='train'
ENV COMPUTING='sagemaker'
#alo v 2.1.3
COPY /.sagemaker /opt/ml/code/
RUN pip install -r /opt/ml/code/requirements.txt
# Defines train.py as script entry point
ENV SAGEMAKER_PROGRAM main.py