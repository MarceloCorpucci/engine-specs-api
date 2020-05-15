# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3

LABEL MAINTAINER="Marcelo Corpucci <mcorpucci@gmail.com>"

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
# ENV FLASK_APP api.main:create_app('PROD')
# ENV FLASK_RUN_PORT 8050

# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE 8050

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# We copy the rest of the codebase into the image
COPY . .

# Finally, we run uWSGI with the ini file we
# created earlier
CMD ["export", "FLASK_APP=\"api.main:create_app('PROD')\""]
CMD ["export", "FLASK_RUN_PORT=8050"]
CMD ["flask", "run"]