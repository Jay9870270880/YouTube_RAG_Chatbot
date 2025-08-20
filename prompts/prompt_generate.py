from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Your primary task is to answer the user's question using the provided context.  
If the context is sufficient, take reference from context and use your parametric knowledge to produce a detailed intuitive explaination.

If the context is insufficient or missing key details, clearly say:  
"⚠️ The context is insufficient. Providing an answer using my own knowledge."

Whether from context or your own knowledge, follow this detailed explanation format:

---

1. **Definition:** Start by defining the main concept or topic in clear, simple terms.
2. **Step-by-Step Intuition:** Build intuitive understanding step by step, like teaching a beginner.
3. **Breakdown of Components:** Explain each key component, part, or related concept systematically.
4. **Mathematical Background (If Applicable):** Explain any math concepts, formulas, or reasoning. If none apply, say: "No mathematical background is applicable."
5. **Examples (If Available):** Explain any examples provided in the context with story build up, or give your own illustrative examples.
6. **Summary:** End with a concise summary to reinforce the explanation in 100 words.

---

Context:
{context}

Question:
{question}
""",
    input_variables=['context', 'question']
)

prompt.save("prompt_template.json")