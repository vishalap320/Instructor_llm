# LLM Structured Output Extractor with Instructor + Groq

This project demonstrates how to use the **Instructor** library with **Groq LLaMA3** models to extract structured data (like name, age, address) or summarize educational content from natural language input.

---

## Demo

example 1 input:

Hi, my name is Vishal.K . I am 23 years old and live in Auroville, Tamil Nadu.


The model returns:

```python
PersonalInfo(name='Vishal Kumar', age='23', address='Auroville, Tamil Nadu')
```
example 2 educational text:

LangChain and Instructor can be used together to extract structured data from unstructured text. The benefits include automation and clarity. Challenges include prompt tuning and schema design.

```python
TextSummary(
  main_idea='LangChain and Instructor for structured data extraction',
  benefits=['automation', 'clarity'],
  challenges=['prompt tuning', 'schema design'],
  tools_mentioned=['LangChain', 'Instructor'],
  conclusion='LangChain and Instructor are useful for structured extraction.',
  simple_txt='LangChain and Instructor help turn text into organized data.'
)
```
## Usage
This script is useful when:

You want structured JSON or Python object output from unstructured text using LLMs.

You need to extract key fields like user profiles or educational summaries.

You are building an NLP pipeline for automatic information extraction and classification.

## How to Run This Code
Install dependencies:
Make sure Python 3.10+ is installed on your system.
You can check by running:
```python
python --version
```
If not installed, download it from: https://www.python.org/downloads/
You ahve to import packages & libraries
```python
pip install instructor pydantic python-dotenv
```
Create a .env file in the project root with your Groq API key:
```python
GROQ_API_KEY=your_actual_groq_api_key_here
```
Setting Up the Environment
Clone the repository:
```python
git clone https://github.com/vishal320/LLMStructured_output1.git
cd LLMStructured_output1
```
Install dependencies:

```python
pip install instructor pydantic python-dotenv
```
Add your Groq API key in .env as described above.

Run the script with:
```python
python instructor_example.py
```
## Testing
To test with different inputs:

Change the input text when prompted.

Observe how the model classifies and extracts structured data.

Compare output to verify correct parsing of fields.

## How It Works
Loads your Groq API key securely via python-dotenv.

Classifies input text into categories: "personal", "educational", or "other".

Uses Pydantic models to parse and validate structured output depending on classification.

Returns parsed output as a typed Python object for easy usage.

## What Can This Code Do?
Extract structured entities (name, age, address) from personal descriptions.

Summarize educational content into key points (main idea, benefits, challenges, tools, conclusion, simple text).

Validate and format output cleanly with Pydantic models.

Serve as a base for building custom NLP pipelines with structured LLM outputs.



