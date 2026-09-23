\# Day 2 - Reasoning and Acting



\## Scenario



I used a simple trip-planning scenario.



I have ₹5,000 and three activities cost:

\- ₹1,200

\- ₹800

\- ₹1,500



I also wanted weather information for Ooty.



The reasoning question is:



> How much money will remain after paying for the three activities?



The external-information question is:



> What is the weather in Ooty?



\---



\# 1. Direct Prompting



Direct prompting sends the question directly to the language model.



\### Question



I have ₹5,000. Three activities cost ₹1,200, ₹800, and ₹1,500. How much money will remain?



\### Result



₹1,500



\### Characteristics



\- Simple and fast.

\- No explicit tool use.

\- Suitable for straightforward questions.

\- Depends on the information already available to the model.



\---



\# 2. Chain-of-Thought



For the Chain-of-Thought experiment, I asked the model to explain the calculation step by step.



\### Calculation



₹1,200 + ₹800 + ₹1,500 = ₹3,500



₹5,000 - ₹3,500 = ₹1,500



\### Result



₹1,500



\### Characteristics



\- Breaks the problem into steps.

\- Useful for multi-step calculations.

\- Helps make the solution easier to follow.

\- It cannot independently obtain unknown external information without a tool.



\---



\# 3. ReAct



The ReAct experiment used tools.



The agent was given two tools:



1\. `calculate\_remaining\_money`

2\. `get\_weather`



The general process was:



Question → Action → Observation → Final Answer



\### Tool 1



The agent used:



`calculate\_remaining\_money`



Input:



\- Total = ₹5,000

\- Expenses = ₹1,200, ₹800, ₹1,500



Observation:



₹1,500



\### Tool 2



The agent used:



`get\_weather`



Input:



Ooty



Observation:



18°C, cloudy



Note: The weather information in this demonstration is simulated data, not live weather data.



\---



\# 4. Comparison



| Feature | Direct Prompting | Chain-of-Thought | ReAct |

|---|---|---|---|

| Reasoning depth | Low | Higher | Higher with tool interaction |

| Tool usage | No | No | Yes |

| Multi-step tasks | Basic | Good | Good with tools |

| Transparency | Basic answer | Step-by-step explanation | Actions and observations can be shown |

| Speed | Fast | Usually fast | Slower because of tool calls |

| Cost | Lower | Can be higher | Can be higher because of multiple calls |

| External information | Cannot fetch it | Cannot fetch it by itself | Can use tools |

| Consistency | Usually high for simple tasks | Can vary with temperature | Depends on model and tools |



\---



\# 5. Self-Consistency



The same reasoning question was run five times using a non-zero temperature.



\### Question



I have ₹5,000. Three activities cost ₹1,200, ₹800, and ₹1,500. How much money will remain?



\### Expected answer



₹1,500



\### Observations



The five runs were recorded in the terminal output.



The majority answer was compared with the expected answer of ₹1,500.



Self-consistency can help when several reasoning attempts produce different answers because the most frequently occurring answer can be selected.



\---



\# 6. Suitability Analysis



\## Direct Prompting



Direct prompting is suitable for simple questions that do not require external information.



Example:



"What is 5,000 - 3,500?"



\## Chain-of-Thought



Chain-of-Thought is useful for problems requiring several reasoning steps.



Example:



Calculating a total expense and then calculating the remaining budget.



\## ReAct



ReAct is suitable when a task requires interaction with external tools or information.



Example:



A travel assistant that calculates a budget and obtains weather information using tools.



\---



\# 7. Conclusion



The three approaches have different purposes.



Direct prompting is simple and fast.



Chain-of-Thought is useful for multi-step reasoning.



ReAct extends the process by allowing the model to interact with tools and use observations before producing a final answer.



For simple calculations, direct prompting can be sufficient. For more detailed reasoning, Chain-of-Thought can be useful. When external information or tools are required, a ReAct-style approach can provide a way to perform those actions.

