from __future__ import annotations

from crewai.tools import BaseTool


# Placeholder tool for fetching customer support data
class CustomerSupportDataTool(BaseTool):
    name: str = "Customer Support Data Fetcher"
    description: str = (
        "Fetches recent customer support interactions, tickets, and feedback. "
        "Returns a summary string."
    )

    def _run(self, argument: str) -> str:
        # In a real scenario, this would query a database or API.
        # For this example, return simulated data.
        print(f"--- Fetching data for query: {argument} ---")
        return """Recent Support Data Summary:
            - 50 tickets related to 'login issues'. High resolution time (avg 48h).
            - 30 tickets about 'billing discrepancies'. Mostly resolved within 12h.
            - 20 tickets on 'feature requests'. Often closed without resolution.
            - Frequent feedback mentions 'confusing user interface' for password reset.
            - High volume of calls related to 'account verification process'.
            - Sentiment analysis shows growing frustration with 'login issues' resolution time.
            - Support agent notes indicate difficulty reproducing 'login issues'."""


support_data_tool = CustomerSupportDataTool()
