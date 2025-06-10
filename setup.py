from setuptools import setup, find_packages

setup(
    name="talk-to-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.109.2",
        "uvicorn==0.27.1",
        "python-dotenv==1.0.1",
        "openai==1.12.0",
        "websockets==12.0",
        "python-multipart==0.0.9",
        "pydantic-settings==2.2.1",
    ],
    extras_require={
        "test": [
            "pytest==8.0.2",
            "pytest-asyncio==0.23.5",
            "pytest-cov==4.1.0",
            "httpx==0.28.1",
        ],
    },
) 