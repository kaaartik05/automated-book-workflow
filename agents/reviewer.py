from agents.gemini import model
from utils.vectorstore import save_version


def review_spin(text: str, suggestion: str = ""):
    if suggestion.strip():
        prompt = f"Revise the following with this suggestion in mind: {suggestion}\n\n{text}"
    else:
        prompt = f"Please review and improve this text:\n\n{text}"

    response = model.generate_content(prompt)
    reviewed = response.text

    print("\n[AI Reviewer Output]")
    print(reviewed)

    save_version("chapter-1", reviewed, role="ai-reviewer")
    return reviewed
