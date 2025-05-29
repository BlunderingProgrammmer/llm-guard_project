# 🔒 LLM Security System

A Streamlit-based security system designed to analyze and protect Large Language Model (LLM) prompts from malicious or unsafe inputs. This project classifies input domains, scans for prompt injections, personally identifiable information (PII), and legal concerns, and provides a user-friendly interface to test and monitor prompt safety.

---

## Features

- **Live Check:** Analyze any user prompt in real-time to determine its safety status.
- **Domain Classification:** Automatically detect the domain of the input (e.g., medical, legal) to apply specialized scanning.
- **Prompt Injection Detection:** Identify and block malicious prompt injections.
- **PII and Legal Scanning:** Domain-specific scanners to detect sensitive information and legal risks.
- **Attack Test:** Generate and run a set of known attack prompts to evaluate the defense system's effectiveness.
- **Interactive Streamlit UI:** Easy-to-use web interface with tabs for live checking and attack testing.

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the main application:

```bash
python main.py
```

This will launch the Streamlit app.

### UI Overview

- **Live Check Tab:**  
  Enter any prompt in the text input box to analyze its safety. The system will display the detected domain, confidence score, safety status (Safe or Blocked), and detailed scan results.

- **Attack Test Tab:**  
  Click the "Run Attacks" button to generate and test a set of predefined attack prompts. The results table shows each attack snippet, its domain, and whether it was blocked by the defense system.

---

## Components

- **DefenseSystem:**  
  Core class that analyzes prompts using domain detection and multiple scanners (prompt injection, PII, legal). Returns detailed safety analysis.

- **AttackGenerator:**  
  Generates a mix of local and external attack prompts to test the defense system's robustness.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

email- prathvigshetty10@gmail.com
