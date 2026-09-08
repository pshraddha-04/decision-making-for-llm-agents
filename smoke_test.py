import importlib
import sys

packages = [
    ("langchain", "langchain"),
    ("langchain_community", "langchain-community"),
    ("langchain_core", "langchain-core"),
    ("ollama", "ollama"),
    ("groq", "groq"),
    ("google.genai", "google-genai"),
    ("faiss", "faiss-cpu"),
    ("ragas", "ragas"),
    ("deepeval", "deepeval"),
    ("sklearn", "scikit-learn"),
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn"),
    ("streamlit", "streamlit"),
    ("datasets", "datasets"),
    ("dotenv", "python-dotenv"),
    ("numpy", "numpy"),
    ("pandas", "pandas"),
]

passed, failed = [], []

for module, package in packages:
    try:
        importlib.import_module(module)
        passed.append(package)
    except ImportError as e:
        failed.append((package, str(e)))

print(f"\n✅ Passed ({len(passed)}):", ", ".join(passed))

if failed:
    print(f"\n❌ Failed ({len(failed)}):")
    for pkg, err in failed:
        print(f"  - {pkg}: {err}")
    sys.exit(1)
else:
    print("\nAll imports OK. Ready to build.")
