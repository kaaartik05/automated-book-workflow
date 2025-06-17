# Automated Book Publication Workflow

This project builds an end-to-end system that scrapes a chapter from a website, spins it using AI (Gemini), allows human-in-the-loop editing, and saves finalized versions with search and versioning support.

Built as part of an evaluation assignment. Check out the demo video and explore the code.

---

## Features

- Web Scraping using Playwright with screenshot capture
- AI Writer and Reviewer powered by Gemini API
- Human-in-the-Loop review flow
- Content Versioning using ChromaDB
- Reinforcement Learning-based retrieval for past content

---

## Tech Stack

Python is used as the primary development language along with:

- Playwright for scraping and screenshots
- Gemini API for AI writing and reviewing
- ChromaDB for versioning and search
- Custom RL reranker for intelligent retrieval
- Git for version control

---

## Folder Structure

automated-book-workflow/
|
├── main.py                      - Project entry point  
├── chapter_text.txt             - Extracted chapter content  
├── chapter_screenshot.png       - Screenshot of the webpage  
├── agents/                      - AI writer, reviewer, spinner agents  
├── utils/                       - Scraper, reranker, vectorstore  
├── requirements.txt             - Python dependencies  
└── README.md                    - Project documentation  

---

## Demo Video

Link to demo video: https://www.loom.com/share/05793ccb289549d9a3667f21cd874a75?sid=e64c547b-45d8-4629-8eb6-8d904a86b5fc

---

## Author

Name: Kartik  
GitHub: https://github.com/kaaartik05
