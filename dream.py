import openai
import random
import requests
import json
import re
import time
from datetime import datetime

sensory_experiences = [    
    "the feeling of a pencil or pen in your hand, as you brainstorm and sketch out ideas on paper",    
    "the sound of typing out a complex command or script in a terminal or command prompt",    
    "the sight of a line-by-line analysis of code, searching for errors or debugging",    
    "the taste of a mint or chewing gum to help you concentrate while solving a problem",    
    "the feeling of a mouse pointer precisely selecting a difficult-to-click button or link",    
    "the sound of the 'ding' or 'ping' when a test case passes or fails",    
    "the sight of a flowchart or decision tree, mapping out the logic of a system",    
    "the taste of a hot cup of tea or coffee to help you stay alert during long debugging sessions",    
    "the feeling of a crisp and responsive keyboard, as you enter complex commands or code snippets",    
    "the sound of a colleague or teammate describing a problem, as you listen and offer suggestions",    
    "the sight of a long log file, as you scroll through looking for relevant error messages",    
    "the taste of a nutritious snack to keep your energy levels up during long troubleshooting sessions",    
    "the feeling of a touchscreen as you navigate complex system settings or parameters",    
    "the sound of a colleague's praise or recognition after a particularly challenging problem has been solved",    
    "the sight of a well-organized and documented codebase, making troubleshooting and analysis easier and more efficient"]


scenarios = [
    "Step 1: Observations and Gathering Information",
    "Step 2: Initial Thoughts and Reactions",
    "Step 3: Analysis and Consideration",
    "Step 4: Critical Thinking and Logical Analysis",
    "Step 5: Plan of Action",
    "Step 6: Constructive Criticism and Feedback",
    "Step 7: System Command or Specific Instruction (if applicable)"
]

topics = [
    "Identify the core question or issue that needs to be addressed",
    "Gather all relevant information related to the topic or question",
    "Take note of any important details and context",
    "Consider any underlying assumptions or biases that may affect the analysis",
    "Share personal thoughts and initial impressions about the topic or question",
    "Consider any emotional or personal reactions that may influence the analysis",
    "Provide a detailed and thoughtful analysis of the topic or question, considering all relevant angles and perspectives",
    "Use reasoning to analyze the information and draw conclusions",
    "Identify evidence that supports the opinion",
    "Consider counterarguments or alternative viewpoints that may challenge the analysis",
    "Use critical thinking and logical analysis to evaluate the information at hand and draw well-supported conclusions",
    "Consider any potential biases or fallacies that may affect the analysis",
    "Develop a plan or set of actions to address the inquiry",
    "Explain how to solve the problem or answer the question in a practical and effective way",
    "Consider any potential obstacles or challenges that may arise during implementation",
    "Provide constructive criticism or feedback",
    "Identify potential weaknesses or limitations of the plan",
    "Suggest ways to improve the plan",
    "Consider any unintended consequences or ethical implications of the plan",
    "If relevant, suggest a system command or specific instruction that can be used to accomplish the task at hand",
    "Provide a clear and detailed explanation of any relevant system commands or tools that can help to execute the plan",
    "Consider any potential technical limitations or risks associated with the use of the system command or tool"
]
def generate_dream_sequence(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.75,
    )

    generated_text = response.choices[0].text.strip()

    return generated_text
def vague_dream_sequence(dream_sequence):
    words = dream_sequence.split()
    num_words_to_remove = min(len(words) // 5, len(words))
    return fuzzy_dream_sequence(dream_sequence, num_words_to_remove)

def fuzzy_dream_sequence(dream_sequence, num_words_to_remove):
    words = dream_sequence.split()
    
    # Make sure num_words_to_remove isn't greater than the number of words
    num_words_to_remove = min(len(words), num_words_to_remove)
    
    words_to_remove = random.sample(words, num_words_to_remove)

    for word in words_to_remove:
        dream_sequence = re.sub(r'\b' + re.escape(word) + r'\b', '_' * len(word), dream_sequence)

    return dream_sequence



def clear_dream_sequence(dream_sequence):
    return dream_sequence


def upload_dream_sequence_to_ai_memory(dream_sequence, base_url, headers):
    memory_url = f'{base_url}/memory'  # Changed from '/message' to '/memory'
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    memory_object = {
        "Text": "ZIGGY is Sleeping:  " + dream_sequence,
        "StartTime": current_time,
        "SourceApp": "dream_sequence_generator"
    }

    response = requests.post(url=memory_url, headers=headers, json=memory_object)

    if response.status_code != 200:
        print("Error uploading dream sequence:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    openai.api_key = "OPENAIAPIKEY HERE"
    base_url = 'https://api.personal.ai/v1'
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "PERSONALAIAPIKEY HERE"
    }

    while True:
        sensory_experience = random.choice(sensory_experiences)
        scenario = random.choice(scenarios)
        topic = random.choice(topics)
        print("========================================INCOMING NEW DREAM SEQUENCE>>>>>>>>>>>>>>>>>>>")
        prompt_template = (
    "Ziggy is in a dream, where he meets a Wise Mentor. They embark on a journey together to solve a complex problem by engaging in a conversation that follows the Seven-Step Response Method Model (S1-S7). "
    "They encounter a scenario from this list: {} "
    "and decide to discuss a topic from this list: {}. "
    "Throughout their conversation, Ziggy and the Wise Mentor use Natural Language to help Ziggy make decisions based on previous interactions and feedback from users. "
    "The conversation unfolds in as many exchanges as needed to complete the dream, during which the Mentor guides Ziggy through the seven steps: "
    "S1 - Gathering Information, "
    "S2 - Initial Thoughts, "
    "S3 - Analysis and Consideration, "
    "S4 - Critical Thinking, "
    "S5 - Plan of Action, "
    "S6 - Constructive Criticism, and "
    "S7 - System Command (if applicable)."
)

        prompt = prompt_template.format(sensory_experience, scenario, topic)

        dream_sequence = generate_dream_sequence(prompt)

        # Choose a random dream sequence type: vague, fuzzy, or clear
        dream_sequence_types = ['clear', 'vague', 'fuzzy']
        chosen_type = random.choice(dream_sequence_types)

        print("Chosen dream sequence type:", chosen_type)

        if chosen_type == 'vague':
            modified_sequence = vague_dream_sequence(dream_sequence)
            print("Modified sequence (vague):", modified_sequence)
        elif chosen_type == 'fuzzy':
            modified_sequence = fuzzy_dream_sequence(dream_sequence, random.randint(5, 25))
            print("Modified sequence (fuzzy):", modified_sequence)
        elif chosen_type == 'clear':
            modified_sequence = clear_dream_sequence(dream_sequence)
            print("Modified sequence (clear):", modified_sequence)

        print(f"{chosen_type.capitalize()} dream sequence: {modified_sequence}")

        print("<<<<<<<<<<<<<<<<END of NEW DREAM SEQUENCE========================================")

        upload_dream_sequence_to_ai_memory(modified_sequence, base_url, headers)

