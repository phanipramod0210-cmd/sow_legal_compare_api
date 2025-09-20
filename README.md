📝 SOW Legal Compare – AI-Powered Contract Analyzer
Overview

SOW Legal Compare is an AI-driven legal contract analysis tool that helps organizations draft tighter, jurisdiction-compliant Statements of Work (SOWs).
It leverages LLMs (GPT-4/5) + Retrieval Augmented Generation (RAG) to detect vague or open-ended clauses, validate them against jurisdiction-specific laws, and automatically suggest tightened alternatives.

⚖️ Disclaimer: This tool is for educational/demo purposes only and does not constitute legal advice.

✨ Features

Contract Upload & Parsing: Upload .docx, .pdf, or plain text contracts.

Clause Analysis: Splits SOW into clauses, detects vague/open-ended language.

Jurisdiction Compliance: Cross-checks clauses with selected legal frameworks (India, US, UK – extendable).

AI-Powered Rewrites: Uses GPT-4/5 to suggest tightened, enforceable clauses.

Final SOW Generation: Builds a complete, jurisdiction-compliant draft.

Frontend: React + Tailwind (modern UI).

Backend: FastAPI + OpenAI integration.

CI/CD & Deployment: Automated GitHub Actions workflow with deployment to Heroku.

🛠️ Tech Stack

Frontend: React, TailwindCSS

Backend: FastAPI (Python), Uvicorn

AI/LLMs: OpenAI GPT-4/5

Data Layer: RAG with jurisdiction-specific legal rules (sample for India, UK, US)

DevOps: GitHub Actions CI/CD, Heroku Deployment

🚀 Getting Started
1. Clone the repo
git clone https://github.com/yourusername/sow-legal-compare.git
cd sow-legal-compare

2. Backend Setup
cd sow_legal_compare_api
pip install -r requirements.txt
uvicorn main:app --reload


API will run at: http://127.0.0.1:8000/docs

3. Frontend Setup
npm install
npm run dev

⚡ Example Workflow

Upload a draft SOW.

Select jurisdictions (India, US, UK).

Run AI analysis → vague clauses are flagged with reasons.

Get suggested tightened clauses + compliance rationale.

Export the final tightened SOW.

🔄 CI/CD & Deployment

GitHub Actions workflow runs on every main push.

Automatic deployment to Heroku (configurable with repo secrets).

Can be extended to Render/Cloud Run for containerized deployments.

📌 Roadmap

 Add more jurisdictions & legal datasets.

 Side-by-side clause diff viewer.

 Multi-language support.

 Role-based access (lawyers, contract managers).

🙌 Acknowledgments

OpenAI GPT models for clause analysis & rewriting.

FastAPI community for a lightweight backend framework.
