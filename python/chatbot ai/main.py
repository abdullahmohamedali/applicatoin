import bardapi

def make_google_bard():
  """Returns a Bard object."""

  # Set the API key.
  api_key = "bQgL8At4FOQJeS9NUMyxJ853L_ASKXziKeXnGbfdt_E9noGk3wIjY6maN_WYIA_57FjDzg."

  # Create a Bard object.
  bard = bardapi.Bard(google_translator_api_key=api_key)

  return bard

# Get the Bard object.
bard = make_google_bard()

# Generate text.
generated_text = bard.get_answer(prompt="What is the meaning of life?")

# Print the generated text.
print(generated_text)