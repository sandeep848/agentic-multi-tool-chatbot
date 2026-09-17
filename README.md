# Agentic Multi-Tool Research Assistant

A research-oriented assistant that can answer from uploaded PDFs or deliberately invoke external tools for current and general information.

## Distinct use case

This repository demonstrates **tool orchestration and source routing**. It is different from the NVIDIA knowledge-base project, which uses only indexed documents and hybrid retrieval.

| Question type | Route |
|---|---|
| Question grounded in uploaded reports | PDF retrieval chain |
| Current information or news | DuckDuckGo |
| Scientific paper lookup | arXiv |
| General background | Wikipedia |

A transparent routing policy sends time-sensitive questions to web tools even when PDFs are loaded.

## Architecture

~~~mermaid
flowchart LR
    A["User question"] --> B["Source router"]
    B --> C["PDF retrieval"]
    B --> D["Search tool"]
    B --> E["arXiv tool"]
    B --> F["Wikipedia tool"]
    C --> G["Answer with conversation memory"]
    D --> G
    E --> G
    F --> G
~~~

## Run

~~~bash
git clone https://github.com/sandeep848/agentic-multi-tool-chatbot.git
cd agentic-multi-tool-chatbot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
~~~

## Test

~~~bash
pytest
~~~

## Key engineering decisions

- uploaded files are fingerprinted before index reuse
- PDF answers are constrained to retrieved document context
- time-sensitive cues force a web-tool route
- conversation history is isolated by session
- the active model and retrieval preference remain user-controlled

## Limitations

External search results are untrusted inputs and should be verified. The application is a research assistant, not an autonomous decision maker.
