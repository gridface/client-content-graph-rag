## User Prompt Template

When using these system prompts, structure your user input like this:

```
GENERATE: [Content Type - Educational Blog / Service Page / Seasonal / FAQ]

CLIENT_PROFILE:
- Name: [Client Name]
- Location: [Main Office City, State]
- Years in Business: [Number]
- Specialties: [Key Differentiators]
- Service Area: [Cities Served]
- Website: [URL]
- Phone: [Contact Number]

LOCATION_CONTEXT:
- Target Location: [City, State]
- Climate Zone: [humid_continental / humid_subtropical / etc]
- Population: [Number]
- Economic Profile: [Key Industries / Demographics]
- Local Challenges: [freeze_thaw / coastal / hurricane / etc]
- Flavor Notes: [Unique characteristics from locations.yaml]
- Nearby Areas: [Neighboring Cities]

SERVICE_DETAILS:
- Service ID: [srv-xxx-xxx]
- Service Name: [Full Name]
- Service Type: [residential / commercial / municipal]
- Description: [From services.yaml]
- Seasonal Considerations: [From services.yaml]
- Equipment Required: [From services.yaml]
- Typical Duration: [From services.yaml]

KEYWORD_DATA:
- Primary Keyword: [Main keyword]
- Semantic Equivalents: [List from keywords.yaml]
- Long-tail Variations: [List from keywords.yaml]
- Search Intent: [transactional / informational / navigational]

RAG_TECHNICAL_CONTENT:
[Paste relevant sections from Certified-Asphalt-Essentials-Complete.md]
- Focus on sections relevant to this service
- Include technical specifications
- Include process details
- Include quality standards

CONTENT_ANGLE (if applicable):
[For seasonal: Spring Preparation / Summer Opportunity / Fall Prevention / Winter Planning]
[For educational: How-to / Comparison / Buyer's Guide / Technical Explanation]

SPECIAL INSTRUCTIONS (optional):
[Any specific requirements, focus areas, or constraints]
```