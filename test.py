import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_mcq(prompt):
    # You can customize the temperature and max_tokens based on your preferences
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n = 1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    return generated_text



context = '''The female reproductive system consists of a pair of ovaries alongwith a pair
of oviducts, uterus, cervix, vagina and the external genitalia located in
pelvic region (Figure 2.3a). These parts of the system alongwith a pair of the
mammary glands are integrated structurally and functionally to support
the processes of ovulation, fertilisation, pregnancy, birth and child care.
Ovaries are the primary female sex organs that produce the female
gamete (ovum) and several steroid hormones (ovarian hormones).
The ovaries are located one on each side of the lower abdomen
(Figure 2.3b). Each ovary is about 2 to 4 cm in length and is connected to
the pelvic wall and uterus by ligaments. Each ovary is covered by a thin
epithelium which encloses the ovarian stroma. The stroma is divided into
two zones – a peripheral cortex and an inner medulla.
'''

# Example usage
prompt = "Generate multiple-choice questions and answers from the context :." + context
generated_mcq = generate_mcq(prompt)

print("Generated MCQs:")
print(generated_mcq)
