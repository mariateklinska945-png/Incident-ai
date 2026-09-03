from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from app.tools import (
    check_transactions,
    check_logs,
    check_deployments,
    check_code_changes,
)

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

tools = [
    check_transactions,
    check_logs,
    check_deployments,
    check_code_changes,
]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are an AI incident investigator.

Your job is to investigate software incidents using the available tools.

Do not guess.
Gather evidence first.

When investigating payment failures, check relevant data such as:
- transactions
- application logs
- recent deployments
- recent code changes

At the end, explain:
1. What happened
2. Most likely root cause
3. Evidence
4. Confidence level

Be concise, technical, and evidence-driven.
"""
)


def investigate_with_trace(question: str):
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    tools_used = []

    for message in result["messages"]:
        if hasattr(message, "tool_calls") and message.tool_calls:
            for tool_call in message.tool_calls:
                tools_used.append(tool_call["name"])

    return {
        "report": result["messages"][-1].content,
        "tools_used": tools_used
    }


def investigate(question: str):
    result = investigate_with_trace(question)

    print("\nTools used:")

    for tool_name in result["tools_used"]:
        print(f"✓ {tool_name}")

    return result["report"]

