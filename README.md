ai_task_assistant/
│
├── backend/
│   ├── main.py             # FastAPI entrypoint
│   ├── database.py         # DB connection (SQLAlchemy)
│   ├── models/             # SQLAlchemy models
│   │    ├── user.py
│   │    └── task.py
│   ├── schemas/            # Pydantic schemas
│   │    ├── user.py
│   │    └── task.py
│   ├── routers/
│   │    ├── auth.py
│   │    └── tasks.py
│   ├── services/           # Business logic, AI calls
│   │    └── langchain_service.py
│   └── utils/              # Helper functions (hash password, JWT)
│        └── auth.py
│
├── frontend/
│   └── app.py              # Streamlit frontend
│
├── .env
├── requirements.txt
└── README.md
