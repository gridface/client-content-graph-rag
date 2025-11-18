
# Analyze the data structure to understand the content generation architecture
import yaml

# Let's understand the data relationships
analysis = {
    "data_structure": {
        "rag_source": "618k character comprehensive asphalt textbook (300+ pages)",
        "clients": "6 asphalt contractors with location/service mappings",
        "services": "50+ detailed service definitions with keywords, standards, seasonal considerations",
        "keywords": "Semantic keyword clusters with intent, variations, long-tail options",
        "locations": "100+ locations with climate, economic, demographic, challenge data"
    },
    "key_relationships": {
        "client_to_services": "active_services array links client to service_id",
        "client_to_locations": "service_area_ids array links client to location_id", 
        "service_to_keywords": "related_keyword_ids array links service to keyword_id",
        "location_context": "climate_zone, local_challenges, economic_profile, flavor_notes"
    },
    "content_generation_components": {
        "technical_authority": "RAG textbook provides deep technical knowledge",
        "hyper_local_context": "Locations provide specific geographic/demographic/climate details",
        "service_specificity": "Services include expertise signals, equipment, duration, seasonal considerations",
        "semantic_relevance": "Keywords provide natural language variations and search intent",
        "client_differentiation": "Client size, specialties, service offerings vary"
    },
    "blog_generation_inputs": {
        "required": [
            "client_id - who is this content for",
            "location_id - where is the service area",
            "service_id(s) - what services to focus on",
            "content_type - educational, promotional, seasonal, FAQ, comparison"
        ],
        "enrichment_data": [
            "technical_depth from RAG",
            "local_flavor from location data",
            "keyword_optimization from keywords.yaml",
            "expertise_signals from services.yaml",
            "competitive_positioning from client.yaml"
        ]
    }
}

print("=" * 80)
print("CONTENT GENERATION ARCHITECTURE ANALYSIS")
print("=" * 80)
print()

for category, items in analysis.items():
    print(f"\n{category.upper().replace('_', ' ')}:")
    print("-" * 60)
    if isinstance(items, dict):
        for key, value in items.items():
            print(f"  • {key}: {value}")
    elif isinstance(items, list):
        for item in items:
            print(f"  • {item}")
print()

# Identify the content generation flow
print("\n" + "=" * 80)
print("PROPOSED CONTENT GENERATION FLOW")
print("=" * 80)

flow = """
1. INPUT PHASE
   - User specifies: Client, Location(s), Service(s), Content Type
   - System retrieves: Client profile, Location context, Service details, Related keywords

2. CONTEXT BUILDING PHASE
   - Merge location climate/challenges with service seasonal considerations
   - Extract relevant RAG technical content for service type
   - Identify semantic keyword variations for natural language
   - Pull client-specific differentiators (expertise, size, specialties)

3. CONTENT STRUCTURING PHASE
   - Generate title with location + service + semantic variation
   - Create outline based on content type template
   - Map RAG technical sections to outline sections
   - Inject local flavor notes and challenges into relevant sections

4. GENERATION PHASE
   - Use system prompt with full context package
   - Generate draft with technical accuracy from RAG
   - Weave in hyper-local details from location data
   - Include semantic keyword variations naturally
   - Add client expertise signals and CTAs

5. OPTIMIZATION PHASE
   - Verify technical accuracy against RAG source
   - Check local relevance and specificity
   - Ensure semantic variety (avoid keyword stuffing)
   - Validate client positioning and differentiation
"""

print(flow)
