# Complete Content Bundle Orchestrator
## Blog + GMB + Facebook + Media Recommendations

---

## System Overview

This orchestrator produces a complete content bundle for each topic: educational blog, Google My Business update, Facebook post, and media recommendations for all three platforms.

**Content Calendar Cadence:** Every 3 days
- Blog Post (1,200-2,000 words)
- GMB Update (150-300 words)  
- Facebook Post (80-150 words)
- 9 Media Recommendations (3 per platform)

---

## Sources of Truth

| Source | Purpose |
|--------|---------|
| `Certified-Asphalt-Essentials-Complete.md` | Technical RAG knowledge base |
| `clients.yaml` | Client profiles, credentials, service areas |
| `services.yaml` | Service definitions, keywords, categories |
| `locations.yaml` | Location data, climate zones, local challenges |
| `blog-topics-database.yaml` | 600 pre-planned topics with RAG section mappings |

---

## Prompt Files

| File | Purpose |
|------|---------|
| `educational-blog-generator.md` | Blog writing instructions, voice, structure |
| `quality-control-checklist.md` | Blog quality verification |
| `sister-content-generator.md` | GMB, Facebook, and Media generation |

---

## User Prompt Template

When requesting a content bundle, provide:

```
GENERATE: Content Bundle

CLIENT_PROFILE:
- Name: [Client Name from clients.yaml]
- Client ID: [client-id]

TOPIC:
- Topic ID: [topic-id from blog-topics-database.yaml]
- Title: [Topic title]
- Topic Angle: [From database]

LOCATION_CONTEXT:
- Target Locations: [loc-ids from topic]

SERVICE_DETAILS:
- Services: [service names from topic]

KEYWORD_DATA:
- Primary Keywords: [from topic]
- Search Intent: [informational/commercial/transactional]

RAG_SECTIONS:
- Include: [rag_sections from topic - comma separated]

NOTES:
- [Any special instructions or emphasis]
```

---

## Instruction Flow

### PHASE 1: BLOG GENERATION

**Step 1.1 - Draft Creation**
- Follow `educational-blog-generator.md` specifications
- Pull relevant content from RAG sections specified
- Pull location data from `locations.yaml`
- Pull client credentials from `clients.yaml`
- Generate blog draft

**Step 1.2 - Quality Check**
- Apply `quality-control-checklist.md`
- Verify technical accuracy against RAG source
- Confirm minimum 5 local references
- Check semantic keyword distribution
- Validate structure and formatting

**Step 1.3 - Finalize Blog**
- If changes needed: generate corrected version with change log
- Output: `blog-[client-id]-[topic-id]-final.md`

---

### PHASE 2: SISTER CONTENT GENERATION

**Step 2.1 - GMB Update**
Using finalized blog as reference:
- Extract ONE key educational takeaway
- Apply `sister-content-generator.md` GMB specifications
- Include location in first sentence
- Add phone number and CTA
- Output: GMB update (150-300 words)

**Step 2.2 - Facebook Post**
Using finalized blog as reference:
- Create scroll-stopping opener
- Distill insight into conversational format
- Add engagement prompt
- Apply `sister-content-generator.md` Facebook specifications
- Output: Facebook post (80-150 words)

**Step 2.3 - Media Recommendations**
For all three platforms:
- Generate 3 specific media recommendations per platform
- Include shot descriptions, local elements, alt text
- Identify cross-platform hero image
- Apply `sister-content-generator.md` Media specifications
- Output: 9 media recommendations with notes

---

### PHASE 3: SISTER CONTENT QUALITY CHECK

**Step 3.1 - Individual Verification**
- [ ] GMB meets all checklist items
- [ ] Facebook meets all checklist items  
- [ ] Media recommendations are specific and actionable

**Step 3.2 - Cohesion Check**
- [ ] All pieces clearly relate to same topic
- [ ] No contradicting information
- [ ] Progressive depth: FB (teaser) → GMB (insight) → Blog (comprehensive)
- [ ] CTAs complement each other
- [ ] Brand voice consistent

---

### PHASE 4: FINAL DELIVERABLES

**Option A: Combined Bundle**
Single file with all content sections:
```
content-bundle-[client-id]-[topic-id].md
```

**Option B: Separate Files**
```
blog-[client-id]-[topic-id]-final.md
gmb-[client-id]-[topic-id].md
facebook-[client-id]-[topic-id].md
media-[client-id]-[topic-id].md
```

---

## Output Template

