# 🔍 Comprehensive Search Query Library for Asphalt Services

## How to Use This Library

Each service type has **3-5 targeted queries** mapped to typical blog sections. Use only the queries relevant to your specific blog structure.

**Token Budget per Article:**
- 3 queries × 3 results × 700 tokens = ~6,300 tokens (vs 20,000+ with broad searches)
- 4 queries × 2-3 results × 600 tokens = ~7,200 tokens
- 5 queries × 2 results × 500 tokens = ~5,000 tokens

---

## 📁 Service Category Index

1. [Core Paving Services](#core-paving-services)
2. [Repair Services](#repair-services)
3. [Resurfacing & Rehabilitation](#resurfacing--rehabilitation)
4. [Preventative Maintenance](#preventative-maintenance)
5. [Climate-Specific Services](#climate-specific-services)
6. [Site Preparation & Base Work](#site-preparation--base-work)
7. [Specialty Services](#specialty-services)
8. [Striping & Marking](#striping--marking)
9. [Niche Applications](#niche-applications)

---

## Core Paving Services

### 🏠 New Residential Asphalt Paving

**Service ID:** `srv-new-asphalt-paving-residential`

```yaml
blog_sections:
  
  introduction_why_it_matters:
    query: "residential driveway asphalt thickness design specifications homeowner"
    max_results: 3
    use_for: "Explaining what goes into quality residential paving"
  
  material_specifications:
    query: "asphalt mix design binder grade residential driveway 3/4 inch NMAS"
    max_results: 3
    use_for: "Technical specs in accessible language"
  
  base_and_drainage:
    query: "base preparation aggregate compaction residential driveway drainage slope"
    max_results: 3
    use_for: "Why proper foundation matters"
  
  installation_process:
    query: "paving process compaction roller density residential construction"
    max_results: 2
    use_for: "What homeowners should expect during installation"
  
  longevity_and_maintenance:
    query: "driveway sealcoating crack sealing preventative maintenance residential"
    max_results: 2
    use_for: "How to protect investment long-term"

total_queries: 5
expected_tokens: 6,500
```

### 🏢 New Commercial Asphalt Paving

**Service ID:** `srv-new-asphalt-paving-commercial`

```yaml
blog_sections:
  
  engineering_and_design:
    query: "commercial parking lot pavement design traffic loads ESALs thickness"
    max_results: 3
    use_for: "Engineering approach for commercial projects"
  
  traffic_considerations:
    query: "heavy traffic truck loads commercial paving structural design"
    max_results: 3
    use_for: "Why commercial differs from residential"
  
  material_specifications:
    query: "commercial asphalt mix design binder grade heavy duty specifications"
    max_results: 3
    use_for: "Materials for durability under commercial traffic"
  
  drainage_and_grading:
    query: "parking lot drainage design grading stormwater ADA compliance"
    max_results: 2
    use_for: "Critical drainage requirements"
  
  striping_and_compliance:
    query: "parking lot striping ADA compliance handicap accessibility MUTCD"
    max_results: 2
    use_for: "Post-paving requirements"

total_queries: 5
expected_tokens: 6,500
```

### 🏛️ Municipal Asphalt Paving

**Service ID:** `srv-new-asphalt-paving-municipal`

```yaml
blog_sections:
  
  specifications_and_standards:
    query: "municipal road specifications AASHTO standards public works requirements"
    max_results: 3
    use_for: "Government project requirements"
  
  pavement_design:
    query: "roadway pavement design traffic analysis structural number municipal"
    max_results: 3
    use_for: "Engineering for public roads"
  
  quality_control:
    query: "quality control testing density nuclear gauge core sampling specifications"
    max_results: 2
    use_for: "QC requirements for public projects"
  
  traffic_management:
    query: "traffic control work zone safety MOT municipal construction"
    max_results: 2
    use_for: "Managing construction in public spaces"

total_queries: 4
expected_tokens: 5,000
```

---

## Repair Services

### 🔧 Asphalt Patching (Full-Depth)

**Service ID:** `srv-asphalt-patching-full-depth`

```yaml
blog_sections:
  
  when_patching_needed:
    query: "asphalt failure types base failure alligator cracking when to patch"
    max_results: 3
    use_for: "Identifying when full-depth repair is necessary"
  
  patch_process:
    query: "full depth patching saw cutting excavation compaction permanent repair"
    max_results: 3
    use_for: "Step-by-step repair methodology"
  
  material_considerations:
    query: "patch mix design tack coat bonding edge preparation"
    max_results: 2
    use_for: "Ensuring patches last and blend properly"
  
  cost_vs_alternatives:
    query: "patching versus resurfacing cost comparison repair decision"
    max_results: 2
    use_for: "When to patch vs. larger repairs"

total_queries: 4
expected_tokens: 5,000
```

### 🕳️ Pothole Repair

**Service ID:** `srv-pothole-repair`

```yaml
blog_sections:
  
  pothole_formation:
    query: "pothole formation causes water damage freeze thaw deterioration"
    max_results: 3
    use_for: "Why potholes form (climate-specific)"
  
  repair_methods:
    query: "pothole repair methods throw and roll semi-permanent spray injection"
    max_results: 3
    use_for: "Different repair approaches and when to use"
  
  temporary_vs_permanent:
    query: "cold patch temporary repair hot mix permanent pothole repair"
    max_results: 2
    use_for: "Understanding repair options"
  
  prevention:
    query: "pothole prevention crack sealing sealcoating water management"
    max_results: 2
    use_for: "How to prevent future potholes"

total_queries: 4
expected_tokens: 5,000
```

### 📍 Surface Patching

**Service ID:** `srv-surface-patching`

```yaml
blog_sections:
  
  when_surface_patching_works:
    query: "surface patching shallow repair skin patching applications limitations"
    max_results: 3
    use_for: "Appropriate use cases for surface patches"
  
  application_methods:
    query: "infrared patching surface repair techniques bonding existing pavement"
    max_results: 3
    use_for: "Modern patching technologies"
  
  expectations_and_limitations:
    query: "surface patch durability limitations temporary versus structural repair"
    max_results: 2
    use_for: "Setting realistic expectations"

total_queries: 3
expected_tokens: 4,000
```

---

## Resurfacing & Rehabilitation

### 🔄 Asphalt Resurfacing (Overlay)

**Service ID:** `srv-asphalt-resurfacing`

```yaml
blog_sections:
  
  when_overlay_appropriate:
    query: "overlay versus reconstruction pavement evaluation structural condition assessment"
    max_results: 3
    use_for: "Determining if overlay is right solution"
  
  surface_preparation:
    query: "overlay preparation crack repair patching tack coat bonding"
    max_results: 3
    use_for: "Critical prep work before overlaying"
  
  thickness_and_specifications:
    query: "overlay thickness design structural contribution service life extension"
    max_results: 2
    use_for: "Technical specifications for overlays"
  
  benefits_and_limitations:
    query: "overlay benefits elevation increase curb reveal drainage considerations"
    max_results: 2
    use_for: "Pros and cons of overlaying"

total_queries: 4
expected_tokens: 5,000
```

### ⚙️ Mill and Overlay

**Service ID:** `srv-mill-and-overlay`

```yaml
blog_sections:
  
  milling_process:
    query: "asphalt milling cold planer operation depth control RAP material"
    max_results: 3
    use_for: "What happens during milling"
  
  benefits_over_overlay:
    query: "mill and overlay versus overlay elevation control curb height drainage"
    max_results: 3
    use_for: "Why mill before overlaying"
  
  rap_recycling:
    query: "RAP reclaimed asphalt pavement recycling sustainability cost savings"
    max_results: 2
    use_for: "Environmental and economic benefits"
  
  typical_applications:
    query: "mill and overlay parking lot rehabilitation roadway resurfacing schedule"
    max_results: 2
    use_for: "When this is the standard treatment"

total_queries: 4
expected_tokens: 5,000
```

### 🔨 Full-Depth Reclamation (FDR)

**Service ID:** `srv-full-depth-reclamation`

```yaml
blog_sections:
  
  what_is_fdr:
    query: "full depth reclamation FDR process pulverization stabilization"
    max_results: 3
    use_for: "Explaining the FDR technique"
  
  when_fdr_makes_sense:
    query: "FDR versus reconstruction cost comparison base failure severe distress"
    max_results: 3
    use_for: "Economic decision-making"
  
  stabilization_materials:
    query: "cement stabilization lime stabilization emulsion FDR additives"
    max_results: 2
    use_for: "Technical approach to stabilization"
  
  benefits_and_sustainability:
    query: "FDR environmental benefits material recycling in place reconstruction"
    max_results: 2
    use_for: "Why FDR is increasingly popular"

total_queries: 4
expected_tokens: 5,000
```

---

## Preventative Maintenance

### 🛡️ Crack Sealing

**Service ID:** `srv-crack-sealing`

```yaml
blog_sections:
  
  why_seal_cracks:
    query: "crack sealing water infiltration pavement preservation cost benefit"
    max_results: 3
    use_for: "The importance of crack sealing"
  
  crack_types:
    query: "crack types transverse longitudinal alligator block thermal fatigue"
    max_results: 3
    use_for: "Understanding different crack patterns"
  
  hot_pour_vs_cold:
    query: "hot pour crack sealant rubberized cold pour quality comparison"
    max_results: 2
    use_for: "Material selection for crack sealing"
  
  process_and_timing:
    query: "crack sealing process routing cleaning sealant application best practices"
    max_results: 2
    use_for: "Proper crack sealing methodology"

total_queries: 4
expected_tokens: 5,000
```

### 🖤 Sealcoating

**Service ID:** `srv-sealcoating-residential` / `srv-sealcoating-commercial`

```yaml
blog_sections:
  
  sealcoat_benefits:
    query: "sealcoating benefits UV protection oxidation water resistance appearance"
    max_results: 3
    use_for: "Why sealcoating matters"
  
  material_types:
    query: "coal tar sealcoat asphalt emulsion sealer material comparison quality"
    max_results: 3
    use_for: "Understanding sealer options"
  
  application_process:
    query: "sealcoating application process weather requirements drying time traffic"
    max_results: 2
    use_for: "What to expect during application"
  
  frequency_and_timing:
    query: "sealcoating frequency schedule maintenance interval climate considerations"
    max_results: 2
    use_for: "Developing maintenance schedule"

total_queries: 4
expected_tokens: 5,000
```

### 📋 Crack Seal and Sealcoat Package

**Service ID:** `srv-crack-seal-and-sealcoat-package`

```yaml
blog_sections:
  
  combined_benefits:
    query: "crack sealing sealcoating together comprehensive maintenance protection"
    max_results: 3
    use_for: "Why combine both services"
  
  proper_sequence:
    query: "crack sealing before sealcoating surface preparation sequence timing"
    max_results: 2
    use_for: "Order of operations"
  
  cost_value_analysis:
    query: "preventative maintenance cost benefit pavement preservation ROI"
    max_results: 2
    use_for: "Economic justification"

total_queries: 3
expected_tokens: 3,500
```

---

## Climate-Specific Services

### 🌡️ Hot Climate Paving

**Service ID:** `srv-hot-climate-paving`

```yaml
blog_sections:
  
  climate_challenges:
    query: "hot climate rutting high temperature UV aging oxidation challenges"
    max_results: 3
    use_for: "Specific problems in hot climates"
  
  binder_selection:
    query: "PG 76 70 binder grade hot climate high temperature rutting resistance"
    max_results: 3
    use_for: "Material selection for heat"
  
  polymer_modification:
    query: "polymer modified asphalt SBS hot climate heavy traffic rutting"
    max_results: 2
    use_for: "Advanced materials for demanding conditions"
  
  construction_practices:
    query: "hot weather paving temperature management compaction timing summer"
    max_results: 2
    use_for: "Installation best practices"
  
  maintenance_considerations:
    query: "hot climate maintenance UV protection sealcoating aging oxidation"
    max_results: 2
    use_for: "Long-term care in hot climates"

total_queries: 5
expected_tokens: 6,000
```

### ❄️ Cold Climate Paving

**Service ID:** `srv-cold-climate-paving`

```yaml
blog_sections:
  
  climate_challenges:
    query: "freeze thaw cycles thermal cracking low temperature pavement failure"
    max_results: 3
    use_for: "Specific problems in cold climates"
  
  binder_selection:
    query: "PG 58 52 binder grade cold climate low temperature thermal cracking"
    max_results: 3
    use_for: "Material selection for cold"
  
  drainage_critical:
    query: "drainage freeze thaw prevention underdrain base design cold climate"
    max_results: 3
    use_for: "Why drainage is critical in cold climates"
  
  construction_season:
    query: "paving season cold climate warm mix asphalt extended season temperature"
    max_results: 2
    use_for: "When to pave and modern solutions"
  
  spring_damage:
    query: "spring thaw pothole formation frost heave winter damage repair"
    max_results: 2
    use_for: "Seasonal challenges and solutions"

total_queries: 5
expected_tokens: 6,500
```

### 🌊 Coastal & Hurricane Zone Paving

**Service ID:** `srv-coastal-hurricane-zone-paving`

```yaml
blog_sections:
  
  coastal_challenges:
    query: "coastal saltwater exposure moisture damage humidity hurricane flooding"
    max_results: 3
    use_for: "Unique coastal environmental factors"
  
  material_selection:
    query: "moisture resistant asphalt anti stripping additives coastal durability"
    max_results: 3
    use_for: "Materials for coastal conditions"
  
  drainage_critical:
    query: "coastal drainage design flood resilience stormwater surge hurricane"
    max_results: 2
    use_for: "Enhanced drainage requirements"
  
  storm_preparation:
    query: "hurricane damage prevention storm surge repair flood recovery asphalt"
    max_results: 2
    use_for: "Preparation and recovery"

total_queries: 4
expected_tokens: 5,000
```

---

## Site Preparation & Base Work

### 🏗️ Grading & Excavation

**Service ID:** `srv-grading-excavation`

```yaml
blog_sections:
  
  importance_of_grading:
    query: "site grading drainage slope preparation excavation importance"
    max_results: 3
    use_for: "Why proper grading matters"
  
  subgrade_preparation:
    query: "subgrade preparation compaction testing proctor density soil"
    max_results: 3
    use_for: "Foundation preparation"
  
  drainage_design:
    query: "site drainage design positive drainage grading slope requirements"
    max_results: 2
    use_for: "Water management through grading"

total_queries: 3
expected_tokens: 4,000
```

### 🪨 Base Installation

**Service ID:** `srv-base-installation`

```yaml
blog_sections:
  
  base_importance:
    query: "aggregate base importance structural support load distribution thickness"
    max_results: 3
    use_for: "Why base is critical to pavement performance"
  
  material_specifications:
    query: "aggregate base material specifications gradation compaction standards"
    max_results: 3
    use_for: "What makes quality base material"
  
  installation_process:
    query: "base installation compaction lift thickness proof rolling quality"
    max_results: 2
    use_for: "Proper installation methodology"
  
  thickness_design:
    query: "base thickness design traffic loads soil bearing capacity CBR"
    max_results: 2
    use_for: "Engineering base thickness"

total_queries: 4
expected_tokens: 5,000
```

### 💧 Drainage Installation

**Service ID:** `srv-drainage-installation`

```yaml
blog_sections:
  
  drainage_critical:
    query: "pavement drainage water damage prevention longevity base failure"
    max_results: 3
    use_for: "Why drainage determines pavement life"
  
  drainage_solutions:
    query: "catch basin french drain underdrain edge drain systems design"
    max_results: 3
    use_for: "Types of drainage systems"
  
  integration_with_paving:
    query: "drainage integration grading slope positive drainage design"
    max_results: 2
    use_for: "How drainage works with paving"

total_queries: 3
expected_tokens: 4,000
```

---

## Specialty Services

### 🌿 Porous Asphalt

**Service ID:** `srv-porous-asphalt`

```yaml
blog_sections:
  
  what_is_porous:
    query: "porous asphalt permeable pavement open graded drainage stormwater"
    max_results: 3
    use_for: "Understanding porous pavement technology"
  
  environmental_benefits:
    query: "porous asphalt stormwater management environmental benefits sustainability"
    max_results: 3
    use_for: "Why property owners choose porous"
  
  applications:
    query: "porous asphalt parking lot applications limitations maintenance requirements"
    max_results: 2
    use_for: "Where it works and where it doesn't"
  
  maintenance:
    query: "porous asphalt maintenance vacuuming clogging prevention cleaning"
    max_results: 2
    use_for: "Unique maintenance needs"

total_queries: 4
expected_tokens: 5,000
```

### 🔥 Warm Mix Asphalt

**Service ID:** `srv-warm-mix-asphalt`

```yaml
blog_sections:
  
  what_is_wma:
    query: "warm mix asphalt WMA technology temperature reduction additives"
    max_results: 3
    use_for: "Explaining WMA technology"
  
  benefits:
    query: "warm mix asphalt benefits emissions energy extended season sustainability"
    max_results: 3
    use_for: "Environmental and practical advantages"
  
  applications:
    query: "warm mix asphalt applications cold weather paving season extension"
    max_results: 2
    use_for: "When WMA makes sense"

total_queries: 3
expected_tokens: 4,000
```

### ♻️ High-RAP Mixes

**Service ID:** `srv-high-rap-mixes`

```yaml
blog_sections:
  
  what_is_rap:
    query: "RAP reclaimed asphalt pavement recycling sustainability percentage"
    max_results: 3
    use_for: "Understanding recycled asphalt"
  
  performance:
    query: "high RAP mix design quality performance durability rejuvenators"
    max_results: 3
    use_for: "Does recycled perform as well?"
  
  environmental_economic:
    query: "RAP benefits cost savings environmental sustainability recycling"
    max_results: 2
    use_for: "Why choose high-RAP mixes"

total_queries: 3
expected_tokens: 4,000
```

---

## Striping & Marking

### 🚗 Parking Lot Striping

**Service ID:** `srv-parking-lot-striping`

```yaml
blog_sections:
  
  importance_compliance:
    query: "parking lot striping ADA compliance MUTCD standards regulations"
    max_results: 3
    use_for: "Legal requirements and safety"
  
  layout_design:
    query: "parking lot layout design stall dimensions traffic flow efficiency"
    max_results: 3
    use_for: "Optimizing parking design"
  
  materials_durability:
    query: "striping materials paint thermoplastic durability longevity comparison"
    max_results: 2
    use_for: "Material options and lifespan"

total_queries: 3
expected_tokens: 4,000
```

### 🛣️ Roadway Striping

**Service ID:** `srv-roadway-striping`

```yaml
blog_sections:
  
  mutcd_standards:
    query: "roadway striping MUTCD standards regulations traffic control markings"
    max_results: 3
    use_for: "Federal and state requirements"
  
  marking_types:
    query: "pavement markings edge lines centerlines crosswalks stop bars standards"
    max_results: 3
    use_for: "Different marking types and meanings"
  
  materials_retroreflectivity:
    query: "thermoplastic markings retroreflectivity beads durability specifications"
    max_results: 2
    use_for: "High-performance marking materials"

total_queries: 3
expected_tokens: 4,000
```

### ♿ ADA Compliance Marking

**Service ID:** `srv-ada-compliance-marking`

```yaml
blog_sections:
  
  ada_requirements:
    query: "ADA parking requirements handicap spaces van accessible dimensions"
    max_results: 3
    use_for: "Legal compliance requirements"
  
  proper_layout:
    query: "accessible parking layout access aisle ramp connection specifications"
    max_results: 3
    use_for: "Correct installation and design"
  
  signage_marking:
    query: "ADA signage international symbol mounting height vertical clearance"
    max_results: 2
    use_for: "Complete accessibility solution"

total_queries: 3
expected_tokens: 4,000
```

---

## Niche Applications

### ✈️ Airport Paving

**Service ID:** `srv-airport-paving`

```yaml
blog_sections:
  
  extreme_requirements:
    query: "airport pavement design heavy aircraft loads jet fuel resistance FAA"
    max_results: 3
    use_for: "Unique demands of airport paving"
  
  specifications:
    query: "FAA airport specifications P-401 P-403 AC 150 airfield construction"
    max_results: 3
    use_for: "Federal aviation requirements"
  
  specialized_materials:
    query: "airport asphalt fuel resistant polymer modified high stability mix"
    max_results: 2
    use_for: "Advanced materials for airports"

total_queries: 3
expected_tokens: 4,000
```

### 🏭 Industrial Heavy-Duty Paving

**Service ID:** `srv-industrial-heavy-duty-paving`

```yaml
blog_sections:
  
  heavy_load_design:
    query: "heavy duty pavement design industrial loads trucks equipment thickness"
    max_results: 3
    use_for: "Engineering for extreme loads"
  
  material_specifications:
    query: "industrial pavement mix design high stability polymer modified heavy duty"
    max_results: 3
    use_for: "Materials for industrial applications"
  
  applications:
    query: "industrial paving loading dock container yard truck terminal heavy equipment"
    max_results: 2
    use_for: "Where heavy-duty paving is needed"

total_queries: 3
expected_tokens: 4,000
```

### 🚴 Bike Path & Trail Paving

**Service ID:** `srv-bike-path-trail-paving`

```yaml
blog_sections:
  
  design_requirements:
    query: "bike path trail design width slope specifications AASHTO greenway"
    max_results: 3
    use_for: "Standards for recreational paths"
  
  surface_quality:
    query: "bike trail smoothness surface texture pavement quality ride comfort"
    max_results: 2
    use_for: "Why smooth surface matters"
  
  environmental_considerations:
    query: "trail paving environmental impact permeable drainage sustainable construction"
    max_results: 2
    use_for: "Eco-friendly trail construction"

total_queries: 3
expected_tokens: 3,500
```

### 🎾 Sports Facility Paving

**Service ID:** `srv-sports-facility-paving`

```yaml
blog_sections:
  
  extreme_standards:
    query: "tennis court specifications USTA asphalt base smoothness flatness"
    max_results: 3
    use_for: "Precision requirements for sports surfaces"
  
  construction_process:
    query: "sports court construction laser grading precision paving acrylic coating"
    max_results: 2
    use_for: "Installation methodology"
  
  surface_systems:
    query: "acrylic sport surface coating cushioned system basketball tennis court"
    max_results: 2
    use_for: "Surface finishing options"

total_queries: 3
expected_tokens: 3,500
```

---

## 🎯 Implementation Guide

### Quick Reference: Token Budget by Article Type

```yaml
simple_services:  # Crack sealing, sealcoating, surface patching
  queries: 3
  results_per_query: 2-3
  total_tokens: 3,500-4,500

standard_services:  # Most paving, repair, resurfacing
  queries: 4
  results_per_query: 2-3
  total_tokens: 5,000-6,000

complex_services:  # Climate-specific, specialized applications
  queries: 5
  results_per_query: 2-3
  total_tokens: 6,000-7,500
```

### Query Construction Best Practices

**✅ DO:**
- Use 5-8 specific keywords per query
- Include technical terms + practical applications
- Combine service + climate/location factors
- Target specific blog sections

**❌ DON'T:**
- Use single broad terms ("paving", "asphalt")
- Include filler words ("and", "or", "the", "how to")
- Make queries longer than 10 words
- Repeat the same query with slight variations

### Example Query Optimization

```yaml
# ❌ Bad: Too broad, will return everything
"asphalt paving"

# ❌ Bad: Too narrow, might miss relevant info  
"PG 76-22 binder for Wesley Chapel Florida summer heat rutting"

# ✅ Good: Specific but not overly narrow
"PG 76 70 binder hot climate rutting prevention"

# ✅ Good: Combines technical + practical
"polymer modified SBS high temperature heavy traffic"

# ✅ Good: Location-relevant without being too specific
"hot weather paving compaction temperature management"
```

---

## 📊 Expected Savings

**Using this library vs. your current approach:**

| Metric | Current | With Library | Savings |
|--------|---------|--------------|---------|
| Avg queries per article | 1-2 broad | 3-5 targeted | N/A |
| Avg tokens per article | 30,000+ | 8,000-10,000 | **70%** |
| Cost per article | $0.80-1.20 | $0.25-0.40 | **67%** |
| Relevant info ratio | ~40% | ~85% | Better quality |

---

## 🔧 Next Steps

1. **Copy this library** into your project documentation
2. **Update your user prompt template** to reference specific queries by service type
3. **Test with 3-4 articles** to verify output quality remains high
4. **Track token usage** and refine queries that return too much/too little
5. **Build n8n workflow** that automatically selects queries based on service_id

Want me to create the updated user prompt template that uses this library? Or help you build the n8n workflow logic?