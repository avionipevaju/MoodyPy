FROM python:2.7
WORKDIR /moody
COPY . /moody
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8887
ENV PYTHONPATH /moody
CMD python /moody/moody_py/engine/core.py