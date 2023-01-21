from langchain import OpenAI, Wikipedia
from langchain.agents import initialize_agent, Tool
from langchain.agents import load_tools


llm = OpenAI(
    temperature=0,
    model_name="text-davinci-002",
    openai_api_key="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",
)

tools = load_tools(["google-search"], llm=llm)
# agentAlt = "self-ask-with-search"
react = initialize_agent(tools, llm, agent="self-ask-with-search", verbose=True)
question = "What disadvantages of arweave relative to ipfs are most relevant to defi apps looking to host their frontend without a server?"
react.run(question)
