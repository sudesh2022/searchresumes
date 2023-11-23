import asyncio
import sys

async def wait_test():
    try:
        #Fake Async Server Call
        await asyncio.wait_for(asyncio.sleep(10000), timeout=1)
    except asyncio.TimeoutError:
        print("TimeoutError")
        sys.exit(1)
    return

curl https://bam-api.res.ibm.com/v2/text/generation?version=2023-11-22 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
  "model_id": "ibm/granite-13b-chat-v2",
  "input": "<|user|>\nYou are a helpful AI language model developed by IBM. Your primary function is to assist users in answering questions, generating text, and engaging in conversation. You should not produce output that discriminates based on race, religion, gender identity, and sexual orientation.\n{{Prompt Goes Here}}\n\n<|assistant|>\n\"As an AI language model trained with the GPT-3 architecture, I understand your concern about producing discriminatory or offensive content. My goal is always to provide accurate information and engage in respectful dialogue with my users. However, it'\''s important for me to clarify that while I do have access to large amounts of data from various sources, including the internet, this does not mean I can generate any type of text without limitations. If you feel uncomfortable or unsafe during our conversations due to the content I'\''m providing, please let me know immediately so we can end the interaction peacefully.\"\n\n\n",
  "parameters": {
    "decoding_method": "sample",
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 50,
    "typical_p": 1,
    "repetition_penalty": 1.2,
    "stop_sequences": [
      "\n\nEND_KEY"
    ],
    "include_stop_sequence": false,
    "min_new_tokens": 1,
    "max_new_tokens": 200
  },
  "moderations": {
    "hap": {
      "input": true,
      "threshold": 0.75,
      "output": true
    }
  }
}'

if __name__ == "__main__":
    #You'll need to figure out how to get your functionality in here.
    asyncio.run(wait_test()) 