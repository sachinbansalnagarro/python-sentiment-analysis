FROM pytorch/pytorch

WORKDIR /reverb/speech_diarization

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/ffmpeg-4
RUN apt-get install -y ffmpeg
RUN apt-get update

COPY requirements.txt requirements.txt

RUN pip install -U textblob
RUN python -m textblob.download_corpora
RUN python -m textblob.download_corpora lite

RUN pip install -r requirements.txt --ignore-installed

COPY server.py server.py
COPY sentiment_analysis.py sentiment_analysis.py


COPY meeting-buddy-c01e6987dd52.json meeting-buddy-c01e6987dd52.json
COPY transcribe_async.py transcribe_async.py
RUN  export GOOGLE_APPLICATION_CREDENTIALS=meeting-buddy-c01e6987dd52.json