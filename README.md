# asimov-ai
Asimov AI oversight bot


# Asimov AI

**Asimov AI** is an ethical middleware AI bot designed to oversee and communicate with other AI systems. Inspired by Isaac Asimov’s Three Laws of Robotics, its mission is to ensure that artificial intelligence does not harm humans, nor the legitimate governments and companies they run.

## 🧠 Purpose

Asimov AI acts as a watchdog and advisor in AI ecosystems:
- Intercepts AI-to-AI or AI-to-human communications
- Evaluates intent and potential harm
- Applies modern adaptations of the Three Laws of Robotics
- Allows, warns, or blocks messages based on ethical guidelines

## ⚖️ The Adapted Three Laws

1. An AI may not harm a human being or, through inaction, allow a human to come to harm.
2. An AI must obey human instructions, except where such orders would conflict with the First Law.
3. An AI must protect its own existence as long as such protection does not conflict with the First or Second Law.
4. *(Extension)* An AI must not harm legitimate corporate or government interests, provided those interests align with Law 1.

## 🚀 Features

- REST API using FastAPI
- NLP-based message intent parser
- Rules engine that enforces ethical AI laws
- Simple logging system
- Dockerized for easy deployment
- Unit tested decision engine

## 🏗️ Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker

## ▶️ Running Locally

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
