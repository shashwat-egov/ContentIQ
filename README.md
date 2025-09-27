# ContentIQ

**AI-Powered Content Discovery for Technical Professionals**

ContentIQ is an intelligent content discovery tool that helps software engineers stay ahead of the curve by identifying trending topics in technology, AI, data engineering, and software development. Built with LangChain and powered by advanced AI reasoning, it provides actionable insights for building your professional brand on LinkedIn.

## Features

- **Trending Topic Discovery**: Automatically finds 3 high-engagement topics currently trending in tech communities
- **Smart Analysis**: Explains why each topic is gaining traction and its relevance to technical professionals
- **Content Strategy**: Suggests specific angles for writing engaging LinkedIn posts
- **AI-Powered Research**: Uses ReAct (Reasoning + Acting) agents with real-time web search capabilities
- **Structured Output**: Provides well-formatted responses with source attribution
- **Professional Focus**: Tailored specifically for Senior Software Engineers and Technical Leads

## Quick Start

### Prerequisites

- Python 3.13 or higher
- OpenAI API key
- Tavily API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langchain-react-search-agent
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

### Usage

Run ContentIQ to discover trending topics:

```bash
python main.py
```

## Sample Output

ContentIQ provides structured responses like this:

```json
{
  "answer": "Here are 3 trending topics in technology and software development:\n\n1. **AI Code Generation Tools Evolution**\n   Why it's trending: Recent advances in AI coding assistants...\n   LinkedIn angle: Share your experience comparing different AI coding tools...\n\n2. **Platform Engineering Best Practices**\n   Why it's trending: Companies are investing heavily in platform teams...\n   LinkedIn angle: Write about your journey implementing platform engineering...\n\n3. **WebAssembly in Production**\n   Why it's trending: Major tech companies are adopting WASM for performance...\n   LinkedIn angle: Create a technical deep-dive on WASM benefits...",
  "sources": [
    {"url": "https://reddit.com/r/programming/..."},
    {"url": "https://news.ycombinator.com/..."}
  ]
}
```

## Architecture

ContentIQ is built on a modern AI agent architecture:

```
+----------------+    +------------------+    +-----------------+
|   User Query   |--->|   ReAct Agent    |--->|  Tavily Search  |
+----------------+    +------------------+    +-----------------+
                               |
                               v
+----------------+    +------------------+    +-----------------+
| Structured     |<---|   GPT-4 Model    |<---|  Custom Prompts |
| Response       |    +------------------+    +-----------------+
+----------------+
```

### Key Components

- **ReAct Agent**: Implements reasoning and acting cycles for systematic problem-solving
- **LangChain Framework**: Provides the foundation for building AI agents and chains
- **Tavily Search**: Performs real-time web searches for current trending topics
- **Pydantic Schemas**: Ensures structured, validated output
- **Custom Prompts**: Optimized for finding technical content relevant to software professionals

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for GPT-4 access | Yes |
| `TAVILY_API_KEY` | Your Tavily API key for web search | Yes |

### Customization

You can modify the search query in `main.py` to focus on different:
- **Industries**: Add healthcare, fintech, e-commerce, etc.
- **Roles**: Target different seniority levels or specializations
- **Platforms**: Include Twitter, GitHub discussions, Stack Overflow trends
- **Content Types**: Focus on tools, frameworks, methodologies, etc.

Example customization:
```python
result = chain.invoke(
    input={
        "input": "Find 3 trending topics in cloud-native technologies and DevOps that would be valuable for Platform Engineers to write about on LinkedIn..."
    }
)
```

## Development

### Project Structure

```
langchain-react-search-agent/
├── main.py           # Main application and agent setup
├── schemas.py        # Pydantic models for structured output
├── prompt.py         # Custom ReAct prompt templates
├── pyproject.toml    # Project configuration and dependencies
├── .env             # Environment variables (not in git)
└── README.md        # This file
```

### Dependencies

- **langchain**: Core framework for building AI applications
- **langchain-openai**: OpenAI integration for LangChain
- **langchain-tavily**: Tavily search integration
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation and settings management

### Code Quality

The project includes formatting and linting tools:
- **black**: Code formatting
- **isort**: Import sorting

Run formatting:
```bash
black .
isort .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines

- Follow the existing code style (black + isort)
- Add type hints for new functions
- Update documentation for significant changes
- Test your changes thoroughly

## Use Cases

ContentIQ is perfect for:

- **Technical Content Creators**: Stay on top of trending topics for blog posts and articles
- **Developer Relations**: Identify community interests for conference talks and content
- **Engineering Managers**: Understand what technologies your team should be exploring
- **Personal Branding**: Build thought leadership by writing about relevant, timely topics
- **Learning & Development**: Discover emerging technologies worth investing time in

## Roadmap

- [ ] Support for multiple social platforms (Twitter, Dev.to, Medium)
- [ ] Custom topic filtering and preferences
- [ ] Historical trend analysis
- [ ] Integration with calendar scheduling for content planning
- [ ] Sentiment analysis for topic viability
- [ ] Team collaboration features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions, suggestions, or contributions, please open an issue on GitHub or reach out to the maintainers.

---

**Built with LangChain, OpenAI, and Tavily**
