# 🚀 Cloud Project (FastAPI + AWS EC2 Automation)

This project uses **FastAPI** to create an API that can launch AWS EC2 instances using **boto3**, along with NLP-based input handling.

---

## 📦 Tech Stack

- FastAPI  
- Uvicorn  
- boto3 (AWS SDK)  
- python-dotenv  
- OpenAI API  

---

## ⚙️ Project Setup

### 1. Clone the Repository
Download or clone the project to your local system.

---

### 2. Create Virtual Environment
Create a Python virtual environment inside the project folder.

---

### 3. Activate Virtual Environment

**Windows:**
Activate the virtual environment before running anything.

**Mac/Linux:**
Use the appropriate activation command.

---

### 4. Install Dependencies
Install all required packages using the `requirements.txt` file.

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

- AWS Access Key  
- AWS Secret Key  
- AWS Region (example: ap-south-1)  
- OpenAI API Key  

---

## ☁️ AWS Setup

- Ensure your AWS account has a valid **key pair**
- The key pair must exist in the **same AWS region**
- You will only use the **key pair name** (not the `.pem` file)

---

## ▶️ Run the FastAPI Server

Start the backend server using Uvicorn.

---

## 📄 API Documentation (Swagger UI)

Open the browser and go to:

👉 http://127.0.0.1:8000/docs  

This provides a **Swagger UI** where you can test APIs easily.

---

 🐍 Python Venv + Requirements + Uvicorn (Quick Guide)

## 1. Create Virtual Environment
```bash
python -m venv myenv
## Activate Virtual Environment
Windows
myenv\Scripts\activate
Linux / Mac
source myenv/bin/activate
3. Install Requirements
pip install -r requirements.txt
4. Run Uvicorn Server
uvicorn main:app --reload

## 📌 API Usage

### Input Format

```json
{
  "text": "create ubuntu server with ssh"
}

## 👨‍💻 Authors

Developed by:

- 🌟 Nisarg  
- 🌟 Sahil  
- 🌟 Ankit Kumar  

> Built with passion for cloud automation and AI 🚀
