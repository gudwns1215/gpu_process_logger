# gpu_process_logger
gpu process logger for prometheus

## run command
docker run -v /run/prometheus:/run/prometheus -gpus all --name gpu_process_logger -it -d gudwns1215/gpu_process_logger