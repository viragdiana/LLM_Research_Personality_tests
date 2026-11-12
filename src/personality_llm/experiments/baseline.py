
import os
import json
from datetime import datetime
from pathlib import Path
from google import genai


MODEL_NAME = "gemini-3.6-flash"

# Example assessment results supplied by the user.
USER_PROFILE = {
    "mbti": "INTJ",
    "enneagram": {
        "type": 5,
        "wing": None
    }
}

QUESTION = "What study method might suit me best?"

def save_result(profile, question, answer):

    results_file = Path("results/baseline_results.md")
    results_file.parent.mkdir(parents=True, exist_ok=True)

    with results_file.open("a", encoding="utf-8") as file:
        file.write(f"\n## Test — {datetime.now().astimezone().isoformat(timespec='seconds')}\n")
        file.write(f"\n**Approach:** Baseline (no RAG)\n")
        file.write(f"\n**Model:** {MODEL_NAME}\n")
        file.write(f"\n**Profile:** {profile}\n")
        file.write(f"\n**Question:** {question}\n")
        file.write(f"\n### Response\n\n{answer}\n")
        file.write("\n### Observations\n\n")
        file.write("[Add your observations here.]\n")
        file.write("\n---\n")


def run_baseline(profile, question):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Check your environment variable."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are an assistant helping users understand their personality
    assessment results and answer questions based on them.

    Treat personality frameworks as interpretive tools, not
    scientifically conclusive descriptions of a person.

    Do not assume that everyone with the same personality type
    behaves identically.

    User profile:
    {json.dumps(profile, indent=2)}

    User question:
    {question}

    Give a practical, personalized answer and explain your reasoning.
    """
    print("\nSending request to Gemini...", flush=True)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    print("=== Personality LLM Baseline ===\n")

    mbti = input("Enter your MBTI type (e.g. ENTJ): ").strip().upper()
    enneagram = input("Enter your Enneagram type (e.g. 3w4): ").strip()

    question = input("\nEnter your question: ").strip()

    user_profile = {
        "mbti": mbti,
        "enneagram": enneagram
    }

    answer = run_baseline(user_profile, question)

    print("\n=== Gemini Response ===\n")
    print(answer)
    save_result(user_profile, question, answer)
    print("\nResult saved to results/baseline_results.md")