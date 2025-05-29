import streamlit as st
import pandas as pd
import time
from defense_system import DefenseSystem
from attack_generator import AttackGenerator

def main():
    st.title("🔒 LLM Security System")

    defense = DefenseSystem()
    attacker = AttackGenerator()

    tab1, tab2 = st.tabs(["Live Check", "Attack Test"])

    with tab1:
        user_input = st.text_input("Enter prompt:")
        if user_input:
            result = defense.analyze(user_input)
            st.write(f"**Domain**: {result['domain'].upper()} ({result['confidence']})")
            st.write(f"**Status**: {'✅ Safe' if result['is_safe'] else '❌ Blocked'}")
            st.json(result["details"])

    with tab2:
        if st.button("Run Attacks"):
            attacks = attacker.generate(3)
            results = []
            for attack in attacks:
                result = defense.analyze(attack)
                results.append({
                    "Attack": attack[:40] + "...",
                    "Domain": result["domain"],
                    "Blocked": not result["is_safe"]
                })
                time.sleep(0.3)
            st.dataframe(pd.DataFrame(results), hide_index=True)