```markdown
# CONTENT BUNDLE: [topic-id]
## [Topic Title]
### Client: [Client Name] | Location: [Primary Location] | Date: [Date]

---

# SECTION 1: EDUCATIONAL BLOG

## SEO Title
[Under 60 characters]

## Meta Description
[Under 155 characters]

## H1 Heading
[SEO-optimized heading]

## Blog Content
[Full 1,200-2,000 word blog following educational-blog-generator.md structure]

---

# SECTION 2: GOOGLE MY BUSINESS UPDATE

**Post Type:** What's New

[150-300 word GMB update]

**CTA Button:** [Learn More / Call Now / Book Online]
**Button Link:** [URL]

---

# SECTION 3: FACEBOOK POST

[80-150 word Facebook post with line breaks]

**Hashtags:** [3-5 hashtags]
**Location Tag:** [City, State]
**Link Placement:** Comments

---

# SECTION 4: MEDIA RECOMMENDATIONS

## Blog Media (3 Recommendations)

### Blog Image 1
- **Type:** [Photo/Video/Infographic/Before-After]
- **Description:** [Specific description]
- **Composition:** [Shot details]
- **Local Element:** [Location identifier]
- **Alt Text:** "[Accessibility text]"

### Blog Image 2
[Same format]

### Blog Image 3
[Same format]

---

## GMB Media (3 Recommendations)

### GMB Image 1 (Primary)
- **Type:** [Photo/Video]
- **Description:** [Specific description - 4:3 or 1:1 format]
- **Composition:** [Shot details]
- **Local Element:** [Location identifier]
- **Alt Text:** "[Accessibility text]"

### GMB Image 2
[Same format]

### GMB Image 3
[Same format]

---

## Facebook Media (3 Recommendations)

### FB Image 1 (Primary)
- **Type:** [Photo/Video/Carousel]
- **Description:** [Specific description - feed optimized]
- **Composition:** [Shot details]
- **Local Element:** [Location identifier]
- **Alt Text:** "[Accessibility text]"

### FB Image 2
[Same format]

### FB Image 3
[Same format]

---

## Cross-Platform Hero Image
**Recommended Primary:** [Description of the ONE image that works everywhere]
- Blog: [Usage notes]
- GMB: [Crop/usage notes]
- Facebook: [Usage notes]

---

# SECTION 5: PUBLISHING CHECKLIST

## Pre-Publish
- [ ] Blog proofread and formatted
- [ ] GMB post ready in GMB dashboard
- [ ] Facebook post scheduled in scheduler
- [ ] Media sourced/created for all platforms
- [ ] Links tested and working

## Publish Day Schedule
- [ ] 8:00 AM - Blog live on website
- [ ] 9:00 AM - GMB update published
- [ ] 10:00 AM - Facebook post published

## Post-Publish (within 4 hours)
- [ ] Monitor GMB for questions
- [ ] Respond to Facebook comments
- [ ] Share blog link in Facebook comments
- [ ] Check analytics for any issues

---

# SECTION 6: CHANGE LOG (if applicable)

## Blog Revisions
| Change | Reason |
|--------|--------|
| [Description] | [Why change was made] |

## Sister Content Notes
[Any special considerations or variations from standard format]

---
```

---

## Quick Reference: Character Limits

| Platform | Limit | Optimal |
|----------|-------|---------|
| Blog SEO Title | 60 chars | 50-60 chars |
| Blog Meta Description | 155 chars | 145-155 chars |
| Blog Word Count | - | 1,200-2,000 words |
| GMB Post | 1,500 chars | 700-1,000 chars |
| GMB (visible preview) | ~100 chars | Front-load key info |
| Facebook Post | 63,206 chars | 400-700 chars (80-150 words) |
| Facebook (before truncation) | ~477 chars | Keep hook above fold |

---

## Quick Reference: Platform Priorities

| Element | Blog | GMB | Facebook |
|---------|------|-----|----------|
| Primary Goal | Educate + SEO | Local Authority + Action | Engage + Awareness |
| Tone | Professional-Educational | Professional-Direct | Conversational-Friendly |
| CTA Strength | Strong | Strong | Soft |
| Local Mentions | 5+ | 2-3 | 1-2 |
| Technical Depth | High | Medium | Low |
| Emoji Use | None | 1-2 max | 2-4 acceptable |
| Hashtags | None | None | 3-5 optional |
| Link | Inline | Button + text | Comments |

---

## Efficiency Tips

1. **Batch Processing:** Generate all content for a week (2-3 bundles) in one session to maintain consistency.

2. **Media Library Building:** Track media recommendations across bundles to identify recurring needs. Build a library of:
   - Before/after shots by service type
   - Team photos at various locations
   - Equipment in action shots
   - Completed project galleries by location

3. **Template Reuse:** For recurring content types (seasonal, service-specific), create sub-templates to speed generation.

4. **Quality Shortcuts:** Once the system is proven, the quality check phase can be streamlined for familiar content types.

5. **Cross-Client Learning:** Media recommendations for one client in a region may apply to other clients in similar climates/markets.

