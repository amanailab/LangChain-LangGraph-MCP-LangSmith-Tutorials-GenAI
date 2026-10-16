import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm import get_model


# 1. Define the output schema
class Ticket(BaseModel):
    category: Literal[
        "billing", "technical", "account", "other"
    ] = Field(description="Best issue category")

    urgency: Literal[
        "low", "medium", "high"
    ] = Field(description="Issue urgency")

    summary: str = Field(
        description="One-sentence summary"
    )


model = get_model()

# 2. Create the structured classifier
classifier = model.with_structured_output(Ticket)


# 3. Create reply chains
def make_reply_chain(instructions):
    prompt = ChatPromptTemplate.from_messages([
        ("system", instructions),
        ("human", "{question}")
    ])

    return prompt | model | StrOutputParser()


billing_chain = make_reply_chain(
    "You are a billing support agent. Be polite. "
    "Do not promise a refund."
)

technical_chain = make_reply_chain(
    "You are a technical support agent. "
    "Suggest one safe troubleshooting step."
)

account_chain = make_reply_chain(
    "You are an account support agent. "
    "Give safe account guidance."
)

other_chain = make_reply_chain(
    "You are a general support agent. Be helpful and polite."
)


# 4. Route according to the structured category
def route_ticket(ticket):
    if ticket.category == "billing":
        return billing_chain

    if ticket.category == "technical":
        return technical_chain

    if ticket.category == "account":
        return account_chain

    return other_chain


# 5. Process the customer request
def process_ticket(question):
    ticket = classifier.invoke(
        "Classify this support request using the schema:\n"
        + question
    )

    reply = route_ticket(ticket).invoke({
        "question": question
    })

    return {
        "customer_message": question,
        "category": ticket.category,
        "urgency": ticket.urgency,
        "summary": ticket.summary,
        "reply": reply
    }


# 6. Run and save the result
if __name__ == "__main__":
    question = input("Customer message: ")

    try:
        result = process_ticket(question)
        print(json.dumps(result, indent=2))

        path = Path("tickets.json")
        records = json.loads(path.read_text()) if path.exists() else []

        records.append(result)
        path.write_text(json.dumps(records, indent=2))

        print("Saved to tickets.json")

    except Exception as exc:
        print("Could not process ticket:", exc)