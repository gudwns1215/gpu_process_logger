# gpu_process_logger
gpu process logger for node-exporter

## run command
docker run -v /run/prometheus:/run/prometheus -gpus all --name gpu_process_logger -it -d --pid host gudwns1215/gpu_process_logger
