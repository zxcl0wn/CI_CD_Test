FROM ubuntu:latest
LABEL authors="m_mar"

ENTRYPOINT ["top", "-b"]