The main objective of this project was to develop a Q&A bot using OpenAI word embeddings and text generation models, applied on a customized dataset, which is the transcribed textual data fetched from a series of YouTube videos.

The Q&A bot is designed using OpenAI's “text-embedding-ada-002” model for word embeddings and “text-davinci-003” for text generation, which is a GPT3.5 chat-based model. It answers only on the basis of the context it is provided through the transcribed text. The bot could be helpful for people having specific health conditions, who would like to know a doctor’s and specialist’s view on its precautions, therapies, and treatments.

The dataset used in this project was fetched by transcribing a series of YouTube videos of a healthcare podcast named “Beaumont Health”. In these videos, different kinds of health conditions, their therapies and treatments are discussed, which are transcribed using a Python API called YouTube Transcript/Subtitles API. It allows us to fetch the transcript for a given YouTube video as well as the automatically generated subtitles. Specifically, the transcriptions of 10 YouTube videos detailing different conditions (each around 30 minutes) were used in this project.

You can find the code in Project_codefile.ipynb and chatbot.py for Streamlit based front-end interface designed for the project.

Original idea: https://www.youtube.com/watch?v=hR8xhJgKcJ0
