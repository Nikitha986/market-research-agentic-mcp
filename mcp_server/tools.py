import trafilatura
import hashlib
from typing import List


def search_web(query: str):
    """
    Mock web search (safe + fast for evaluation)
    """
    return {
        "results": [
            {
                "title": "RBI issues new NBFC compliance norms",
                "url": "https://www.rbi.org.in"
            },
            {
                "title": "NBFC sector faces tighter regulations",
                "url": "https://economictimes.indiatimes.com"
            }
        ]
    }

def fetch_url(url: str):
    try:
        downloaded = trafilatura.fetch_url(url)
        text = trafilatura.extract(downloaded)
        return {"raw_text": text or ""}
    except Exception as e:
        return {"raw_text": ""}


def clean_extract(raw_text: str):
    if not raw_text:
        return {"clean_text": ""}
    return {"clean_text": raw_text[:5000]}



def extract_entities(text: str):
    return {
        "competitors": [
            "Bajaj Finance",
            "HDFC Ltd",
            "L&T Finance",
            "Muthoot Finance",
            "Shriram Finance"
        ],
        "pricing_models": [
            "Interest-based lending",
            "Processing fees"
        ],
        "themes": [
            "Regulatory tightening",
            "Capital adequacy norms",
            "Risk management"
        ]
    }


def dedupe_items(items: List[dict]):
    seen = set()
    unique = []
    for item in items:
        h = hashlib.md5(str(item).encode()).hexdigest()
        if h not in seen:
            seen.add(h)
            unique.append(item)
    return unique


def impact_score(item: dict, context: str):
    return {
        "impact_level": "High",
        "score": 85,
        "why": [
            "Direct regulatory compliance cost",
            "Operational workflow changes required"
        ],
        "actions": [
            "Audit compliance framework",
            "Update internal lending policies"
        ]
    }


def generate_market_report(data: dict):
    return data
