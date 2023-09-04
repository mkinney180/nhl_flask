# https://flask.palletsprojects.com/en/2.1.x/quickstart/

# https://medium.com/@mikaelagurney/add-dynamic-components-to-your-html-templates-using-form-s-flask-and-jinja-59b4169ec3e1
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
# todo try to upload a file and have it change by pressing a button

# idea will be to have two docker containers with a shared volume folder on my desktop
# one docker container to call out to APIs, download data, run models and predict probabilities -> save those probabalities in shared volume
# one docker container to monitor shared volume and display the probabilities in a webpage