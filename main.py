#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from dotenv import find_dotenv, load_dotenv

from crewai import Crew, Process
from agent import data_analyst, process_optimizer, report_writer
from task import analysis_task, optimization_task, report_task

from crewai import LLM


load_dotenv(find_dotenv())
api_key = os.environ.get("GEMINI_API_KEY", "xxx")


gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=api_key,
    temperature=0.7,  # NOTE: Setting a lower temperature gives more consistent results.
)


# Define the crew with agents, tasks, and process
support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)


# Start the crew's work
print("--- Starting Customer Support Analysis Crew ---")
# The 'inputs' dictionary provides initial context if needed by the first task.
# In this case, the tool simulates data fetching regardless of the input.
result = support_analysis_crew.kickoff(inputs={'data_query': 'last quarter support data'})

print("--- Crew Execution Finished ---")
print("--- Final Report for COO ---")
print(result)
