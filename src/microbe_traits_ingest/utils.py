from oaklib import get_adapter


def get_oi(ontology: str):
    adapter = get_adapter(f"sqlite:obo:{ontology}")
    return adapter
