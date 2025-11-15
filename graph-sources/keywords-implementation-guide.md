# Keywords.yaml Implementation Guide

## Overview
Your comprehensive keywords.yaml file contains **65+ primary keyword clusters** covering all aspects of asphalt paving services. Each keyword is fully populated with semantic equivalents, long-tail variations, and metadata for SEO optimization.

## File Statistics

- **Total Primary Keywords**: 65+
- **Semantic Equivalents per Keyword**: 4-7 average
- **Long-Tail Variations per Keyword**: 6-10 average
- **Total Searchable Phrases**: 800+ unique keyword combinations

## Structure Explanation

Each keyword entry follows this format:

```yaml
keyword_id: kw-unique-identifier
primary_keyword: "main search term"
search_intent: transactional/informational/commercial
customer_type: residential/commercial/both
semantic_equivalents: [alternative ways to search for the same thing]
related_terms: [closely related concepts]
long_tail_variations: [specific, longer search phrases]
search_volume_tier: high/medium/low
conversion_potential: very-high/high/medium/low
content_topics: [content themes to address this keyword]
technical_level: basic/intermediate/advanced
```

## Keyword Categories Included

### Core Paving Services (5 keywords)
- Asphalt paving
- Paving contractor
- Sealcoating
- Asphalt driveway
- Parking lot paving

### Repair & Maintenance (6 keywords)
- Crack filling
- Pothole repair
- Asphalt repair
- Patching
- Asphalt resurfacing
- Mill and overlay

### Specialty Services (5 keywords)
- Chip seal
- Grading and excavation
- Base work
- Porous asphalt
- Recycled asphalt

### Project Types (5 keywords)
- Residential paving
- Commercial paving
- New paving
- Driveway paving
- Parking lot

### Maintenance Activities (4 keywords)
- Preventative maintenance
- Sealcoating and crack sealing
- Pavement marking
- Surface cleaning

### Materials & Technical (3 keywords)
- Hot mix asphalt
- Warm mix asphalt
- Cold mix asphalt

### Problem Areas (3 keywords)
- Asphalt cracking
- Potholes
- Drainage issues

### Customer Intent (4 keywords)
- Free quote
- Cost
- Near me
- Best contractor

### Additional Services (5 keywords)
- Land clearing
- Excavating work
- Gravel work
- Concrete work
- Tear out

## Integration with Your YAML Files

### Linking to services.yaml

In your services.yaml file, use the `keyword_id` to link services to keywords:

```yaml
services:
  - service_id: srv-sealcoating
    name: Seal Coating
    related_keyword_ids:
      - kw-sealcoating
      - kw-seal-coating
      - kw-preventative-maintenance
      - kw-sealcoating-crack-sealing
```

### Linking to locations.yaml

Combine keywords with location data for hyper-local SEO:

Example content generation:
- "Asphalt paving in Davenport, FL" (kw-asphalt-paving + loc-davenport)
- "Parking lot sealcoating Marshfield, WI" (kw-sealcoating + loc-marshfield-wi)

## SEO Strategy by Keyword Type

### High-Conversion Keywords (Target First)
These have `conversion_potential: very-high` or `conversion_potential: high`:

1. **kw-paving-contractor** - People actively looking for contractors
2. **kw-free-quote** - Ready to request services
3. **kw-near-me** - Local intent, high urgency
4. **kw-asphalt-paving** - Core service, high volume
5. **kw-asphalt-driveway** - Residential focus, clear need

### Content Marketing Keywords
These are `search_intent: informational` - build authority:

- kw-chip-seal
- kw-base-work
- kw-porous-asphalt
- kw-cracking
- kw-drainage-issues

### Commercial Keywords
These have `search_intent: commercial` - for comparison content:

- kw-cost
- kw-best-contractor
- kw-concrete-work (for asphalt vs concrete comparisons)

## Content Creation Strategy

### For Each Keyword, Create:

1. **Primary Service Page**
   - Target: primary_keyword
   - Include: All semantic_equivalents naturally in content
   - H2/H3 sections: Address each long_tail_variation topic

2. **Location-Specific Pages**
   - Combine keyword with each location
   - Example: "Asphalt Paving in [City Name]"

