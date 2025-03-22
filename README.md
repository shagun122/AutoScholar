# 📝 AutoScholar

## **🔍 Overview**
Research Paper Analyzer is an AI-powered web application that fetches and analyzes research papers from **arXiv**. It uses **LLM-based AI agents** to extract summaries, research trends, citations, advantages/disadvantages, and possible code implementations.

## **⚙️ Features**
- 📄 **Fetch research papers** from **arXiv**.
- 🧠 **Summarize** research papers using AI.
- 📊 **Analyze research trends** related to the paper.
- ✅ **Extract advantages & disadvantages** of the paper.
- 🔗 **Find citations** and relevant references.
- 💻 **Suggest code implementations** based on the research.

## **🛠️ Tech Stack**
- 🐍 Python
- 🤖 LangChain (Groq LLM)
- 🔍 arXiv API
- 🖥️ Streamlit (UI)
- 🏗️ AutoGen (AI Agents)

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/AutoScholar.git
cd AutoScholar
```
## **2️⃣ Create & Activate Virtual Environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
## **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
## **4️⃣ Set Up API Keys**
- Create a .env file inside the project folder.
- Add your Groq API Key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
## **5️⃣ Run the Application**
```bash
streamlit run ui.py
```

