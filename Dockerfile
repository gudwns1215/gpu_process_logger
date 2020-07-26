FROM pytorch/pytorch
ADD . /workspace/gpu_process_logger
WORKDIR /workspace/gpu_process_logger
RUN /opt/conda/bin/pip install -r /workspace/gpu_process_logger/requirements.txt

CMD ["/opt/conda/bin/python", "/workspace/gpu_process_logger/run.py"]