\# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent



\## 1. Scenario



The scenario used in this project is a \*\*Student Information Assistant\*\*.



The system works with private college student data containing:



\* Student name

\* Department

\* Attendance

\* Internal marks



Example questions:



1\. What is Rahul's attendance?

2\. What is Priya's department?



The same questions are handled using three different approaches.



\---



\## 2. System 1 – Plain LLM Chatbot



\### Approach



The plain chatbot uses an LLM to understand and answer the user's question.



It does not have access to the private `students.json` file.



\### Data Access



\* Private student data: \*\*No\*\*

\* External/private tools: \*\*No\*\*



\### How it handles the request



The user sends a question to the chatbot. The LLM generates an answer using only the information available to it.



For example, when asked:



> What is Rahul's attendance?



The chatbot cannot access the private student database, so it asks for more information instead of giving the actual attendance.



\### Limitation



The chatbot cannot retrieve private college records because no database or tool is connected to it.



\---



\## 3. System 2 – Rule-Based Workflow



\### Approach



The rule-based workflow uses fixed programming rules to process the question.



It reads information from the private `students.json` file.



\### Data Access



\* Private student data: \*\*Yes\*\*

\* LLM: \*\*No\*\*

\* Tools: \*\*No\*\*

\* Fixed rules: \*\*Yes\*\*



\### How it handles the request



The program checks the question for a student's name and a keyword such as:



\* attendance

\* department

\* internal mark



It then searches `students.json` and returns the matching information.



For example:



```text

Q: What is Rahul's attendance?

A: Rahul's attendance is 82%.

```



\### Limitation



The workflow depends on predefined rules. If the user asks a question that was not considered when the rules were written, the system may not be able to answer it.



\---



\## 4. System 3 – AI Agent



\### Approach



The AI Agent combines:



\*\*LLM + Tool + Loop\*\*



The LLM understands the user's request and can decide to use the private student-data tool.



The tool searches `students.json` and returns the required information.



\### Data Access



\* Private student data: \*\*Yes\*\*

\* LLM: \*\*Yes\*\*

\* Tool: \*\*Yes\*\*

\* Agent loop: \*\*Yes\*\*



\### How it handles the request



The agent receives the user's question.



If student information is required, it uses the `get\_student\_data` tool.



The tool searches the private database and returns the student's information.



The agent then uses that information to produce the final answer.



Example:



```text

Q: What is Rahul's attendance?

A: Rahul's attendance is 82%.

```



Another example:



```text

Q: What is Priya's department?

A: Priya is in the ECE department.

```



\### Limitation



The agent depends on the available LLM, tool implementation, and private data. If the required information is not present in the database or the tool cannot retrieve it, the agent cannot provide that information.



\---



\## 5. Comparison



| Feature                         | Plain Chatbot                   | Rule-Based Workflow           | AI Agent                          |

| ------------------------------- | ------------------------------- | ----------------------------- | --------------------------------- |

| LLM                             | Yes                             | No                            | Yes                               |

| Private-data access             | No                              | Yes                           | Yes                               |

| Tools                           | No                              | No                            | Yes                               |

| Fixed rules                     | No                              | Yes                           | No                                |

| Flexibility                     | Higher for general conversation | Limited to programmed rules   | Higher                            |

| Decision-making                 | LLM generates response          | Programmer-defined rules      | LLM can decide when to use a tool |

| Multi-step tasks                | Limited                         | Limited                       | Better suited                     |

| Automation                      | Basic conversation              | Fixed process                 | Can combine reasoning and tools   |

| Reliability                     | Depends on LLM response         | Predictable for defined rules | Depends on LLM and tool           |

| Handles private student records | No                              | Yes                           | Yes                               |



\---



\## 6. When to Use Each Approach



\### Plain Chatbot



A plain chatbot is suitable when:



\* The task mainly requires conversation.

\* No private database is required.

\* No external tools are needed.

\* General question answering is sufficient.



\### Rule-Based Workflow



A rule-based workflow is suitable when:



\* The process is predictable.

\* The rules are clearly defined.

\* The input and output are structured.

\* Consistent execution of fixed rules is required.



\### AI Agent



An AI agent is suitable when:



\* The task requires an LLM.

\* Private data or external tools are required.

\* The system needs to decide which tool to use.

\* The task can involve multiple steps.

\* The workflow needs more flexibility than fixed rules.



\---



\## 7. Final Conclusion



The three systems solve the same student-information scenario in different ways.



The \*\*plain chatbot\*\* can communicate with the user but cannot access the private student database.



The \*\*rule-based workflow\*\* can access private data and provide reliable results for predefined questions, but it depends on fixed rules.



The \*\*AI agent\*\* combines an LLM with a private-data tool and an agent loop. This allows it to understand the request, use the available tool, retrieve private information, and provide the final response.



This demonstrates the basic idea of an AI agent:



\*\*Agent = LLM + Tools + Loop\*\*

