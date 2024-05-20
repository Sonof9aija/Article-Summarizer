# Article-Summarizer
This Python application uses the `tkinter` library to create a graphical user interface (GUI) that allows users to input a URL of an article, summarize the article, and optionally translate the summary into a specified language. The `newspaper3k` library is used to scrape and process the article, and the `deep_translator` library is used for translating the summary.

## Requirements

To run this application, you need to have Python installed along with the following libraries:

- `tkinter`: For creating the GUI.
- `newspaper3k`: For extracting and summarizing the article.
- `deep_translator`: For translating the summary.

## Installation

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Install Required Libraries**: Open your command prompt or terminal and run the following commands:

    ```bash
    pip install tkinter
    pip install newspaper3k
    pip install deep-translator
    ```

## Usage

1. **Run the Script**: Save the provided code into a Python file, for example `article_summarizer.py`, and run it using the command:

    ```bash
    python article_summarizer.py
    ```

2. **User Interface**: The application window will open with fields to input the article URL and the desired language for translation.

3. **Input Fields**:
    - **Article URL**: Enter the URL of the article you want to summarize.
    - **Language**: Enter the language code or language name for translation (leave empty for no translation).

4. **Buttons**:
    - **Summarize**: Click this button to summarize the article. If a language is specified, the summary will be translated to that language.
    - **Click if translate not working**: Clicking this link will open a new window displaying the list of supported languages and their codes.
