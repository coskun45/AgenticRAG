Collecting workspace information

# README

## Overview

This project is a document retrieval and question-answering system that leverages various machine learning models and tools to provide answers to user queries. The system is designed to handle questions related to Islamic principles, the Quran, and contemporary issues in accordance with Islamic teachings.

## Project Structure

```
.
├── .chromadb/
│   ├── 73fa11c1-f242-47c2-bffd-274450aae22b/
│   │   └── index_metadata.pickle
│   └── chroma.sqlite3
├── .env
├── .gitignore
├── get_retriever.py
├── graph/
│   ├── __init__.py
│   ├── chains/
│   │   ├── __init__.py
│   │   ├── answer_grader.py
│   │   ├── generation.py
│   │   ├── hallucination_grader.py
│   │   ├── retrieval_grader.py
│   │   └── router.py
│   ├── graph.py
│   ├── node_constants.py
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── generate.py
│   │   ├── grade_documents.py
│   │   ├── retrieve.py
│   │   └── web_search.py
│   └── state.py
├── ingestion.ipynb
├── KnowledgeBase/
├── main.py
├── myenv/
├── pdf/
├── requirements.txt
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a 

.env

 file in the root directory and add necessary environment variables.

## Usage

1. **Ingest documents:**
   Use the 

ingestion.ipynb

 notebook to load and process documents into the vector store.

2. **Run the application:**
   ```sh
   python main.py
   ```

## Files and Directories

- **

get_retriever.py

**: Contains the code to set up the document retriever using Chroma and SentenceTransformerEmbeddings.
- **

graph

**: Contains the main logic for the state graph, nodes, and chains used in the question-answering workflow.
- **`ingestion.ipynb`**: Jupyter notebook for ingesting documents into the vector store.
- **`main.py`**: Entry point for running the application.
- **`requirements.txt`**: Lists the dependencies required for the project.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please open an issue in the repository or contact the maintainer.

