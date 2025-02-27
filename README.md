# CITY&#8226;HUB

CityHub is an AI-powered conversational assistant designed to help residents and visitors easily access information about San Francisco's city services and resources. By leveraging advanced language models like Meta's Llama 3 and knowledge graphs, CityHub provides interactive, personalized guidance to help users navigate the complex landscape of local government.

## Background

This is the project submitted for the [Meta Llama 3 Hackathon](https://metallama3.devpost.com/) (May 11/12 2024).  The project was shortlisted for the Final 8 amongst 52 projects.
https://devpost.com/software/cityhub

## Team members

- [JP Zhang](https://github.com/jpzhangvincent)
  - Prototyped the Adaptive RAG module and Agent framework in `langchain` and `langgraph`
  - Implemented the backend LLM API in `fastAPI` and integrated with the frontend UI
- [Rama Narasimhan](https://github.com/Rama4) (Front end)
- [Colin Alexander](https://github.com/colinalexander) (Back end)
  - Utilized [Groq](https://wow.groq.com/why-groq/) with the `llama3-70b-8192` model to generate responses to user messages in the `groq_it()` function.
  - Leveraged [ScrapegraphAI](https://github.com/VinciGit00/Scrapegraph-ai) with Groq's `llama3-8b-8192` model for the LLM and Ollama's `nomic-embed-text` model for embeddings to scrape data from the San Francisco government [website](https://www.sf.gov/). 
  - Used LLM prompts to guide the scraping.

## Project documents

- [Presentation slides](https://docs.google.com/presentation/d/19K0d0pSgpOjFar9P9ySab2wHj8nlm7HHAY9KsvACke0/edit#slide=id.g27113729c33_0_57)
- [Project plan](https://docs.google.com/document/d/17ufgJSBhHJsN_bcrvRLMrHKD5v6RGgRLk7vG0Gkhkv0/edit?pli=1)
- [Demo video](https://www.youtube.com/watch?v=_roTeEO92es)

## Installation

To run CityHub locally, follow these steps:

1. Clone the repository
```
git clone https://github.com/colinalexander/city-hub.git
```

2. Create and activate virtual environment
Create your project folder. Then create your virtual environment and activate it.

```
cd my/project/root/folder
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up the necessary environment variables
```
cp .env-example .env
# EDIT NEW .env FILE AND ENTER VALID API KEYS WHERE REQUIRED
```

5. Run the application:
Run the client:
```
cd client
npm start
```

6. Open your browser and navigate to `http://localhost:3000` to start chatting with CityHub.

## Usage

To interact with CityHub, simply type your question or request in the chat interface. CityHub will process your input and provide a relevant, informative response. You can ask follow-up questions, request clarifications, or explore related topics as needed.
Some example queries:

- "How do I apply for a residential parking permit?"
- "What are the recycling guidelines in San Francisco?"
- "What's the best way to get from the Castro to the Ferry Building using public transportation?"

CityHub will guide you through the process, provide step-by-step instructions, and offer personalized recommendations based on your needs.

### Sample output

Here's an example of a conversation with CityHub:
```
User: How can I reserve a picnic area in Golden Gate Park?
CityHub: To reserve a picnic area in Golden Gate Park, you'll need to contact the San Francisco Recreation and Parks Department. Reservations can be made online, by phone, or in person. You'll need to provide the date, time, location, and number of people in your party. There is a fee for reservations, which varies based on the size of the picnic area. Shall I assist you with finding the reservation website?

User: Yes, please provide the link.
CityHub: Certainly! You can reserve a picnic area in Golden Gate Park by visiting the San Francisco Recreation and Parks Department website at https://sfrecpark.org/permits-and-reservations/picnic-areas/. From there, you can select your desired location, date, and time, and complete the online reservation form. Let me know if you have any other questions!
```

## Open issues

- Expand CityHub's knowledge base to cover more city services and resources
- Improve the natural language understanding capabilities to handle more complex queries
- Integrate with more data sources to provide real-time information (e.g., transit schedules, event calendars)
- Enhance the user interface with visual elements and multimedia content
- Implement multi-language support to serve San Francisco's diverse population
- Expand to other cities!

## FAQs

Q: _How is CityHub different from Google?_\
A:  CityHub offers a more personalized, interactive, and efficient experience compared to using a search engine like Google. While Google is a powerful tool for general information searching, CityHub offers a more specialized, user-friendly, and efficient experience tailored specifically for navigating San Francisco's city services and resources.
- Conversational Interface: \
  CityHub provides a natural, dialogue-based interface that allows users to ask questions and receive responses in a conversational manner. This makes it easier for users to find the information they need without having to sift through search results and web pages.
- Personalized Guidance: \
  CityHub can provide step-by-step instructions, recommendations, and context-specific advice based on the user's individual needs and questions. This level of personalization is difficult to achieve with a generic search engine.
- Curated Knowledge Base: \
  CityHub's knowledge base is specifically curated for San Francisco city services and resources, ensuring that users receive accurate, relevant, and up-to-date information. With Google, users may have to navigate through multiple websites to find the information they need.
- Efficient Information Retrieval: \
  By leveraging advanced language models and knowledge graphs, CityHub can quickly understand the user's intent and provide concise, targeted responses. This saves users time and effort compared to manually searching through Google results.
- Interactive Follow-up: \
  CityHub can engage in multi-turn conversations, allowing users to ask follow-up questions, request clarifications, and explore related topics seamlessly. This interactive nature makes it easier for users to find the information they need without having to start new searches.
  
Q: _Is CityHub an official service provided by the City of San Francisco?_\
A: No, CityHub is an independent project developed by a team of AI enthusiasts and is not affiliated with the San Francisco government.

Q: _How does CityHub protect user privacy_?\
A: CityHub does not store any personally identifiable information from user interactions. All conversations are processed anonymously and are not linked to individual users.

Q: _Can CityHub help me with issues related to private businesses or organizations_?\
A: No, CityHub's knowledge base is focused on San Francisco's public services and resources. For inquiries related to private entities, please contact the relevant business or organization directly.

Q: _How can I contribute to the development of CityHub_?\
A: We welcome contributions from the community! Please check our contributing guidelines for more information on how to get involved.

Q: _Who can I contact for more information about CityHub_?\
A: If you have any questions, suggestions, or feedback, please open an issue on our GitHub repository.

## Tech stack

- https://github.com/meta-llama
- https://github.com/groq/groq-python
- https://github.com/ollama/ollama-python
- https://brave.com/search/api/
- https://github.com/facebook/react
- https://github.com/tiangolo/fastapi

