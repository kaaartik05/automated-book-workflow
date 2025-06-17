from agents.gemini import model
from utils.vectorstore import save_version


def spin_book(prompt: str):
    response = model.generate_content(prompt)
    output = response.text

    print("\n[AI Writer Output]")
    print(output)

    save_version("chapter-1", output, role="ai-writer")
    return output
