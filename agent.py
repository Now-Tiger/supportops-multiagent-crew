from __future__ import annotations

from crewai import Agent

from tool import support_data_tool
from main import gemini_llm


data_analyst = Agent(
    role="Customer Support Data Analyst",
    goal="Analyze customer support data to identify trends, recurring issues, and key pain points.",
    backstory=(
        """You are an expert data analyst specializing in customer support operations.
        Your strength lies in identifying patterns and quantifying problems from raw support data."""
    ),
    verbose=True,
    allow_delegation=False,  # This agent focuses on its specific task
    tools=[support_data_tool],  # Assign the data fetching tool
    llm=gemini_llm,  # Use the configured Gemini LLM
)

# Agent 2: Process optimizer
process_optimizer = Agent(
    role="Process Optimization Specialist",
    goal="Identify bottlenecks and inefficiencies in current support processes based on the data analysis. Propose actionable improvements.",
    backstory=(
        """You are a specialist in optimizing business processes, particularly in customer support.
        You excel at pinpointing root causes of delays and inefficiencies and suggesting concrete solutions."""
    ),
    verbose=True,
    allow_delegation=False,
    # No tools needed, this agent relies on the context provided by data_analyst.
    llm=gemini_llm,
)

# Agent 3: Report writer
report_writer = Agent(
    role="Executive Report Writer",
    goal="Compile the analysis and improvement suggestions into a concise, clear, and actionable report for the COO.",
    backstory=(
        """You are a skilled writer adept at creating executive summaries and reports.
        You focus on clarity, conciseness, and highlighting the most critical information and recommendations for senior leadership."""
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
)
