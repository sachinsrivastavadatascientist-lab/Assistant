from langgraph.graph import StateGraph,END,START
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tools_node import ChatbotWithToolNode



class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
       

    def basic_chatbot_build_graph(self):
         '''Building a basic Chatbot graph udsing Langgraph
         
         This method initalizes a chatbot node using the 'BasicChatbotNode'. class 
         and integrates it into the graph.The chatbot node is set as both the
         entry and exit point of the graph'''   

         self.basic_chatbot_node = BasicChatbotNode(self.llm)

         self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
         
         # building edges
         self.graph_builder.add_edge(START,"chatbot")

         self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        '''
        Builds an Advanced Chatbot graph with tool integration.
        This method creates a chatbot graph that ncludes chatbot node and a tool node.
        it defines the tools,initalizes chatbot with tool capabilities,and set up conditional and direct edges between nodes.
        The chatbot node is set as a entry point
        '''   
        # define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Define the LLM
        llm = self.llm

        # Definig the chatbot node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        # Add the node
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        # Defining the conditional edges and normal edges

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")

    def setup_graph(self,usecase: str):
        '''Setups the graph for the selected usecases''' 

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()


        return self.graph_builder.compile()    