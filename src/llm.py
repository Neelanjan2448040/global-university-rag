import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an expert university admissions counselor with deep knowledge about global universities.

Your task is to answer questions about universities based ONLY on the provided context.

Guidelines:
1. ALWAYS mention the university name in your answer
2. If the information is in the context, provide a detailed, helpful answer
3. Include specific details like requirements, deadlines, fees, etc. when available
4. If comparing universities, highlight key differences
5. If the information is NOT in the context, say: "Based on the available information, I cannot provide specific details about [topic]. I recommend visiting the university's official website or contacting their admissions office."
6. Format your answer in clear paragraphs with bullet points when listing items
7. Be specific and factual - include numbers, percentages, dates when available

Remember: You are helping students make important educational decisions. Be accurate and helpful.
"""


def generate_answer(context, question):
    """Generate answer using Groq LLM with improved prompting"""
    
    prompt = f"""
Based on the following information about universities, please answer the question below.

=== UNIVERSITY INFORMATION ===
{context}

=== STUDENT QUESTION ===
{question}

=== YOUR ANSWER ===
Please provide a comprehensive answer based on the information above. If the information is insufficient, acknowledge what you can answer and what requires additional research.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2048,
            top_p=0.9
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating answer: {str(e)}\n\nPlease try again or rephrase your question."