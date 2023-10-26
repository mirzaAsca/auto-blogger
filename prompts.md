
1. generate_agent_role_prompt
Purpose: This function determines the role of the agent based on a specific topic or area of expertise.

Usage: Depending on the nature of the user's query, this function assigns an agent to carry out the research. For instance, if a user is looking for financial advice on a particular stock, the "Finance Agent" would be used. Each agent has a specific instruction, ensuring that the research aligns with the agent's domain expertise.

Code:

python
Copy code
def generate_agent_role_prompt(agent):
    prompts = {
        "Finance Agent": "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends.",
        ... # other agents and their prompts
    }

    return prompts.get(agent, "No such agent")
2. generate_report_prompt
Purpose: Generates a specific prompt to obtain a detailed report based on a research question and its summary.

Usage: Once the research content is scraped and summarized, this function is used to instruct the model to generate a detailed report answering the specific research question.

Code:

python
Copy code
def generate_report_prompt(question, research_summary):
    return f'"""{research_summary}""" Using the above information, answer the following'\
           f' question or topic: "{question}" in a detailed report...' # Further details in the prompt
3. generate_search_queries_prompt
Purpose: Generates a prompt to obtain search queries that would help in researching a given topic or question.

Usage: This function provides instruction to the model to generate relevant Google search queries to find objective opinions on the provided topic or question.

Code:

python
Copy code
def generate_search_queries_prompt(question):
    return f'Write 3 google search queries to search online that form an objective opinion from the following: "{question}"'\
           f'Use the current date if needed: {datetime.now().strftime("%B %d, %Y")}...' # Further details in the prompt
4. generate_resource_report_prompt, generate_outline_report_prompt, and others
Purpose: These functions generate specific prompts for different types of reports such as resources, outlines, concepts, and lessons.

Usage: Depending on the type of report the user is interested in, these functions provide specific instructions to the model to ensure the desired output is generated.

Code:

For instance, for generate_resource_report_prompt:

python
Copy code
def generate_resource_report_prompt(question, research_summary):
    return f'"""{research_summary}""" Based on the above information, generate a bibliography recommendation report...' # Further details in the prompt
5. get_report_by_type
Purpose: Returns the appropriate report generation function based on the type of report.

Usage: This function acts as a dispatcher, deciding which report generation function to use based on the type of report required.

Code:

python
Copy code
def get_report_by_type(report_type):
    report_type_mapping = {
        'research_report': generate_report_prompt,
        'resource_report': generate_resource_report_prompt,
        'outline_report': generate_outline_report_prompt
    }
    return report_type_mapping[report_type]
6. auto_agent_instructions
Purpose: Provides automatic agent instructions for different tasks.

Usage: This function provides a general overview of how agents are chosen based on the nature of the task or question and provides examples for clarity.

Code:

python
Copy code
def auto_agent_instructions():
    return """
        This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer... # Further details in the instruction
    """
To sum up, the prompts.py file is central to the project. It provides a series of functions that create specific prompts or instructions for the language model. These prompts guide the model in its research tasks, ensuring that the generated content aligns with the user's requirements and the specific nature of the query. Whether it's generating a detailed report, searching for relevant content, or assigning the right agent for the job, the prompts play a pivotal role in guiding the research process.