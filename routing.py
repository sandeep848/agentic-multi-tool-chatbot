"""Transparent source-routing policy for the research assistant."""

WEB_CUES = {"latest", "today", "current", "news", "web", "wikipedia", "arxiv"}


def choose_source(question: str, has_documents: bool, prefer_documents: bool) -> str:
    words = set(question.lower().split())
    if words & WEB_CUES:
        return "web_tools"
    if has_documents and prefer_documents:
        return "documents"
    return "web_tools"
