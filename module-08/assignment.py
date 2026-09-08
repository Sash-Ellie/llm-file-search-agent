"""
Module 08 Assignment: Understanding ChatAgent vs Direct LLM Calls

This assignment explores the key concepts from the module:
1. Direct LLM calls (stateless)
2. ChatAgent with automatic conversation management
3. Building a simple interactive chatbot

"""

import os
from typing import Optional
import langroid as lr
import langroid.language_models as lm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get model from environment - this is set by your course instructor
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gemini-2.5-flash")


def direct_llm_chat(query1: str = "Is 5 a prime number?", query2: str = "What about 15?") -> tuple[str, str]:
    """
    Demonstrate direct LLM interaction without conversation memory.
    This mimics step-04-direct-llm-chat.py from the materials.
    
    Args:
        query1: First query to send to the LLM
        query2: Second query to send to the LLM (will show lack of context)
        
    Returns:
        A tuple of (response1, response2) strings
    """
    # Create LLM configuration and instance
    llm_config = lm.OpenAIGPTConfig(
        chat_model=CHAT_MODEL,
        max_output_tokens=500,
        temperature=0.7
    )
    llm = lm.OpenAIGPT(llm_config)
    
    # TODO 1: Complete this function to show stateless behavior
    # Make two LLM calls using the `chat` method on `llm`:
    # 1. First call: use query1 parameter
    # 2. Second call: use query2 parameter
    # Print both responses AND return them as a tuple
    
    # TODO: Get response to query1
    response1 = llm.chat(query1)
    print(f"LLM Response 1: {response1.message}")
    
    # TODO: Get response to query2
    # This will demonstrate that the LLM doesn't remember the previous message
    response2 = llm.chat(query2)
    print(f"LLM Response 2: {response2.message}")
    
    # TODO: Return both responses as a tuple of (str, str)
    return (response1.message, response2.message)



def create_chat_agent() -> Optional[lr.ChatAgent]:
    """
    Create and return a configured ChatAgent.
    This follows the pattern from step-06-chat-agent-basics.py in the video/materials.
    """
    # TODO 2: Create and return a ChatAgent with a helpful system message
    # The agent should be configured to act as a helpful assistant
    # Steps:
    # 1. Create a ChatAgentConfig with:
    #    - name="Assistant" (name of the agent)
    #    - llm configuration using OpenAIGPTConfig with CHAT_MODEL
    #       - max_output_tokens=500 to avoid context issues
    #       - temperature=0.7
    #    - system_message="You are a helpful assistant."
    # 2. Create a ChatAgent with the config
    # 3. Return the agent
    #
    # return None  # Replace with your agent

    agent_config = lr.ChatAgentConfig(
         name="Assistant",
         llm=lm.OpenAIGPTConfig(
             chat_model=CHAT_MODEL,
             max_output_tokens=500,
             temperature=0.7,
         ),
         system_message="You are a helpful assistant.",
    )

    agent = lr.ChatAgent(agent_config)
    return agent


def chat_with_agent(agent: Optional[lr.ChatAgent], message: str) -> str:
    """
    Send the `message` to the `agent` and return the response,
    using the agent's llm_response method.
    
    Args:
        agent: The ChatAgent instance
        message: User message to send
        
    Returns:
        The agent's response as a string
    """
    # TODO 3: Use the agent's llm_response method to get a response to `message`
    # Use the `agent`, `message` function args above.
    response = agent.llm_response(message)
    print(f"Agent Response: {response.content}")
    return response.content

    # Extract the content from the response object
    # Note that response is a ChatDocument object, with a content attribute of type str.



def interactive_chat_loop(agent: Optional[lr.ChatAgent]) -> None:
    """
    Run an interactive chat loop with the agent.
    This implements the pattern from step-07-enhanced-chat-agent.py.
    """
    print("Chat started! Type 'quit' to exit.\n")
    
    while True:
        # get user input
        user_input = input("You: ")

        # TODO 4: break out of loop if user types 'quit'
        if user_input.lower().strip() == "quit":
            break
      

        # TODO 5: Get agent's response to input, and print it
        # Use the chat_with_agent function you implemented above
        response = chat_with_agent(agent, user_input)
        print(f"Assistant: {response}\n")


