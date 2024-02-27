from typing import Dict

MISTRALAI_MODELS: Dict[str, int] = {
    "open-mistral-7b": 8000,
    "open-mixtral-8x7B": 32000, # This endpoint is currently returning a Status 400 But should work according to their documentation.
    "mistral-small-2312": 32000, # This is an allia for open-mixtral-8x7B
    "mistral-small-latest": 32000,
    "mistral-medium-latest": 32000,
    "mistral-large-latest": 32000,
}

# Mistral AI Changes 2-26-2024 provides five API endpoints:

# open-mistral-7b (aka mistral-tiny-2312) - The endpoint mistral-tiny will be deprecated in May 2024.
# open-mixtral-8x7b (aka mistral-small-2312) - (Note: This endpoint is currently returning Status: 400.) The endpoint mistral-small will be deprecated in May 2024.
# mistral-small-latest (aka mistral-small-2402) - new model
# mistral-medium-latest (aka mistral-medium-2312) - The previous mistral-medium has been dated and tagged as mistral-medium-2312. The endpoint mistral-medium will be deprecated in May 2024.
# mistral-large-latest (aka mistral-large-2402) - New Flagship model


def mistralai_modelname_to_contextsize(modelname: str) -> int:
    if modelname not in MISTRALAI_MODELS:
        raise ValueError(
            f"Unknown model: {modelname}. Please provide a valid MistralAI model name."
            "Known models are: " + ", ".join(MISTRALAI_MODELS.keys())
        )

    return MISTRALAI_MODELS[modelname]
