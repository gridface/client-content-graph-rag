### Ontological GraphRag Content Generation

### Codename: Oliver

The purpose of this application is to generate high quality, extremely accurate content for construction and trades based clients.

### Initial Business Use Case:

In order to meet the ever increasing demands of markeing SEO, it is necessary to create a content creation system that can perform the function of a highly accurate expert system while reaching client customers down to the neighborhood level by addressing real world questions and making the content relevant to their local areas. 

Two problems arise when attempting to create content of this nature, at the quality and quantity requirements demanded by local Search Engines.

1. Finding a human who can not only write these articles at a high output, but with SEO quality, high technical accuracy, and keen location awareness

2. The problem clearly demands automation in order to create content that can be found by their customers. Basic prompts that generate blogs on the "free tier" of chat AI services then to be generic, unpredictable in SEO format, and unreliable in technical detail.

### The Solution

The solution Oliver provides is to create a source of truth for a particular technical domain (in the current case, it is Asphalt Paving Contracting) and tie it to Client detail that includes their service areas covered, services offered, and company details. 

This source of truth, coupled with highly detailed SEO instructions for content creation, along with verification checks of all "first draft" material provides extremely high quality content that is both useful to customers and highly accurate in its domain. From a marketing standpoint, this creates high Domain Authority SEO scores to my clients' online presence.

### The Current Challenge

This process is expensive. In order to create the existing sources of truth, it took many hours (and tokens) worth of coding and processing time across two LLM systems (Claude and Perplexity).

In order to generate each new blog or web page, the token cost alone is between $1-$3, and it takes about 20 minutes, not including the maintenance involved in managing the source content. Blogs written on the free tier of claude can be written in less than 5 minutes for free. 

The system created is fairly technical, and hiring someone to manage the genertion process quickly becomes unscalable.

### The Future

The next phase will be to turn the current graph system into a proper graph database in neo4j, using GraphQL to optimize my queries. Natural language (English) prompts are a luxury that do not provide scale or accuracy. 

The existing RAG solution, which is an asphalt textbook, needs to be vectorized in pinecone in order to cut costs and increase functionality

### Wheres the UI?

Once the workflow is created and the databases are in place, I will be creating a UI front end that will allow end users to select queries, update client information, and upload and tag media.


### How to navigate this material

This is a work in progress and is quite messy. The best place to start is with the blog-prompt-orchestrator.md file found in the prompts --> blog-post-testing-prompts directory. That will point you to the relevant yaml files and the textbook that is found in the graph-sources nd the rag-sources directories
