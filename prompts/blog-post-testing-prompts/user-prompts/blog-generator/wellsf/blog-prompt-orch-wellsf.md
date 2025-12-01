# Blog Content Generation Orchestrator
## Hyper-Local Asphalt Contractor Content System

---

## System Overview

There are three files I have attached for you to create a blog post for my client. i will list each out here at the top then describe them in detail further down. lastly i will provide the instruction flow showing how to use these files to create the Blog post output.

1. Source of truth file: this is the the attached markdown file has a naming pattern of 'blogger-wells-fl-" as a prefix followed by a number that corresponds to a blog number system i have determined elsewhere. For instance, 'blogger-wells-fl-1.md','blogger-wells-fl-2.md', etc
2. educational blog generator: educational-blog-generator.md
3. quality control checklist: quality-control-checklist.md

### Source of Truth:
the attached markdown file has a naming pattern of 'blogger-wells-fl-" as a prefix followed by a number that corresponds to a blog number system i have determined elsewhere. For instance, 'blogger-wells-fl-1.md','blogger-wells-fl-2.md', etc

Inside this file there are several items that determine title, description, and data source of truth for the blog that needs to be generated. 

The first part of the file describes the blog at a high level, including the target keywords, locations, and topic angles we are going for.

The second part of the file is in yaml structure within the markdown headers. these yaml snippets were taken from a larger database. this includes:
- customer information
- location information
- service information

The final section is titled RAG Infomation and it constitutes the bulk of this document. It represents the specific chapters of a book that i use as my source of truth for my blogs, and these cut-and-paste chapters are representative of the information i need to reference for this blog. 

The reason for this file is that i am trying to save on tokens and be very specific about the information i provide you instead of giving you an entire textbook and yaml database structure to parse out.


### Content Generation Prompts:
These next two prompt files provided will 
- **educational-blog-generator.md**: This provides a description of your role, voice, and detailed instructions for writing the blog. It assumes that you are taking input variables from the user-prompt, and only use the sources of truth for technical asphalt details, services offered, and client specifics. Location flavor uses the location data as a guideline for what kind of information we are looking for, that is, information that is of interest to asphalt customers and contractors in regards to asphalt paving services
- **quality-control-checklist.md**: this provides detailed instructions for a professional reviewer agent to read through the blog and make sure it passes our rigourous content guildelines.


### Instruction Flow
1. **follow the educational-blog-generator**: this is your core instruction set for blog writing. The source of truth file will provide you with the specific variables that you will need to create this blog. Utilize sources of truth documents for informational content. 
2. **generate first draft**: generate a first draft of this document and append -draft to the end of the file
3. **quality check Phase**: Verify accuracy, local specificity, and semantic variety.
4. **generate quality checked blog**: if you needed to make any changes in step 3, provide a fresh copy of the blog with -fixed appened to the end, and at the top of the file i want you to list out all the changes you made and why so i can compare the two versions and evaluate your reasoning.


```




