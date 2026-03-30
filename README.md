# Final Project

1. Automated News Aggregator
2. CI/CD with Gitlab

Automated News Aggregator Container Diagram

```mermaid
graph TB
    subgraph "Automated News Aggregator System"
        subgraph "Application Layer"
            CLI["Terminal CLI
            [Container: Python/Shell]
            Provides command-line interface
            for users to view and search
            aggregated news"]
            
            Service["News Service
            [Container: Python]
            Business logic layer that
            handles data access, search,
            and filtering operations"]
            
            Scraper["News Scraper
            [Container: Python]
            Scrapes news from multiple
            sources using web scraping
            libraries (BeautifulSoup, Scrapy)"]
            
            Summarizer["News Summarizer
            [Container: Python]
            Generates summaries using
            local NLP techniques
            (spaCy, NLTK, extractive methods)"]
            
            Scheduler["Cron Scheduler
            [Container: Cron Job]
            Triggers scraper every hour
            to fetch latest news"]
        end
        
        subgraph "Data Layer"
            DB["Local Database
            [Container: SQLite]
            Stores news articles,
            summaries, sources, and
            metadata in a single file"]
        end
    end
    
    subgraph "External Systems"
        NewsAPI["News APIs
        [External System]
        NewsAPI, RSS feeds"]
        
        NewsSites["News Websites
        [External System]
        CNN, BBC, Reuters,
        TechCrunch, etc."]
    end
    
    User["User
    [Person]
    Reads aggregated and
    summarized news via terminal"]
    
    %% Relationships
    User -->|Views news, searches| CLI
    CLI -->|Requests news data| Service
    Service -->|Queries database| DB
    
    Scheduler -->|Triggers hourly| Scraper
    
    Scraper -->|Fetches news via HTTP| NewsAPI
    Scraper -->|Scrapes content via HTTP| NewsSites
    Service -->|Writes to| DB
    Scraper -->|Sends articles for processing| Summarizer
    
    Summarizer -->|Saves summaries via| Service
    
    style CLI fill:#85C1E9,color:#000
    style Service fill:#85C1E9,color:#000
    style Scraper fill:#85C1E9,color:#000
    style Summarizer fill:#85C1E9,color:#000
    style Scheduler fill:#F8B400,color:#000
    style DB fill:#58D68D,color:#000
    style NewsAPI fill:#E8DAEF,color:#000
    style NewsSites fill:#E8DAEF,color:#000
    style User fill:#FAD7A0,color:#000
    
    classDef container fill:#85C1E9,stroke:#2874A6,stroke-width:2px,color:#000
    classDef database fill:#58D68D,stroke:#229954,stroke-width:2px,color:#000
    classDef external fill:#E8DAEF,stroke:#7D3C98,stroke-width:2px,color:#000
    classDef person fill:#FAD7A0,stroke:#E67E22,stroke-width:2px,color:#000
```

