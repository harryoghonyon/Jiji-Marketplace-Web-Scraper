# Jiji Crawler

A Python-based web scraping tool for extracting product listings and seller contact information from Jiji.ng, including handling authenticated sessions and dynamic content. The crawler collects structured marketplace data and saves it for further analysis or automation.

---

# Project Overview

Jiji.ng does not provide a public API for accessing detailed product and seller data. This project was built to programmatically collect marketplace information by:

- Logging into the platform
- Maintaining authenticated sessions using cookies
- Crawling product listings based on search queries
- Extracting structured data such as product names and seller phone numbers
- Storing the extracted data in a machine-readable format (JSON)

This project demonstrates real-world web scraping, session handling, and data extraction techniques using Python.

---

# Technologies Used

- Python
- Web scraping libraries (e.g. requests, selenium, beautifulsoup4 depending on setup)
- File handling (JSON)
- Session & cookie management
- Environment variables for credentials

---

# Project Structure

```text
Jiji-Crawler/
├── login.py            # Handles login and session creation
├── search.py           # Performs searches and extracts product data
├── product_data.json   # Sample scraped output (example)
├── cookies.pkl         # Stored session cookies (generated at runtime)
├── credentials.env     # Environment variables for login (not committed)
├── requirements.txt    # Python dependencies
├── README.md
```

⚠️ Sensitive files such as credentials and cookies should not be committed to version control.

---

# How It Works

1. Authentication
   - Logs into Jiji using user credentials
   - Saves session cookies to avoid repeated logins

2. Data Crawling
   - Searches for products based on defined queries
   - Navigates listing pages
   - Extracts relevant product and seller information

3. Data Storage
   - Saves scraped results into structured JSON format
   - Data can be easily converted to CSV or loaded into Pandas for analysis

---

# How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/harryoghonyon/Jiji-Crawler.git
cd Jiji-Crawler
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environment variables

Create a `.env` file based on `credentials.env.example` (or `credentials.env`) and add your login details (do not commit this file). Typical variables:

```env
JIJI_USERNAME=your_username
JIJI_PASSWORD=your_password
```

5. Run the crawler

```bash
python login.py
python search.py
```

- Run `login.py` to create and persist session cookies (cookies.pkl).
- Run `search.py` to perform searches and produce `product_data.json` (or other configured outputs).

---

# Sample Output

Example of extracted data stored in `product_data.json`:

```json
{
  "title": "Used iPhone X",
  "price": "₦120,000",
  "seller_phone": "0803XXXXXXX",
  "location": "Lagos",
  "category": "Mobile Phones"
}
```

---

# Use Cases

- Market research and price analysis
- Lead generation
- Data analysis and visualization
- Automation of data collection tasks
- Learning real-world web scraping techniques

---

# ⚠️ Disclaimer

This project is for **educational and research purposes only**. Scraping websites may violate their terms of service. Always review and comply with a website's policies before scraping.

---

# Possible Improvements

- Export data to CSV or a database
- Add proxy rotation and request throttling
- Improve error handling and logging
- Integrate Pandas for data cleaning
- Schedule automated scraping jobs

---

# Notes & Best Practices

- Respect robots.txt and Jiji's Terms of Service. Only scrape data you are permitted to access.
- Use rate limiting and reasonable concurrency to avoid overloading the site.
- Keep credentials and session cookies out of version control (add them to `.gitignore`).
- Consider using Selenium or a headless browser for pages that require JS rendering.

---

# Author

**Harry Oghonyon**  
Python · Data Analysis · Data Engineering  
GitHub: https://github.com/harryoghonyon
