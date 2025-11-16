from dotenv import load_dotenv
from langchain import hub 
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
 
 

 
 
tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
 
react_prompt= hub.pull("hwchase17/react")


def main():
  print("Hello from langchain-course")
 
 
if __name__ == "__main__":
    main()