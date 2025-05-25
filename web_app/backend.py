from langchain_google_vertexai import ChatVertexAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

memory = ConversationBufferMemory(
    memory_key="history",  # the variable name passed into the prompt
    return_messages=True,  # so that memory stores full message objects
)

llm = ChatVertexAI(
    project="neme-ai-rnd-dev-prj-01",
    model_name="gemini-2.5-flash-preview-04-17",
    temperature=0.1,
    max_retries=2,
    # streaming=True,
)

# prompt = ChatPromptTemplate.from_messages(
#     [("system", "You are a helpful assistant."), ("human", "{input}")]
# )

system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a helpful assistant."
)

prompt = ChatPromptTemplate.from_messages(
    [
        system_prompt,
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

chain = ConversationChain(llm=llm, memory=memory, prompt=prompt, verbose=False)

# response = chain.invoke({"input": "Tell me a story about a goldfish on the moon."})
# answer = response["response"]
# chain = prompt | llm
