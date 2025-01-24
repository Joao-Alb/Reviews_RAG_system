# Google Reviews AI Query System

This open-source project combines cutting-edge technologies to enable the retrieval, summarization, and querying of Google Maps customer reviews. By leveraging the Outscraper API and OpenAI's GPT models, the system integrates a Retrieval-Augmented Generation (RAG) approach, utilizing the Llama\_Index library for efficient document indexing and query handling. Through embeddings, it ensures precise semantic search capabilities, offering users a robust tool to analyze reviews and extract actionable insights. The system fetches reviews from Google Maps, processes them into a structured format, and enables interactive querying using advanced AI models. This allows users to analyze reviews, extract key insights, and answer specific questions seamlessly.

---

## Features

- **Outscraper Integration**: Automatically fetch customer reviews for the last month from Google Maps using Outscraper.
- **OpenAI-Powered Query Engine**: Summarize and query review data using OpenAI's GPT models.
- **Interactive Query System**: Engage in a conversational interface to retrieve insights from review data.

---

## Installation

### Prerequisites

1. Python 3.8 or higher.
2. An OpenAI API key.
3. An Outscraper API key.
4. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

### Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a `.env` file to store sensitive information:

   ```plaintext
   OPENAI_API_KEY=<your_openai_api_key>
   OUTSCRAPER_API_KEY=<your_outscraper_api_key>
   CUSTOMER_PLACE_ID=<place_id>
   ```

3. The `.env` file and `avaliacoes.json` (reviews data) are ignored by Git to protect sensitive customer data.

4. Install any additional dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

```plaintext
.
├── Agent.py          # Query engine for document summarization and context retrieval
├── avaliacoes.json   # Review data fetched from Outscraper (ignored in .gitignore)
├── main.py           # Main script to interact with the system
├── outscraper.py     # Functions for fetching reviews using the Outscraper API
├── prompts.json      # Contains system prompts for the query engine
├── secret.py         # Handles secure retrieval of API keys
├── unix.py           # Utility to calculate timestamps
├── .env              # Stores API keys (ignored in .gitignore)
├── .gitignore        # Specifies ignored files
```

---

## Usage

1. **Run the System**:

   ```bash
   python main.py
   ```

2. The program works as follows:

   - Fetches Google Maps reviews for the last month using Outscraper.
   - Saves the reviews in a JSON file (avaliacoes.json).
   - Processes the reviews to allow interactive querying and summarization using OpenAI's GPT models.
   - Allow you to ask questions interactively, such as:
     - "Summarize the customer feedback."
     - "What are the most common complaints?"

3. Example:

   ```plaintext
   Voce: Summarize the reviews for this month.
   Seu agente de IA: The reviews highlight excellent customer service and fast delivery but mention occasional issues with product quality.
   ```

---

## Configuration

- **Prompts**: Customize the `prompts.json` file to adjust the behavior of the query engine.
- **Ignored Files**: The `.env` and `avaliacoes.json` are excluded from version control to protect sensitive data.

---

## Notes

- This system relies on the availability of Outscraper and OpenAI APIs.
- Ensure that API usage limits are sufficient for your needs.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions

Contributions are welcome! Please create an issue or submit a pull request to suggest improvements or report bugs.

---

## Disclaimer

This project is designed for educational and informational purposes. Use responsibly and ensure compliance with local regulations when processing user data.
