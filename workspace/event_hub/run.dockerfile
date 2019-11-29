FROM openjdk:8-jre-alpine

WORKDIR /app
ADD build/libs/event_hub-all-1.0.jar /app/app.jar

CMD ["/usr/bin/java", "-jar", "./app.jar"]
