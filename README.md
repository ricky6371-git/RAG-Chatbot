# 📚 RAG Chatbot – Chat with Multiple PDFs

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with  **LangChain** ,  **Google Gemini** ,  **FAISS** , and  **Streamlit** .

It allows users to **upload multiple PDF documents** and then  **chat with them interactively** .

The app extracts text from PDFs, chunks it, embeds it using  **Google Generative AI Embeddings** , stores it in a  **FAISS vector database** , and then uses **Conversational Retrieval Chains** to generate context-aware answers.

---

## 🚀 Features

* Upload multiple PDFs and query them instantly.
* Text extraction with  **PyPDF** .
* Smart text chunking for better retrieval.
* Vector search using  **FAISS** .
* Conversational memory to maintain context.
* Interactive UI built with  **Streamlit** .
* Custom chat interface with user and bot avatars.

---

## 🛠️ Installation

1. **Clone the repository**

<pre class="overflow-visible!" data-start="1050" data-end="1134"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/ricky6371-git/RAG-Chatbot
</span><span>cd</span><span> RAG-Chatbot
</span></span></code></div></div></pre>

2. **Create and activate a virtual environment**

<pre class="overflow-visible!" data-start="1187" data-end="1297"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
venv\Scripts\activate   </span><span># On Windows</span><span>
</span><span>source</span><span> venv/bin/activate   </span><span># On Mac/Linux</span><span>
</span></span></code></div></div></pre>

3. **Install dependencies**

<pre class="overflow-visible!" data-start="1329" data-end="1372"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

4. **Set up environment variables**

   Create a `.env` file in the root directory with your Google API key:

<pre class="overflow-visible!" data-start="1483" data-end="1530"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>GOOGLE_API_KEY</span><span>=your_google_api_key_here
</span></span></code></div></div></pre>

---

## ▶️ Usage

Run the Streamlit app:

<pre class="overflow-visible!" data-start="1577" data-end="1609"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>streamlit run app.py
</span></span></code></div></div></pre>

Upload your PDFs from the  **sidebar** , click  **Process** , and start asking questions!

---

## 📂 Project Structure

<pre class="overflow-visible!" data-start="1731" data-end="2194"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>RAG_CHATBOT/
│── app.py                </span><span># Main Streamlit app</span><span>
│── html_templates.py     </span><span># Custom CSS & chat templates</span><span>
│── requirements.txt      </span><span># Dependencies</span><span>
│── .</span><span>env</span><span></span><span># API keys (not tracked in Git)</span><span>
│── .gitignore            </span><span># Ignore sensitive & unnecessary files</span><span>
│── user.png              </span><span># User avatar</span><span>
│── bot.png               </span><span># Bot avatar</span><span>
│── test.py               </span><span># (Optional) test file</span><span>
│── .python-version       </span><span># Python version file</span><span>
</span></span></code></div></div></pre>

---

## 🖼️ UI Preview

Here’s what the interface looks like:

---

## ⚡ Tech Stack

* **LangChain** – Conversational AI framework
* **Google Gemini API** – Embeddings + Chat LLM
* **FAISS** – Vector database for retrieval
* **Streamlit** – Web UI
* **PyPDF** – PDF parsing

---

## 🔮 Future Improvements

* Support for more file types (Word, Excel, etc.)
* Enhanced summarization for large documents
* Option to save and reload chat history
