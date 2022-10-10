ENGLISH TO FRENCH TRANSLATION MODEL

Deployment Steps:

We created a new repository on GitHub for source control. We created a folder locally and pushed our readme file after committing and setting the remote origin.
We started the project setup by going over the solution collab that we have created a copy of in our drive.
We made sure to save the tokenizers of English and French in JSON files and trained the model again in order to save the weights after completion in final_model.h5
After completion, we downloaded the model weights, and tokenizers JSON files and added them under the model folder in our project folder.
The model folder contains a class for our model and its initialization that loads the model’s weights and tokenizers into variables. It also includes our predict function that uses the tokenizers, applies padding to the input sentence, and gets the result using the model.
We’ve tested our model using python3 model.py from our terminal.
Then we started implementing Flask in app.py by defining the routes for our application. We’ve created an HTML page with styling and javascript functions to first ensure that we have only 15 words as input and to call the prediction API at the specified route.
Now our ‘/’ route returns our HTML page using render_template from Flask and our API has ‘/translate’ GET supported route that takes english_sentence from the payload.
Now we moved to docker, We’ve initialized a Dockerfile that has the steps, docker-compose.yml for our pipelines, and requirements.txt for our necessary libraries.
Running sudo docker-up helped create the images from the requirements.txt file and build the project that we tested locally and found the same results as when running the app.py using python3 app.py
We moved to deployment by creating a Docker account and a Heroku account then applied the following commands:
heroku login (after installing Heroku CLI)
sudo docker login --username=OUR USERNAME --password=OUR PASSWORD
sudo heroku container:login
heroku create translator-ghadi-waseem
heroku git:remote -a translator-ghadi-waseem
sudo heroku container:push web --app translator-ghadi-waseem
sudo heroku container:release web --app translator-ghadi-waseem
