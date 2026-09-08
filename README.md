# LLM File Search & Multi-Agent Assistant

A progressive Python project exploring large language model agents, custom tool use, file retrieval, summarization, and multi-agent orchestration using Langroid.

## Project Overview

This repository documents the progression of an LLM-agent system developed across multiple course modules.

The project begins with basic direct LLM interaction and conversational agents, then progresses to custom file tools, file-search workflows, specialist summarization agents, and a multi-agent file assistant capable of coordinating multiple tools to complete complex file-related tasks.

## Project Progression

### Module 08 — ChatAgent Fundamentals

Introduces the difference between direct stateless LLM calls and conversational agents with managed context.

Key concepts include:

- Direct LLM interaction
- Stateless vs. conversational behavior
- Langroid `ChatAgent`
- Agent configuration
- Conversation management
- Interactive chatbot loops

### Module 10 — File Assistant and Custom Tools

Extends agent functionality by introducing file-related tools and an assistant capable of interacting with local files.

Key concepts include:

- Custom tool implementation
- File reading and writing
- Directory interaction
- Agent tool use
- Structured file workflows

### Module 12 — File Search Agent

Implements a specialized agent for locating files based on user queries and file content.

Key concepts include:

- Specialized LLM agents
- File-search workflows
- Custom search tools
- Tool invocation
- Retrieval-oriented agent behavior

### Module 13 — Multi-Agent File Assistant

Builds a complete multi-agent system combining file search, file summarization, file operations, and orchestration.

The system includes:

- `FileSearchAgent`
- `FileSummarizerAgent`
- `FileSearchTool`
- `FileSummarizerTool`
- File reading, writing, and directory tools
- Multi-agent orchestration
- Tool delegation
- Task decomposition
- Automated testing
- Sample documents for search and summarization

The main assistant coordinates specialized agents and tools to handle multi-step requests such as finding relevant files, summarizing their contents, and creating output files.

## Repository Structure

    llm-file-search-agent/
    │
    ├── module-08/
    │   └── assignment.py
    │
    ├── module-10/
    │   ├── file_assistant.py
    │   └── file_tools.py
    │
    ├── module-12/
    │   ├── file_search_agent.py
    │   └── search_tool.py
    │
    └── module-13/
        ├── myfiles/
        │   ├── beethoven.md
        │   ├── beyonce.md
        │   ├── bill_evans.md
        │   ├── budgeting_tips.md
        │   ├── debt_management.md
        │   └── investment_basics.md
        ├── conftest.py
        ├── file_search_agent.py
        ├── file_summarizer_agent.py
        ├── file_tools.py
        ├── multi_agent_assistant.py
        ├── pyproject.toml
        ├── search_tool.py
        ├── summarizer_tool.py
        └── test.py

## Technologies

- Python
- Langroid
- Large Language Models
- Agent-based AI
- Custom LLM tools
- Environment-variable configuration
- pytest
- TOML / Python project configuration

## Skills Demonstrated

- Large language model application development
- LLM agents
- Multi-agent systems
- Tool calling
- Agent orchestration
- Retrieval workflows
- File search
- Automated summarization
- Python software development
- Modular architecture
- Task decomposition
- Testing and debugging
- AI-assisted workflow design

## Author

**Elzanne Naudé**  
M.S. Data Science Candidate, University of Pittsburgh
