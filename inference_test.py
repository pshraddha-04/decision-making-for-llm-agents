from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()
response = client.chat.completions.create(model="qwen/qwen3.6-27b", messages=[{"role": "user", "content": "What is Kafka?"}])
print(response.choices[0].message.content)
