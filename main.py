from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class AnalyzeRequest(BaseModel):
    text: str
    partyA: str
    partyB: str
    jurisdictions: list[str]

# Sample jurisdiction rules
legal_rules = [
  {"jurisdiction": "India", "rule": "Indian Contract Act Sec. 37 requires clear performance timelines."},
  {"jurisdiction": "India", "rule": "IT Act requires data localization for sensitive personal data."},
  {"jurisdiction": "United Kingdom", "rule": "UK CRA 2015 requires fairness and clarity in consumer contracts."},
  {"jurisdiction": "United Kingdom", "rule": "GDPR requires clear data processing obligations."},
  {"jurisdiction": "United States", "rule": "UCC requires definite quantity terms in sale of goods."},
  {"jurisdiction": "United States", "rule": "FTC Act prohibits unfair or deceptive contract terms."}
]

@app.post("/api/analyze")
async def analyze(req: AnalyzeRequest):
    # Split text into clauses
    clauses = [c.strip() for c in req.text.split("\n") if c.strip()]

    # Filter rules for selected jurisdictions
    rules = [r for r in legal_rules if r["jurisdiction"] in req.jurisdictions]

    # Dummy analysis response for now
    openClauses = []
    tightened_clauses = []
    for clause in clauses:
        tightened = clause.replace("reasonable efforts", "shall deliver within 10 business days")
        if "reasonable efforts" in clause:
            openClauses.append({
                "text": clause,
                "reason": "Vague term 'reasonable efforts'",
                "suggestion": tightened
            })
        tightened_clauses.append(tightened)

    return {
        "openClauses": openClauses,
        "legalConflicts": [],
        "finalSOW": "\n".join(tightened_clauses)
    }
