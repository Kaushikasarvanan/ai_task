\# Day 3 - From Prompt to Action



\## 1. Scenario



My chosen scenario is calculating the total cost of shopping items.



The question used in the experiment is:



"What is the total cost of 3 apples at ₹20 each and 2 notebooks at ₹50 each?"



The calculation is:



3 × 20 + 2 × 50 = ₹160.



This scenario is useful because a language model can answer general questions such as what Python is or what an AI agent is from its learned knowledge. However, a calculation can be handled more reliably by giving the model access to a calculation tool.



\## 2. What is a Large Language Model?



A Large Language Model (LLM) is an AI model trained on a large amount of text. It can understand questions and generate human-like answers.



For example, in my scenario, the LLM can answer "What is Python?" because this is general knowledge.



However, a plain LLM does not automatically have access to an external calculator or live information. It generates an answer from what it has learned and the information given in the prompt. Therefore, for calculations or information that needs an external operation, using a tool can make the result more reliable.



\## 3. What is an Agent?



An AI agent is an LLM-based system that can decide what action is needed to complete a task and can use external tools when required.



A plain chat response directly generates an answer.



An agent can follow a process such as:



User question → decide whether a tool is needed → call the tool → receive the result → generate the final answer.



In my scenario, the tool-enabled program recognises that a calculation is required and calls the calculation tool before giving the final answer.



\## 4. What is a Tool and Tool Call?



A tool is an external function that an LLM can use to perform an operation that it cannot reliably perform by generating text alone.



In my scenario, the tool is the `calculate\_total()` function.



A tool call means requesting that tool to perform its operation.



The tool has a name, description and parameters. These tell the model what the tool does and what information it needs.



For example, my tool receives a list of prices:



`calculate\_total(prices)`



The model needs this information so that it can decide when the tool is appropriate and provide the correct input.



\## 5. Flow of One Tool Call



The tool call in my scenario follows these steps:



1\. The user asks for the total cost.

2\. The model identifies that a calculation is required.

3\. The model decides that the calculation tool should be used.

4\. The tool is called with the prices.

5\. The tool calculates the total.

6\. The result is returned to the model.

7\. The model uses the tool result.

8\. The final answer is given to the user.



The flow is:



User Question

→ LLM

→ Tool Decision

→ Tool Call

→ Tool Result

→ LLM

→ Final Answer



\## 6. Why Should a Tool Return Plain Text?



A tool should return its result as plain text even when something goes wrong because the model can then understand the result and respond appropriately.



If the tool always stops the program by raising an error, the complete agent workflow may stop.



Returning text allows the model to receive the result and continue the conversation.



\## 7. Comparison Table



| Basis | Plain LLM Prompt | LLM with One Tool |

|---|---|---|

| Source of the answer | LLM's learned knowledge and prompt | LLM plus external tool result |

| Can it fetch or compute outside its memory? | No external tool access | Yes, through the available tool |

| Reliability on factual or numeric questions | Can be less reliable for calculations or changing information | More reliable when the tool performs the required operation |

| Transparency | The answer is generated directly | The tool call and result can be observed |

| Speed / cost | Usually simpler and faster | Adds a tool execution step |



\## 8. Observations



I tested three questions.



\### Question 1



"What is Python?"



The plain LLM can answer this question because it is general knowledge.



The tool-enabled system does not need the calculation tool because no external calculation is required.



\### Question 2



"What is an AI agent?"



The plain LLM can answer this because it is a conceptual question.



The tool is not necessary.



\### Question 3



"What is the total cost of 3 apples at ₹20 each and 2 notebooks at ₹50 each?"



This question requires a calculation.



The tool-enabled run calls `calculate\_total()` with the required prices.



The tool returns:



`Total cost is ₹160`



The final answer uses this tool result.



\## 9. Suitability



A plain LLM prompt is suitable when the question can be answered from the model's learned knowledge and does not require external information or an external operation.



Examples include simple definitions and explanations.



A tool becomes useful when the question requires a calculation, current information, database lookup, file access, or another operation outside the model's normal text generation.



In my scenario, the general questions did not require the tool, while the shopping total could be handled more reliably using the calculation tool.



\## 10. Conclusion



This experiment shows the difference between a plain LLM and an LLM with a tool.



A plain LLM generates an answer directly from its learned knowledge and the prompt.



An agent can decide when an external operation is required, call a tool, receive the result, and then use that result to produce the final answer.



Therefore, tools extend the practical capabilities of an LLM. A plain prompt is sufficient for many general questions, while tools are useful when reliable calculations, external information, or other operations are required.

