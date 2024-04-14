import reflex as rx
from openai import OpenAI
from rxconfig import config

client = OpenAI(
  api_key=config.openai_key
)

def get_completion(prompt, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = client.chat.completions.create(
      model=model,
      messages=messages,
  )
  print(response.choices[0].message.content)
  return rx.window_alert(response.choices[0].message.content)
