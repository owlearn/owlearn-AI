def refine_image_prompt(raw_prompt: str) -> str:
    return (
        f"A detailed illustration of the scene: \"{raw_prompt}\". "
        f"Children's book style, warm atmosphere"
    )


def generate_final_image_prompts(raw_prompts: list[str]) -> list[str]:
    return [refine_image_prompt(p) for p in raw_prompts]
