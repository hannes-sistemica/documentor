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

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies and set up the virtual environment**:
   ```bash
   make install-local
   ```

3. **Start the local database**:
   ```bash
   make db-start-local
   ```

4. **Run the application locally**:
   ```bash
   make run-local
   ```

5. **To stop the local database**:
   ```bash
   make db-stop-local
   ```

### Docker Setup

To run the application in Docker:

1. **Build the Docker image**:
   ```bash
   make docker-build
   ```

2. **Start the application and database in Docker**:
   ```bash
   make docker-run
   ```

3. **To stop the Docker containers**:
   ```bash
   make docker-stop
   ```

### Ollama Setup

To use the Ollama LLM provider, ensure that you have Ollama running with the corresponding models. You can configure the host URL and default model in the `.env.local` and `.env.docker` files.

### Environment Configuration

- For local development, edit `.env.local`
- For Docker deployment, edit `.env.docker`

The appropriate environment file will be copied to `.env` when running the application using the provided make commands.