3. **FAQ Content**
   - Each long_tail_variation is a potential FAQ
   - Example: "How often to sealcoat driveway?" → FAQ answer

4. **Blog Posts**
   - Use content_topics as blog themes
   - Link back to service pages

## Technical Level Guidance

- **basic**: Write for homeowners, minimal jargon
- **intermediate**: Business owners, some technical detail
- **advanced**: Technical decision-makers, full specifications

## Search Volume Tiers

- **high**: Primary focus, optimize first, most traffic potential
- **medium**: Secondary focus, good opportunities
- **low**: Long-tail, niche targeting, lower traffic but often higher intent

## Next Steps

1. **Audit Current Content**
   - Compare your existing pages to these keywords
   - Identify gaps

2. **Create Content Calendar**
   - Prioritize high-conversion keywords
   - Schedule 2-4 pieces of content per month

3. **Optimize Existing Pages**
   - Add semantic_equivalents to current content
   - Include long_tail_variations in H2/H3 headers

4. **Build Location Pages**
   - Create [service] + [location] pages for top keywords
   - Target: kw-near-me searches

5. **Track Performance**
   - Monitor which keywords drive traffic
   - Adjust strategy based on results

## Usage Examples

### Example 1: Creating a Service Page
For "Sealcoating Services" page:
- Primary keyword: "sealcoating" (kw-sealcoating)
- Semantic equivalents to include:
  - seal coating
  - asphalt sealing
  - pavement sealing
  - driveway sealing
- Long-tail variations for H2 sections:
  - "How Often to Sealcoat Your Driveway"
  - "Commercial Sealcoating Services"
  - "Sealcoating and Crack Sealing Package"

### Example 2: Local SEO Page
For "Davenport Asphalt Paving" page:
- Primary keyword: "asphalt paving" (kw-asphalt-paving)
- Location: "Davenport, FL" (loc-davenport)
- Title: "Asphalt Paving Contractor in Davenport, FL"
- Include: residential paving, commercial paving, parking lot paving
- Reference: local challenges (hot weather, seasonal rain)

### Example 3: Blog Post
Topic: "Understanding Different Types of Asphalt Cracks"
- Primary keyword: "asphalt cracking" (kw-cracking)
- Content topics: crack-types, causes, repair-options, prevention
- Related keywords: kw-crack-filling, kw-preventative-maintenance
- Link to: crack sealing service pages

## Benefits of This Structure

✅ **Semantic SEO Ready**: Google understands your content covers the full topic
✅ **Easy Integration**: Links directly to your services and locations
✅ **Scalable**: Add new keywords following the same structure
✅ **Content Planning**: Clear guidance on what to write
✅ **Conversion Focused**: Prioritizes high-intent keywords
✅ **Local SEO**: Combines with location data for geo-targeting

## Maintenance

Update this file:
- **Quarterly**: Review search volume tiers based on actual traffic
- **Annually**: Add new keywords from customer questions
- **As needed**: Adjust based on SEO performance data

---

## Quick Reference: Top 20 Keywords to Target First

Based on conversion_potential and search_volume_tier:

1. kw-paving-contractor (very-high conversion)
2. kw-free-quote (very-high conversion)
3. kw-near-me (very-high conversion)
4. kw-asphalt-paving (high volume + high conversion)
5. kw-asphalt-driveway (high volume + high conversion)
6. kw-sealcoating (high volume + high conversion)
7. kw-cost (high volume + high conversion)
8. kw-parking-lot-paving (medium volume + high conversion)
9. kw-asphalt-repair (high volume + high conversion)
10. kw-crack-filling (medium volume + high conversion)
11. kw-pothole-repair (medium volume + high conversion)
12. kw-residential-paving (medium volume + high conversion)
13. kw-commercial-paving (medium volume + high conversion)
14. kw-driveway-paving (high volume + high conversion)
15. kw-asphalt-resurfacing (medium volume + high conversion)
16. kw-best-contractor (medium volume + high conversion)
17. kw-patching (medium volume + high conversion)
18. kw-new-paving (medium volume + high conversion)
19. kw-sealcoating-crack-sealing (low volume + high conversion)
20. kw-potholes (medium volume + high conversion)

Focus on these first for maximum ROI on your SEO efforts!
