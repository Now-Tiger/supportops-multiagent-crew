# 🚀 SupportOps AI Analyst Crew

An intelligent, multi-agent system built with **CrewAI** and **Google Gemini** to autonomously analyze customer support data, identify process bottlenecks, and generate executive-level, actionable reports for optimization.

## ✨ Project Goal

To transform raw customer support data (tickets, logs, feedback) into clear, data-driven process improvements, enabling faster resolution times and improved customer satisfaction. This system provides senior leadership (e.g., COO) with immediate, actionable intelligence without manual data analysis overhead.

## 🧠 The Agent Workflow

This project utilizes a three-agent crew, each specialized in a critical step of the analysis and reporting pipeline:

| Agent                 | Role                            | Goal                                                            | Key Action                                                                                |
| :-------------------- | :------------------------------ | :-------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **Data Analyst**      | Customer Support Data Analyst   | Identify trends, recurring issues, and key pain points.         | Fetches and analyzes data using the **`Customer Support Data Fetcher`** tool.             |
| **Process Optimizer** | Process Optimization Specialist | Pinpoint bottlenecks and propose actionable improvements.       | Synthesizes data analysis to link issues to process failures.                             |
| **Report Writer**     | Executive Report Writer         | Compile findings into a concise, actionable report for the COO. | Formats the analysis and recommendations into a professional, one-page executive summary. |

---

## 🛠️ Technology Stack

- **Framework:** **CrewAI** for orchestrating the multi-agent system.
- **LLM:** **Google Gemini** (via `main.py`) provides the reasoning and generative power for all agents.
- **Tooling:** A dedicated **`Customer Support Data Fetcher`** tool simulates real-world data retrieval from databases or APIs.

## 🏃 Getting Started

1.  **Set up Environment:** Ensure you have the required libraries installed:
    ```bash
    pip install crewai google-genai
    ```
2.  **API Key:** Set your Gemini API key as an environment variable:
    ```bash
    export GEMINI_API_KEY='YOUR_API_KEY'
    ```
3.  **Run the Crew:** Execute the main script (assuming your entry point is `main.py` or similar):
    ```bash
    python main.py
    ```

The crew will autonomously execute the tasks, and the final executive report will be the output.
