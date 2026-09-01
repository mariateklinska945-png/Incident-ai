from app.agent import investigate

question = input("Ask about an incident: ")

print("\nInvestigating...\n")

result = investigate(question)

print(result)

