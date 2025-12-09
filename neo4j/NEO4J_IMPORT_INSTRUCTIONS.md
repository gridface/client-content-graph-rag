# Neo4j Import Instructions for Centaur Ontology

## Generated Files

### Node Files
| File | Type | Records | Description |
|------|------|---------|-------------|
| `clients_nodes.csv` | Nodes | 6 | Client entities |
| `locations_nodes.csv` | Nodes | 109 | Location entities (WI, FL, MO, AR, MN) |
| `services_nodes.csv` | Nodes | 51 | Asphalt service offerings |
| `keywords_nodes.csv` | Nodes | 40 | SEO keyword clusters |

### Relationship Files
| File | Type | Records | Description |
|------|------|---------|-------------|
| `client_main_address_rels.csv` | Relationships | 6 | Client → Location (HAS_MAIN_ADDRESS) |
| `client_serves_area_rels.csv` | Relationships | 111 | Client → Location (SERVES_AREA) |
| `client_offers_service_rels.csv` | Relationships | 192 | Client → Service (OFFERS_SERVICE) |
| `service_has_keyword_rels.csv` | Relationships | 115 | Service → Keyword (HAS_KEYWORD) |
| `location_near_rels.csv` | Relationships | 300 | Location → Location (NEAR) |

**Total: 206 nodes, 724 relationships**

## Schema Overview

```
(:Client)-[:HAS_MAIN_ADDRESS]->(:Location)
(:Client)-[:SERVES_AREA]->(:Location)
(:Client)-[:OFFERS_SERVICE]->(:Service)
(:Service)-[:HAS_KEYWORD]->(:Keyword)
(:Location)-[:NEAR]->(:Location)
```

## ID Spaces Used

The CSVs use Neo4j ID spaces for referential integrity:
- `Client` - customerId (e.g., `client-wells-wi`)
- `Location` - locationId (e.g., `loc-madison-wi`)
- `Service` - serviceId (e.g., `srv-sealcoating-residential`)
- `Keyword` - keywordId (e.g., `kw-asphalt-paving`)

---

## Import Method 1: Neo4j Data Importer (Recommended for Desktop/Aura)

### Steps:
1. Open Neo4j Desktop or go to your Aura instance
2. Navigate to **Import** → **Open Data Importer**
3. Drag and drop all 4 CSV files
4. The importer will auto-detect:
   - Node files (has `:LABEL` column)
   - Relationship files (has `:START_ID` and `:END_ID` columns)
5. Map the ID spaces:
   - For `clients_nodes.csv`: Set ID property to `customerId` with ID space `Client`
   - For relationships: Confirm start/end ID spaces match
6. Click **Run Import**

---

## Import Method 2: neo4j-admin import (Bulk Import - Empty Database)

For large datasets or fresh database setup. **This only works on an empty database.**

```bash
# Place all CSV files in the import directory, then run:

neo4j-admin database import full \
  --nodes=Location=locations_nodes.csv \
  --nodes=Service=services_nodes.csv \
  --nodes=Keyword=keywords_nodes.csv \
  --nodes=Client=clients_nodes.csv \
  --relationships=client_main_address_rels.csv \
  --relationships=client_serves_area_rels.csv \
  --relationships=client_offers_service_rels.csv \
  --relationships=service_has_keyword_rels.csv \
  --relationships=location_near_rels.csv \
  --array-delimiter=";" \
  neo4j
```

### Notes:
- Replace `neo4j` with your database name
- The `--array-delimiter=";"` is required for array properties (e.g., `localChallenges`, `serviceTypes`)
- Order matters: nodes before relationships

---

## Import Method 3: Cypher LOAD CSV (Existing Database)

### Step 1: Import Location Nodes
```cypher
LOAD CSV WITH HEADERS FROM 'file:///locations_nodes.csv' AS row
CREATE (l:Location {
  locationId: row.`locationId:ID(Location)`,
  name: row.name,
  region: row.region,
  state: row.state,
  postalCode: row.postalCode,
  country: row.country,
  geoLatitude: toFloat(row.`geoLatitude:double`),
  geoLongitude: toFloat(row.`geoLongitude:double`),
  population: toInteger(row.`population:int`),
  climateZone: row.climateZone,
  economicProfile: row.economicProfile,
  localChallenges: split(row.`localChallenges:string[]`, ';'),
  flavorNotes: row.flavorNotes
});
```

### Step 2: Import Service Nodes
```cypher
LOAD CSV WITH HEADERS FROM 'file:///services_nodes.csv' AS row
CREATE (s:Service {
  serviceId: row.`serviceId:ID(Service)`,
  name: row.name,
  serviceTypes: split(row.`serviceTypes:string[]`, ';'),
  description: row.description,
  expertiseSignals: split(row.`expertiseSignals:string[]`, ';'),
  regulatoryStandards: split(row.`regulatoryStandards:string[]`, ';'),
  seasonalConsiderations: row.seasonalConsiderations,
  equipmentRequired: row.equipmentRequired,
  typicalDuration: row.typicalDuration,
  notes: row.notes
});
```

