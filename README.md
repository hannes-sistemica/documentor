# DocuMentor

DocuMentor is a retrieval-augmented generation (RAG) web application that utilizes the content of uploaded PDF files to provide enhanced, context-aware responses to user queries. Leveraging the power of advanced natural language processing, DocuMentor aims to deliver precise information by understanding and incorporating the knowledge embedded in PDF documents.

## Features

- **PDF Upload**: Users can upload PDF documents which the app will use as additional context for generating answers.
- **Query Processing**: Submit questions and receive contextually relevant answers, with insights derived directly from the uploaded PDFs.
- **Contextual Understanding**: Advanced algorithms ensure that the app understands the context of user queries, resulting in accurate and informative responses.

## Getting Started

These instructions will guide you through setting up DocuMentor on your local machine for development and testing purposes.

### Prerequisites

Here's what you need to install the software and how to install them:

- Python 3.8 or higher
- Python's venv module (for creating virtual environments)
```

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the database**:
   ```bash
   make start-db
   ```

6. **Run the application locally**:
   ```bash
   make run
   ```

7. **Stop the database**:
   ```bash
   make stop-db
   ```

### Running with Docker Compose

1. **Start the application and database**:
   ```bash
   make run-docker
   ```

2. **Stop the application and database**:
   ```bash
   make stop-docker
   ```
