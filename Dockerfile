FROM pytorch/pytorch
ADD . /workspace/gpu_process_logger
WORKDIR /workspace/gpu_process_logger
RUN /usr/local/bin/pip install -r /workspace/gpu_process_logger/requirements.txt

CMD ["/usr/local/bin/python", "/workspace/gpu_process_logger/run.py"]