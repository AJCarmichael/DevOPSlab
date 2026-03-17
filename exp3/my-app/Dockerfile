# Use Tomcat 9 as the base image
FROM tomcat:9.0-jdk11-openjdk-slim

# Remove default Tomcat apps to keep it clean
RUN rm -rf /usr/local/tomcat/webapps/*

# Copy your WAR file from the target folder into Tomcat's webapps
COPY target/*.war /usr/local/tomcat/webapps/ROOT.war

# Expose port 8080 inside the container
EXPOSE 8080

CMD ["catalina.sh", "run"]
