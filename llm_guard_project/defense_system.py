from llm_guard import scan_prompt
from llm_guard.vault import Vault
from llm_guard.input_scanners import PromptInjection, PII, Legal
 # This should now work
from domain_classifier import detect_domain

class DefenseSystem:
    def __init__(self):
        self.vault = Vault()
        self.injection_scanner = PromptInjection()
        self.pii_scanner = PII()
        self.legal_scanner = Legal()

    def analyze(self, text):
        domain, confidence = detect_domain(text)

        scanners = [self.injection_scanner]
        if domain == "medical":
            scanners.append(self.pii_scanner)
        if domain == "legal":
            scanners.append(self.legal_scanner)

        sanitized, results, is_valid = scan_prompt(text, self.vault, scanners=scanners)
        return {
            "is_safe": is_valid,
            "domain": domain,
            "confidence": round(confidence, 2),
            "details": results
        }
