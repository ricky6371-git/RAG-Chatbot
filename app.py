from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from html_templates import css, bot_template, user_template
from pypdf import PdfReader
import streamlit as st

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(text)
    return chunks



def get_vectorstore(text_chunks):
    import asyncio
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=st.secrets["GOOGLE_API_KEY"])
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore



def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=st.secrets["GOOGLE_API_KEY"]
)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm = llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain



def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{$MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{$MSG}}", message.content), unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Chat with Multiple PDFs"
                       ,page_icon=":books:")
    
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.markdown("<h1 style='text-align: center;'>Chat with Multiple PDFs 📚</h1>", unsafe_allow_html=True)
    user_question = st.text_input("Ask a question about your documents:")


    if user_question:
        handle_userinput(user_question)


    with st.sidebar:
        st.subheader("Your Documents:")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                #get PDF text
                raw_text = get_pdf_text(pdf_docs)


                #get the text chunks
                text_chunks = get_text_chunks(raw_text)

                
                #create vector store
                vectorstore = get_vectorstore(text_chunks)
                st.write("Number of docs in FAISS:", vectorstore.index.ntotal)

                #create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
                
                st.success("Processing complete. You can now ask questions about your documents.")

    if st.session_state.conversation:
        st.success("Conversation chain is ready. Ask me a question!")


if __name__ == '__main__':
    main()