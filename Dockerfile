FROM python:3.7-buster
ADD . /workspace/gpu_process_logger
WORKDIR /workspace/gpu_process_logger

CMD ["/usr/local/bin/python run.py"]