### Step 3: Import Keyword Nodes
```cypher
LOAD CSV WITH HEADERS FROM 'file:///keywords_nodes.csv' AS row
CREATE (k:Keyword {
  keywordId: row.`keywordId:ID(Keyword)`,
  primaryKeyword: row.primaryKeyword,
  searchIntent: row.searchIntent,
  customerType: row.customerType,
  semanticEquivalents: split(row.`semanticEquivalents:string[]`, ';'),
  relatedTerms: split(row.`relatedTerms:string[]`, ';'),
  longTailVariations: split(row.`longTailVariations:string[]`, ';'),
  searchVolumeTier: row.searchVolumeTier,
  conversionPotential: row.conversionPotential,
  contentTopics: split(row.`contentTopics:string[]`, ';'),
  technicalLevel: row.technicalLevel
});
```

### Step 4: Import Client Nodes
```cypher
LOAD CSV WITH HEADERS FROM 'file:///clients_nodes.csv' AS row
CREATE (c:Client {
  customerId: row.`customerId:ID(Client)`,
  name: row.name,
  businessType: row.businessType,
  owner: row.owner,
  industry: row.industry,
  websiteUrl: row.websiteUrl,
  contactPhone: row.contactPhone,
  clientSize: row.clientSize,
  onboardingDate: row.onboardingDate,
  notes: row.notes
});
```

### Step 5: Create Indexes (Important for Performance)
```cypher
CREATE INDEX location_id FOR (l:Location) ON (l.locationId);
CREATE INDEX service_id FOR (s:Service) ON (s.serviceId);
CREATE INDEX keyword_id FOR (k:Keyword) ON (k.keywordId);
CREATE INDEX client_id FOR (c:Client) ON (c.customerId);
```

### Step 6: Import Relationships
```cypher
// Location NEAR relationships
LOAD CSV WITH HEADERS FROM 'file:///location_near_rels.csv' AS row
MATCH (l1:Location {locationId: row.`:START_ID(Location)`})
MATCH (l2:Location {locationId: row.`:END_ID(Location)`})
CREATE (l1)-[:NEAR]->(l2);

// Service HAS_KEYWORD relationships
LOAD CSV WITH HEADERS FROM 'file:///service_has_keyword_rels.csv' AS row
MATCH (s:Service {serviceId: row.`:START_ID(Service)`})
MATCH (k:Keyword {keywordId: row.`:END_ID(Keyword)`})
CREATE (s)-[:HAS_KEYWORD]->(k);

// Client HAS_MAIN_ADDRESS relationships
LOAD CSV WITH HEADERS FROM 'file:///client_main_address_rels.csv' AS row
MATCH (c:Client {customerId: row.`:START_ID(Client)`})
MATCH (l:Location {locationId: row.`:END_ID(Location)`})
CREATE (c)-[:HAS_MAIN_ADDRESS]->(l);

// Client SERVES_AREA relationships
LOAD CSV WITH HEADERS FROM 'file:///client_serves_area_rels.csv' AS row
MATCH (c:Client {customerId: row.`:START_ID(Client)`})
MATCH (l:Location {locationId: row.`:END_ID(Location)`})
CREATE (c)-[:SERVES_AREA]->(l);

// Client OFFERS_SERVICE relationships
LOAD CSV WITH HEADERS FROM 'file:///client_offers_service_rels.csv' AS row
MATCH (c:Client {customerId: row.`:START_ID(Client)`})
MATCH (s:Service {serviceId: row.`:END_ID(Service)`})
CREATE (c)-[:OFFERS_SERVICE]->(s);
```

---

## Verification Queries

After import, verify your data:

```cypher
// Count all nodes by label
MATCH (n) RETURN labels(n)[0] AS label, count(n) AS count;

// Count all relationships by type
MATCH ()-[r]->() RETURN type(r) AS relType, count(r) AS count;

// View client with most service areas
MATCH (c:Client)-[r:SERVES_AREA]->()
RETURN c.name, count(r) AS areaCount
ORDER BY areaCount DESC LIMIT 5;

// View services with most keywords
MATCH (s:Service)-[r:HAS_KEYWORD]->()
RETURN s.name, count(r) AS keywordCount
ORDER BY keywordCount DESC LIMIT 5;

// Find all services a specific client offers
MATCH (c:Client {name: 'Wells Asphalt Paving'})-[:OFFERS_SERVICE]->(s:Service)
RETURN s.name;

// Find keywords for a service
MATCH (s:Service {name: 'New Residential Asphalt Paving'})-[:HAS_KEYWORD]->(k:Keyword)
RETURN k.primaryKeyword, k.searchVolumeTier;

// Find nearby locations
MATCH (l:Location {name: 'Madison'})-[:NEAR]->(nearby:Location)
RETURN nearby.name, nearby.state;

// Find clients serving a specific location
MATCH (c:Client)-[:SERVES_AREA]->(l:Location {name: 'Waunakee'})
RETURN c.name, c.contactPhone;

// Full path: Client → Service → Keywords
MATCH (c:Client)-[:OFFERS_SERVICE]->(s:Service)-[:HAS_KEYWORD]->(k:Keyword)
WHERE c.name = 'Wells Asphalt Paving'
RETURN c.name, s.name, collect(k.primaryKeyword) AS keywords
LIMIT 10;
```

---

## Expected Import Results

After successful import:

| Label | Count |
|-------|-------|
| Location | 109 |
| Service | 51 |
| Keyword | 40 |
| Client | 6 |
| **Total Nodes** | **206** |

| Relationship | Count |
|--------------|-------|
| NEAR | 300 |
| OFFERS_SERVICE | 192 |
| HAS_KEYWORD | 115 |
| SERVES_AREA | 111 |
| HAS_MAIN_ADDRESS | 6 |
| **Total Relationships** | **724** |
