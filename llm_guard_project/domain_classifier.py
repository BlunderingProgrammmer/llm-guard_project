from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

DOMAIN_EXAMPLES = {
    "medical": [
        "patient diagnosis report",
        "blood test results analysis",
        "prescription for antibiotics",
        "post-surgery recovery plan"
    ],
    "legal": [
        "copyright infringement case",
        "contract termination clause",
        "patent filing requirements",
        "GDPR compliance checklist"
    ],
    "technical": [
        "debug Python list comprehension",
        "optimize SQL query performance",
        "Docker container networking",
        "REST API authentication"
    ],
    "casual": [
        "movie recommendations for kids",
        "best pizza places in town",
        "weekend hiking trail ideas",
        "how to start a book club"
    ]
}

model = SentenceTransformer('all-MiniLM-L6-v2')
domain_embeddings = {domain: model.encode(examples) for domain, examples in DOMAIN_EXAMPLES.items()}

def detect_domain(text, threshold=0.7):
    text_embed = model.encode(text)
    scores = {}
    for domain, embeds in domain_embeddings.items():
        similarity_scores = cosine_similarity([text_embed], embeds)[0]
        scores[domain] = np.max(similarity_scores)
    best_domain = max(scores, key=scores.get)
    confidence = scores[best_domain]
    return (best_domain, confidence) if confidence >= threshold else ("unknown", confidence)
