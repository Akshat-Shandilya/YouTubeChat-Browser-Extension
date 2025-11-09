import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv() 

HF_TOKEN = os.environ.get("HF_TOKEN")
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"token": HF_TOKEN}
)

gemini_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.5,
    max_output_tokens=128
)

template="""
      You are a helpful Youtube chatbot. Answer the question only from the provided youtube video transcript context .
      Context: {context}
      Question: {question}
    """

def main_chain(video_id, question):

    ytapi = YouTubeTranscriptApi()
    transcript_list = ytapi.fetch(video_id=video_id)
    transcript = " ".join(e.text for e in transcript_list)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.create_documents([transcript])

    vector_store = FAISS.from_documents(chunks, embedding_model)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    prompt = PromptTemplate(
        template=template,
        input_variables=['context', 'question']
    )

    parser = StrOutputParser()

    chain = ({
            "context": retriever | RunnableLambda(lambda docs: "\n\n".join(d.page_content for d in docs)),
            "question": RunnablePassthrough() }
        | prompt
        | gemini_model
        | parser
    )

    answer = chain.invoke(question)

    return answer

print(main_chain( "aircAruvnKk", "How does a neural network work?" ))

