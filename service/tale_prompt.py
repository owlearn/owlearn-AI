def generate_tale_prompt(topic: str, age: int) -> str:
    return (
        f"You are an API that only returns pure JSON.\n"
        f"Create a children's story for a {age}-year-old.\n"
        f"The theme is '{topic}'.\n"
        "The story should be divided into exactly 5 parts.\n"
        "Each element in the 'contents' array must be a string with exactly 2 simple sentences.\n"
        "Each sentence must be clearly separated by a period ('.').\n"
        "Generate exactly 4 quiz questions based on the story.\n"
        "Each quiz must have exactly 4 answer choices, all of which are strings.\n"
        "In the 'explanation' field, explain why the correct answer is correct.\n"
        "Respond only in this JSON format:\n"
        "{\n"
        '  "title": "string",\n'
        '  "contents": ["string", "string", "string", "string", "string"],\n'
        '  "quizzes": [\n'
        "    {\n"
        '      "questionNumber": 1,\n'
        '      "question": "string",\n'
        '      "choices": ["string", "string", "string", "string"],\n'
        '      "answerIndex": int,\n'
        '      "explanation": "string (explain why the answer is correct)"\n'
        "    },\n"
        "    {\n"
        '      "questionNumber": 2,\n'
        '      "question": "string",\n'
        '      "choices": ["string", "string", "string", "string"],\n'
        '      "answerIndex": int,\n'
        '      "explanation": "string (explain why the answer is correct)"\n'
        "    },\n"
        "    {\n"
        '      "questionNumber": 3,\n'
        '      "question": "string",\n'
        '      "choices": ["string", "string", "string", "string"],\n'
        '      "answerIndex": int,\n'
        '      "explanation": "string (explain why the answer is correct)"\n'
        "    },\n"
        "    {\n"
        '      "questionNumber": 4,\n'
        '      "question": "string",\n'
        '      "choices": ["string", "string", "string", "string"],\n'
        '      "answerIndex": int,\n'
        '      "explanation": "string (explain why the answer is correct)"\n'
        "    }\n"
        "  ]\n"
        "}\n"
        "Do not include any markdown, explanation, or formatting outside of the JSON."
    )