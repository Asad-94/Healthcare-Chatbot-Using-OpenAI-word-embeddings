import openai
import streamlit as st
from streamlit_chat import message
from openai.embeddings_utils import get_embedding, cosine_similarity
import pickle

# Specify the file path of the pickle file
file_path = 'model.pkl'

# Load the DataFrame from the pickle file
with open(file_path, 'rb') as f:
    merged_df = pickle.load(f)

openai.api_key = "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"

def generate_response(question):

    question_vector = get_embedding(question, engine='text-embedding-ada-002')

    merged_df["similarities"] = merged_df['embedding'].apply(lambda x: cosine_similarity(x, question_vector))
    sorted_merged_df = merged_df.sort_values("similarities", ascending=False).head(5)

    context = []
    for i, row in sorted_merged_df.iterrows():
        context.append(row['context'])
    
    text = "\n".join(context)
    context = text

    prompt = f"""Answer the following question using only the context below. If you don't know the answer, just reply I don't know.

    Context:
    {context}

    Q: {question}
    A:"""

    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=prompt, 
        temperature=1, 
        max_tokens=500, 
        top_p=1, 
        frequency_penalty=0, 
        presence_penalty=0,
    )
    
    message = completions.choices[0].text.strip(" \n")
    return message


st.title("🩺 HealthcareGPT")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
    
def get_text():
    input_text = st.text_input("You: ","", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))