from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from config import AZURE_ENDPOINT, API_KEY, API_VERSION, DEPLOYMENT_ID
llm = AzureChatOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
    model=DEPLOYMENT_ID,
    openai_api_type="azure",
    temperature=0,
)
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question as clearly as possible:\n\nQuestion: {question}\nAnswer:"
)
chain = LLMChain(prompt=prompt, llm=llm)
def get_answer(question: str) -> str:
    try:
        return chain.run(question)
    except Exception as e:
        return f"[❌ LLM Error]: {str(e)}"
