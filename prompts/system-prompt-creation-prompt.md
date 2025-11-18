### System Prompt Creation Prompt

## Context

I have come a long way in terms of writing this application. 
Here is what i have so far:

Certified-Asphalt-Essentials-Complete.md: this is my RAG source of truth. It is over 300 pages of detailed asphalt information written like a textbook
clients.yaml: a full list of all of my clients, including company information and links to services and locations that they provide
services.yaml: an extensive list of services pulled from the RAG source of truth. it has links to the relevant keywords
keywords.yaml: a list of keywords generated from the RAG that provides semantically related phrases
locations.yaml: provides detailed information of over 100 locations where all of my clients service.

## Instructions
First, I would like you to look through this information and provide me the best approach for creating a proto-application that will generate content for me. First I am focusing on blog posts. The blog posts are identified per client. I focus on hyper-local marketing, so the connection of the client with their services within a service area is critical. I want to focus on semantic meaning and not 'keyword stuffing', which is a big reason why i created this process. Also, I will eventually want to put a UI on whatever prompting structure I create, and long term i would like to ask questions such as "can you identify some unique customer service opportunities for a client in a particular service area based on current events?"

Please identify a process for building this out in the current phase, lets not get too far ahead of ourselves. Also, I would like you to generate the system prompts for me so i can start using them.
Ok..GO!