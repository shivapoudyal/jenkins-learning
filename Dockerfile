FROM jenkins/jenkins

RUN apt install default-jre -y && \
    apt install openjdk-11-jre-headless -y && \
    apt install openjdk-8-jre-headless -y    