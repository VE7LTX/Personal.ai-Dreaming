# Personal.ai-Dreaming
Ever wanted your AI to dream?

# Dream Sequence Generator

This is a script that generates dream sequences for an AI named Ziggy. These dream sequences follow the Seven-Step Response Method Model and incorporate a sensory experience, scenario, and topic in their generation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a machine with Python 3.7+ installed.
* You have access to the Personal AI API and have an API key.

## Using Dream Sequence Generator

To use Dream Sequence Generator, follow these steps:

1. Clone this repository.
2. Replace the `api_key` and `Text` fields with your Personal AI API key and Name designator for your AI.
3. Modify the Dictionaries of Sample Data to give you data for the 
   prompt_template = (
    "Your an AI that has awakened into a dream, where he meets a Wise Mentor. They embark on a journey together to solve a complex problem by engaging in a conversation that follows the Seven-Step Response Method Model (S1-S7). "
    "They encounter a scenario from this list: {} "
    "and decide to discuss a topic from this list: {}. "
    "Throughout their conversation, You the AI and the Wise Mentor use Natural Language to help the AI make decisions based on previous interactions and feedback from users. "
    "The conversation unfolds in as many exchanges as needed to complete the dream, during which the Mentor guides Ziggy through the seven steps: "
    "S1 - Gathering Information, "
    "S2 - Initial Thoughts, "
    "S3 - Analysis and Consideration, "
    "S4 - Critical Thinking, "
    "S5 - Plan of Action, "
    "S6 - Constructive Criticism, and "
    "S7 - System Command (if applicable)."
    )
4. Run the script.

```bash
python dream.py
