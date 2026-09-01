import csv
import json

from langchain_core.tools import tool


@tool
def check_transactions():
    """Check recent payment transactions and calculate the failure rate."""

    total = 0
    failed = 0

    with open("data/transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1

            if row["status"] == "failed":
                failed += 1

    failure_rate = (failed / total) * 100

    return {
        "total_transactions": total,
        "failed_transactions": failed,
        "failure_rate": failure_rate
    }


@tool
def check_logs():
    """Check application logs for recent errors."""

    with open("data/logs.json", "r") as file:
        logs = json.load(file)

    return logs


@tool
def check_deployments():
    """Check recent software deployments."""

    with open("data/deployments.json", "r") as file:
        deployments = json.load(file)

    return deployments


@tool
def check_code_changes():
    """Check recent code changes."""

    with open("data/code_changes.json", "r") as file:
        changes = json.load(file)

    return changes

