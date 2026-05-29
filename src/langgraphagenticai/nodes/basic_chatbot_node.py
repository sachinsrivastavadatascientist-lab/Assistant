from src.langgraphagenticai.state.state import State
from langchain_core.messages import HumanMessage,AIMessage

class BasicChatbotNode:
    '''
    Basic chatbot login implementation
    '''
    def __init__(self,model):
        self.llm = model
    
    def process(self,state:State)->dict:

        response = self.llm.invoke(state['messages'])
        print(response)

        return {"messages":self.llm.invoke(state['messages'])}
