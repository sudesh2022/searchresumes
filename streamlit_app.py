import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

#st.set_page_config(page_title="This Chat is powered by IBM watsonx", page_icon="IBM", layout="centered", initial_sidebar_state="auto", menu_items=None)
# Add custom CSSst.set_page_config(page_title="App built using watsonx.ai", layout="wide",initial_sidebar_state="auto", page_icon='👧🏻')
st.set_page_config(page_title="App built using watsonx.ai", layout="wide",initial_sidebar_state="auto", page_icon='👧🏻')

# app sidebar
with st.sidebar:
    st.markdown("""
                # What can I ask ? 
                """)
    with st.expander("Click here to see FAQs"):
        st.info(
            f"""
            - Which city Anthony did his schooling ?
            - What is Anthonys favorite food ?
            - Which game Anthony, Vijay, Sudesh can play  ?
            - I want to visit a National Park. Who can advise me on it ?
            - I want to learn swimming. Whom should I speak to ?
          
            """
        )
    st.caption(f"Report bugs to sudesh@sg.ibm.com ")

with st.container():
    col1,col2 = st.columns([8,3])

openai.api_key = st.secrets.API_KEY
#st.set_page_config(page_title="App built using watsonx.ai", layout="centered")

remove_all_streamlit_icons = """
  <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        .body {
        background-color: #f0f0f0; /* You can replace this with your desired color code */
        }
    </style>
"""


st.markdown(remove_all_streamlit_icons, unsafe_allow_html=True)

st.title("KYC - Know your colleagues powered by IBM Watsonx.ai 💬🦙")
       
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Sudesh, Anthony , Rambabu and Arvind Krishna! For now you can ask about where they work, what they studied, experience"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the following people resumes. Your job is to answer technical questions. Assume that all questions are related to the peoples resume provided. Keep your answers short and  based on facts – do not hallucinate features."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])



# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
