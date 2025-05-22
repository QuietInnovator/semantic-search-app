# 🔍 Semantic Search Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

A beautiful, interactive web application for semantic document search powered by AI. Find documents by meaning, not just keywords!

## ✨ Features

- **📊 Interactive Document Table**: Browse all documents in an organized, searchable table
- **🔍 AI-Powered Search**: Find documents using natural language queries
- **📈 Real-time Results**: Instant search with similarity scores and performance metrics
- **🎨 Beautiful UI**: Modern, responsive design with color-coded results
- **⚡ Fast Performance**: Optimized search algorithms with sub-second response times
- **🤖 Smart Fallback**: Works with or without AI dependencies

## 🚀 Live Demo

**[Try the app online →](https://your-app-url.streamlit.app)**

## 📱 Screenshots

### Main Interface
- **Left Panel**: Document collection table with statistics
- **Right Panel**: Search interface with real-time results
- **Color-coded results**: Green (high similarity), Yellow (medium), Red (low)

### Sample Queries
Try these example searches:
- `"artificial intelligence applications"`
- `"healthy lifestyle and wellness"`
- `"environmental conservation efforts"`
- `"digital technology innovation"`

## 🏗️ Local Development

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/semantic-search-app.git
cd semantic-search-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. **Open your browser** to `http://localhost:8501`

### With AI Dependencies (Recommended)
For full semantic search capabilities:
```bash
pip install -r requirements.txt
pip install faiss-cpu sentence-transformers
```

## 🌐 Online Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account

2. **Visit [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your GitHub** account

4. **Deploy the app**:
   - Repository: `yourusername/semantic-search-app`
   - Branch: `main`
   - Main file path: `app.py`

5. **Your app will be live** at `https://yourusername-semantic-search-app.streamlit.app`

### Alternative Deployment Options

#### Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
git push heroku main
```

#### Railway
```bash
# Connect GitHub repo at railway.app
# Auto-deploys on git push
```

#### Render
```bash
# Connect GitHub repo at render.com
# Auto-deploys on git push
```

## 📁 Project Structure

```
semantic-search-app/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── modules/
│   ├── __init__.py
│   ├── config.py          # App configuration
│   ├── search_engine.py   # Search functionality
│   ├── sample_data.py     # Sample documents
│   └── utils.py           # Utility functions
└── assets/
    └── sample_documents.json  # Document dataset
```

## ⚙️ Configuration

### Environment Variables
Set these for production deployment:

- `STREAMLIT_SERVER_PORT`: Port number (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: localhost)
- `MODEL_NAME`: AI model to use (default: all-MiniLM-L6-v2)

### Streamlit Configuration
Edit `.streamlit/config.toml` for custom settings:

```toml
[server]
port = 8501
enableCORS = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#000080"
```

## 🔧 Technical Details

### AI Models
- **Default**: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- **Alternative**: `all-mpnet-base-v2` (768-dimensional, higher quality)
- **Fallback**: Keyword search when AI unavailable

### Performance
- **Search Time**: ~1-10ms per query
- **Model Loading**: ~2-5 seconds (first time only)
- **Memory Usage**: ~100MB for model + embeddings

### Dependencies
- **Core**: Streamlit, Pandas, NumPy
- **AI**: FAISS, Sentence Transformers
- **Optional**: Plotly (for visualizations)

## 📊 Sample Data

The app includes 16 sample documents covering:
- **Technology**: AI, cloud computing, digital transformation
- **Health**: Exercise, nutrition, wellness
- **Education**: Online learning, critical thinking
- **Environment**: Conservation, sustainability
- **Culture**: Music, literature, cultural exchange

## 🎯 Usage Examples

### Basic Search
```python
# In the web interface:
Query: "machine learning"
Results: Documents about AI, algorithms, data processing
```

### Semantic Understanding
```python
# These queries find similar results:
"artificial intelligence" ≈ "machine learning" ≈ "AI algorithms"
"healthy living" ≈ "wellness tips" ≈ "fitness advice"
```

## 🔮 Future Enhancements

- [ ] **File Upload**: Allow users to upload their own documents
- [ ] **Multiple Languages**: Support for multilingual search
- [ ] **Advanced Filters**: Filter by document type, date, etc.
- [ ] **User Accounts**: Save search history and preferences
- [ ] **API Endpoint**: REST API for programmatic access
- [ ] **Batch Processing**: Upload and search large document collections

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Common Issues

**"AI components not found"**
- Install: `pip install faiss-cpu sentence-transformers`
- Or use in keyword search mode

**"Slow first search"**
- First run downloads AI model (~100MB)
- Subsequent searches are fast

**"No results found"**
- Try broader search terms
- Use synonyms or related words
- Check spelling

### Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/semantic-search-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/semantic-search-app/discussions)
- **Email**: your-email@domain.com

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **Sentence Transformers** for semantic embeddings
- **FAISS** for efficient vector search
- **Hugging Face** for pre-trained models

---

**Made with ❤️ and AI**

**⭐ Star this repo if you find it useful!**
