from routing import choose_source


def test_current_question_uses_web():
    assert choose_source("What is the latest research?", True, True) == "web_tools"


def test_uploaded_document_is_preferred():
    assert choose_source("What are the stated limitations?", True, True) == "documents"


def test_no_documents_uses_tools():
    assert choose_source("Explain particle filters", False, True) == "web_tools"
