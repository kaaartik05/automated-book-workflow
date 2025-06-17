from utils.scrape import scrape_chapter
from agents.spin import spin_book
from agents.reviewer import review_spin
from utils.vectorstore import search_versions

# Step 0: Scrape content
scrape_chapter()

# Step 1: Spin (AI Writer)
prompt = "Write a short poem about the monsoon in India"
output = spin_book(prompt)

# Step 2: Show similar previous versions
print("\n Similar saved versions:")
results = search_versions("monsoon poem")
for doc in results['documents'][0]:
    print(f"- {doc[:100]}...")

# Step 3: Human-in-the-loop Review
print("\n [Human Review Mode]")
suggestion = input("Enter your suggestions for the reviewer (optional): ")

# Step 4: AI Review
reviewed_output = review_spin(output, suggestion)

# Step 5: Final output
print("\n Reviewed and saved successfully.")
