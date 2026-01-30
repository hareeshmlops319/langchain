from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field


class  Source(BaseModel):
    """Schema for a agent source used by the agnet"""
    url:str=Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and source"""
    answer:str =Field(description="The agent's answer to the quesation")
    sources: List[Source] = Field(default_factory=list, description="list of source to generate the answer")

llm = ChatOpenAI()
tavily_search = TavilySearch(max_results=5, topic="general")
tools = [tavily_search]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="can you find the langchain ai engineer role in the charlotte NC")})
    print(result)

if __name__=="__main__":
    main()
