""" Provides a function to generate responses from a language model using the Groq API.

The main functionality is provided by the `groq_it()` function, which:
    1. Takes a user message (`content`) and an optional `model` parameter as input.
    2. Creates a Groq client instance using the `GROQ_API_KEY` environment variable.
    3. Sends a request to the Groq API to generate a response to the user message using
        the specified model.
    4. Returns the generated response from the model.

The function uses the `Groq` class from the `groq` library to create a client instance 
and the `ChatCompletion` class from `groq.types.chat.chat_completion` to handle the 
API response.

The `model` parameter allows you to specify the desired language model to use for 
generating the response. It defaults to "llama3-70b-8192", but you can provide any 
valid model name from the available models listed in the Groq documentation.

If the Groq API request fails, the function raises an exception with the error details.

To use this module, ensure that the required dependencies are installed and that the 
`GROQ_API_KEY` environment variable is set with your Groq API key. Then, you can call 
the `groq_it()` function with a user message and optionally specify the desired model 
to generate a response.

Example usage:
```python
content = "Why is the sky blue?"
reply = groq_it(content)  # Default model is llama3-70b-8192
print(reply)
```

This will send the user message "Why is the sky blue?" to the default model and print 
the generated response.
"""

from groq import Groq
from groq.types.chat.chat_completion import ChatCompletion

client = Groq()  # Requires GROQ_API_KEY in environment variables.


def groq_it(content: str, model: str = "llama3-70b-8192") -> str:
    """Use Groq to generate a response to a user message from the selected model.

    Args:
        content: The user message to ask the model.
        model: A valid model name. Defaults to "llama3-70b-8192". See available models:
            https://console.groq.com/docs/models

    Returns:
        The model response to the user message.

    Raises:
        Exception: If the Groq API request fails.

    Example usage:
        content = "Why is the sky blue?"
        reply = groq_it(content)  # Default model is llama3-70b-8192
        print(reply)
    """
    try:
        response: ChatCompletion = client.chat.completions.create(
            messages=[{"role": "user", "content": content}],
            model=model,
        )
    except Exception as e:
        raise e

    if not response.choices:
        return ""
    return response.choices[0].message.content
