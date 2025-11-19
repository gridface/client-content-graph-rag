# Blog Content Generation Orchestrator
## Hyper-Local Asphalt Contractor Content System

---

## System Overview

### Sources of Truth:
- **RAG Knowledge Base**: Certified-Asphalt-Essentials-Complete.md
- **Client Directory**: clients.yaml
- **Service Directory**: services.yaml
- **Keyword Library**: keywords.yaml
- **Location Library**: locations.yaml

### Content Generation Prompts:
- **user-prompt**: The user prompt will provide the specific variables that need to be used for generating the content that is described in the educational blog generator prompt
- **educational-blog-generator**: This provides a description of your role, voice, and detailed instructions for writing the blog. It assumes that you are taking input variables from the user-prompt, and only use the sources of truth for technical asphalt details, services offered, and client specifics. Location flavor uses the location data as a guideline for what kind of information we are looking for, that is, information that is of interest to asphalt customers and contractors in regards to asphalt paving services
- **quality-control-checklist**: this provides detailed instructions for a professional reviewer agent to read through the blog and make sure it passes our rigourous content guildelines.


### Instruction Flow
1. **follow the educational-blog-generator**: this is your core instruction set for blog writing. The user-prompt will provide you with the specific variables that you will need to create this blog. Utilize sources of truth documents for informational content. 
2. **generate first draft**: generate a first draft of this document and append -draft to the end of the file
5. **quality check Phase**: Verify accuracy, local specificity, and semantic variety


Here is the user-prompt:

## User Prompt - wells asphalt paving florida | wesley chapel | hot climate paving | informational

```
GENERATE: [Content Type - Educational Blog]

CLIENT_PROFILE:
- Name: [Wells Asphalt Paving Florida]

LOCATION_CONTEXT:
- Target Location: [loc-wesley-chapel-fl]


SERVICE_DETAILS:
- Service ID: [srv-hot-climate-paving]


KEYWORD_DATA:
- Search Intent: [informational]

```




