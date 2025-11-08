from dotenv import load_dotenv
load_dotenv()


# from langchainhub import hub

from langchainhub import LangChainHub

client = LangChainHub()  # create a Hub client instance
print("✅ Import successful!")


from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")

react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    result = agent_executor.invoke({
        "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
    })
    print(result)

if __name__ == "__main__":
    main()
