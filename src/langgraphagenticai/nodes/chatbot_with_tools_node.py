from src.langgraphagenticai.state.state import State
from langchain_core.messages import HumanMessage,AIMessage

class ChatbotWithToolNode:
    '''
     chatbot with tools login implementation
    '''
    def __init__(self,model):
        self.llm = model
    
    def create_chatbot(self,tools)->dict:
        '''
        processes the input state and generates a response with tool integration'''
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state:State):
            '''Return a chatbot node function.
            '''
            response = llm_with_tools.invoke(state['messages'])
            return {"messages":response}


        return chatbot_node
