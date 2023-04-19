from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import OpenSearchVectorSearch
from langchain.document_loaders import TextLoader

load_dotenv()
loader = TextLoader('sample.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()

docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(search_type="similarity"))


def query(q):
    # print("Query: ", q)
    print("Answer: ", qa.run(q))


# query("Nominees for the Best original song Oscars 2023")
# query('Nominees for the Best Director in Oscars 2023')
while(True):
    inp = input("Question? : ")
    query(inp)
