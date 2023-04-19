from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain import OpenAI
from langchain.retrievers import ChatGPTPluginRetriever

load_dotenv()
llm = OpenAI(model_name='gpt-3.5-turbo')
#chat = ChatOpenAI(model_name='gpt-3.5-turbo')


def query(q):
    # print("Query: ", q)
    #print("Answer: ", chat())
    print("Answer: ", llm(q))


# query("What is COVID19?")
# query('What is the Best original Song in Oscars 2023')
# query("Does Approximate k-NN Search supports post-filtering in OpenSearch?")

while(True):
    inp = input("Question? : ")
    query(inp)
