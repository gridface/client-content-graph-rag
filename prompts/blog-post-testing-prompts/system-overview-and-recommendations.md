# Blog Content Generation System Prompts
## Hyper-Local Asphalt Contractor Content System

---

## Table of Contents
1. [System Overview](#system-overview)
2. [Core Prompt: Educational Blog Generator](#educational-blog-generator)
3. [User Prompt Template](#user-prompt-template)
4. [Quality Control Checklist](#quality-control-checklist)

---

## System Overview

### Architecture
This content generation system leverages:
- **RAG Knowledge Base**: 618k character comprehensive asphalt textbook (300+ pages)
- **Client Database**: 6+ asphalt contractors with service/location mappings
- **Service Catalog**: 50+ detailed service definitions with technical specifications
- **Keyword Library**: Semantic clusters with search intent and variations
- **Location Database**: 100+ locations with climate, economic, and demographic data

### Content Generation Flow
1. **Input Phase**: User specifies client, location(s), service(s), content type
2. **Context Building**: System retrieves and merges all relevant data
3. **Content Structuring**: Generate outline based on content type template
4. **Generation Phase**: Create draft with technical accuracy and local relevance
5. **Optimization Phase**: Verify accuracy, local specificity, and semantic variety

---






---


---

## Implementation Notes

### Phase 1: Current Phase (Blog Generation)
Focus on:
- Educational blog posts that rank and establish authority
- Service pages that convert local traffic
- Seasonal campaigns that create urgency
- FAQ content that addresses customer questions

### Phase 2: Future Enhancement
Consider developing:
- Competitive analysis content
- Local event tie-in posts
- Customer success story templates
- Community involvement content
- Video script templates
- Social media post variants

### Phase 3: Advanced Features
For UI implementation, enable:
- Client selection dropdown
- Multi-location selection
- Service combination options
- Content type templates
- Seasonal calendar integration
- Batch generation capabilities

### Future Vision: Opportunity Identification
Develop prompts for:
- "What local events in [location] could [client] sponsor or participate in?"
- "What seasonal opportunities exist for [client] in [location] this month?"
- "What local business partnerships make sense for [client] in [service area]?"
- "What unique content angles exist for [service] in [location] based on current events?"

---

## Example Usage Workflow

1. **Select Client**: Choose from clients.yaml
2. **Select Location(s)**: Choose target cities from client's service area
3. **Select Service(s)**: Choose from client's active services
4. **Choose Content Type**: Educational, service page, seasonal, or FAQ
5. **System Assembles Context**: Automatically pulls all relevant data
6. **Generate Content**: System creates first draft
7. **Review & Edit**: Apply quality checklist
8. **Publish**: Deploy to client website/blog

---

## Maintenance and Updates

### Regular Updates Needed:
- Add new seasonal angles quarterly
- Update location data with current events
- Refresh technical content from RAG as industry evolves
- Add new service types as clients expand
- Update keyword data based on search trends
- Refine prompts based on performance data

### Performance Tracking:
- Monitor ranking for target keywords
- Track organic traffic to generated content
- Measure conversion rates from blog to contact
- Gather client feedback on content quality
- A/B test different angles and structures

---

**Document Version**: 1.0  
**Created**: November 2025  
**Purpose**: System prompts for hyper-local asphalt contractor blog content generation
