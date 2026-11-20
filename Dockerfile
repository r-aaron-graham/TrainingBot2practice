FROM python:3.12-slim
WORKDIR /app
COPY training_eval.py test_training_eval.py ./
USER 65534:65534
CMD ["python", "training_eval.py"]
