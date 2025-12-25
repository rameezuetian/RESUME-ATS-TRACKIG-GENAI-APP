# 📄 AI-Powered ATS Resume Tracking System

An **AI-based Applicant Tracking System (ATS)** built using **Google Gemini 1.5** and **Streamlit**.
This app analyzes resumes against job descriptions and provides **ATS match percentage, HR-style evaluation, and skill improvement suggestions**.

---

## 🚀 Features

* 📑 Resume vs Job Description analysis
* 🤖 AI-powered ATS percentage match
* 🧠 HR-style strengths & weaknesses review
* 🛠 Skill gap & improvement suggestions
* ⚡ Native PDF processing (no OCR / no Poppler)

---

## 🧠 AI Model

* **Google Gemini 1.5 Flash / Pro**

  * Supports PDF input directly
  * Long-context understanding
  * High accuracy resume parsing

---

## 🛠 Tech Stack

* Python 🐍
* Streamlit 🎈
* Google Generative AI (Gemini 1.5)
* dotenv

---

## 📂 Project Structure

```
ATS-Resume-Tracking-App/
│
├── app.py
├── README.md
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ats-resume-tracking.git
cd ats-resume-tracking
```

### 2️⃣ Create Virtual Environment

```bash
conda create -n ats-ai python=3.10
conda activate ats-ai
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. Upload your **resume (PDF)**
2. Paste the **job description**
3. Choose an option:

   * Resume Evaluation
   * Skill Improvement
   * ATS Match Percentage
4. Get AI-generated insights instantly ⚡

---

## 📊 Sample Output

* **ATS Match:** 82%
* **Matched Skills:** Python, Machine Learning, Data Analysis
* **Missing Skills:** Docker, FastAPI
* **Suggestions:** Add quantified achievements and relevant projects

---

## 🔐 Security

* API keys stored using `.env`
* `.env` excluded from GitHub commits

---

## 🌟 Future Improvements

* 📥 Download ATS report (PDF)
* 📊 Skill-wise scoring
* 🔍 Resume keyword heatmap
* 🐳 Docker deployment
* ☁️ Cloud hosting (Streamlit / HuggingFace)

---

## 👨‍💻 Author

**Muhammad Rameez**
AI / ML Engineer | Data Scientist
UET Lahore

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 💬 Share feedback

---

If you want, I can also:

* Generate `requirements.txt`
* Optimize README for **recruiters**
* Write a **GitHub description**
* Create a **LinkedIn post** for this project 🚀
