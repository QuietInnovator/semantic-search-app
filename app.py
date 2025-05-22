import streamlit as st
import pandas as pd
import time
import json
from typing import List, Tuple

# Configure Streamlit page
st.set_page_config(
    page_title="Semantic Search Engine",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .result-card {
        background-color: #f8f9fa;
        border-left: 4px solid #1f77b4;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
        color: #000080;
    }
    .result-card div {
        color: #000080;
    }
    .similarity-score {
        font-weight: bold;
    }
    .metric-card {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        height: 3rem;
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_documents():
    """Load sample documents for the search engine."""
    return [
        "Artificial intelligence is transforming how we work and live",
        "Machine learning algorithms can process large datasets efficiently",
        "Cloud computing provides on-demand access to computing resources",
        "Renewable energy technologies are crucial for environmental sustainability",
        "Digital transformation is reshaping traditional business models",
        "Customer experience drives competitive advantage in modern markets",
        "Regular exercise promotes cardiovascular health and mental wellbeing",
        "Balanced nutrition provides essential nutrients for optimal health",
        "Online learning platforms make education accessible to global audiences",
        "Critical thinking skills are essential for academic and professional success",
        "Music therapy can improve mental health and emotional wellbeing",
        "Literature reflects and shapes cultural values and perspectives",
        "Conservation efforts protect endangered species and their habitats",
        "Sustainable practices reduce environmental impact and resource consumption",
        "Cultural exchange programs promote international understanding",
        "Geographic information systems help analyze spatial data and patterns",
        "Blockchain technology enables secure and decentralized transactions",
        "Virtual reality creates immersive educational and entertainment experiences",
        "Cybersecurity measures protect digital assets from online threats",
        "Data analytics reveals insights for informed decision making"
    ]

@st.cache_resource
def initialize_search_engine():
    """Initialize the semantic search engine."""
    try:
        # Import here to handle missing dependencies gracefully
        import numpy as np
        import faiss
        from sentence_transformers import SentenceTransformer
        
        documents = load_sample_documents()
        
        with st.spinner("🤖 Loading AI model and building search index..."):
            # Load the sentence transformer model
            model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # Generate embeddings for all documents
            embeddings = model.encode(documents)
            
            # Build FAISS index
            dimension = embeddings.shape[1]
            index = faiss.IndexFlatL2(dimension)
            index.add(embeddings.astype('float32'))
            
            return {
                'model': model,
                'index': index,
                'documents': documents,
                'embeddings': embeddings
            }, True
            
    except ImportError as e:
        st.error(f"AI dependencies not available: {e}")
        st.info("The app will run in keyword search mode. For full semantic search, install: `pip install faiss-cpu sentence-transformers`")
        return None, False
    except Exception as e:
        st.error(f"Failed to initialize search engine: {e}")
        return None, False

def semantic_search(engine, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
    """Perform semantic search using the AI engine."""
    if not engine:
        return []
    
    try:
        # Generate query embedding
        query_embedding = engine['model'].encode([query])
        
        # Search the index
        distances, indices = engine['index'].search(query_embedding.astype('float32'), top_k)
        
        # Convert to results with similarity scores
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            if idx < len(engine['documents']):
                similarity = 1 / (1 + distance)  # Convert distance to similarity
                results.append((engine['documents'][idx], similarity))
        
        return results
    except Exception as e:
        st.error(f"Search failed: {e}")
        return []

def keyword_search(documents: List[str], query: str, top_k: int = 5) -> List[Tuple[str, float]]:
    """Fallback keyword search when AI is not available."""
    if not query:
        return []
    
    query_words = set(query.lower().split())
    results = []
    
    for doc in documents:
        doc_words = set(doc.lower().split())
        overlap = len(query_words.intersection(doc_words))
        if overlap > 0:
            similarity = overlap / len(query_words.union(doc_words))
            results.append((doc, similarity))
    
    return sorted(results, key=lambda x: x[1], reverse=True)[:top_k]

def highlight_query_terms(text: str, query: str) -> str:
    """Highlight query terms in text."""
    if not query:
        return text
    
    words = query.lower().split()
    highlighted = text
    
    for word in words:
        if len(word) > 2:
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            highlighted = pattern.sub(
                f"<strong style='color: #000080; background-color: #e6f3ff;'>{word.upper()}</strong>", 
                highlighted
            )
    
    return highlighted

def create_document_table(documents: List[str]) -> pd.DataFrame:
    """Create a pandas DataFrame from documents."""
    df = pd.DataFrame({
        'ID': range(1, len(documents) + 1),
        'Document': documents,
        'Length': [len(doc) for doc in documents],
        'Words': [len(doc.split()) for doc in documents]
    })
    return df

def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<h1 class="main-header">🔍 Semantic Search Engine</h1>', unsafe_allow_html=True)
    st.markdown("**Find documents by meaning, not just keywords**")
    
    # Load documents and initialize search engine
    documents = load_sample_documents()
    engine, ai_available = initialize_search_engine()
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Search settings
        top_k = st.slider("Number of results", 1, 10, 5)
        
        # Dataset info
        st.subheader("📊 Dataset Info")
        st.metric("Total Documents", len(documents))
        st.metric("Total Words", sum(len(doc.split()) for doc in documents))
        
        # Model info
        if ai_available:
            st.success("✅ AI Search Engine Ready")
            st.info("Using: all-MiniLM-L6-v2")
        else:
            st.warning("⚠️ Keyword Search Only")
            st.info("Install AI dependencies for semantic search")
        
        st.markdown("---")
        
        # Instructions
        st.subheader("💡 How to Use")
        st.markdown("""
        1. **Browse documents** in the table below
        2. **Enter your search query** in natural language
        3. **View results** ranked by semantic similarity
        
        **Example queries:**
        - "machine learning and AI"
        - "healthy lifestyle tips"
        - "environmental conservation"
        - "digital technology trends"
        """)
        
        # GitHub link
        st.markdown("---")
        st.markdown("### 🔗 Links")
        st.markdown("[📖 Documentation](https://github.com/yourusername/semantic-search-app)")
        st.markdown("[🐛 Report Issues](https://github.com/yourusername/semantic-search-app/issues)")
        
        # Performance info
        if 'search_time' in st.session_state:
            st.subheader("⚡ Performance")
            st.metric("Last Search Time", f"{st.session_state.search_time:.2f}ms")

    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Document Collection")
        
        # Create and display document table
        df = create_document_table(documents)
        
        # Display table
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "ID": st.column_config.NumberColumn("ID", width="small"),
                "Document": st.column_config.TextColumn("Document Content"),
                "Length": st.column_config.NumberColumn("Chars", width="small"),
                "Words": st.column_config.NumberColumn("Words", width="small")
            }
        )
        
    with col2:
        st.subheader("🔍 Search Interface")
        
        # Search input
        query = st.text_input(
            "Enter your search query:",
            placeholder="e.g., artificial intelligence applications",
            help="Describe what you're looking for in natural language"
        )
        
        # Search button
        search_clicked = st.button("🚀 Search", type="primary")
        
        # Perform search when button clicked or query entered
        if (search_clicked or query) and query:
            start_time = time.time()
            
            # Perform search
            if ai_available and engine:
                results = semantic_search(engine, query, top_k)
            else:
                results = keyword_search(documents, query, top_k)
            
            search_time = (time.time() - start_time) * 1000
            st.session_state.search_time = search_time
            
            # Display results
            if results:
                st.success(f"Found {len(results)} results in {search_time:.1f}ms")
                
                for i, (document, similarity) in enumerate(results, 1):
                    # Color code based on similarity score
                    if similarity > 0.7:
                        color = "#28a745"  # Green
                        icon = "🟢"
                    elif similarity > 0.5:
                        color = "#ffc107"  # Yellow
                        icon = "🟡"
                    else:
                        color = "#dc3545"  # Red
                        icon = "🔴"
                    
                    # Create result card
                    with st.container():
                        st.markdown(f"""
                        <div class="result-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <strong style="color: #000080;">{icon} Result #{i}</strong>
                                <span class="similarity-score" style="color: {color};">
                                    {similarity:.3f} ({similarity*100:.1f}%)
                                </span>
                            </div>
                            <div style="line-height: 1.6; color: #000080;">
                                {highlight_query_terms(document, query)}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("No results found. Try a different query.")
                st.info("**Suggestions:**\n- Try broader terms\n- Use synonyms\n- Check spelling")
    
    # Footer section
    st.markdown("---")
    
    # Statistics dashboard
    if query and 'search_time' in st.session_state:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Query Length", f"{len(query)} chars")
        
        with col2:
            st.metric("Search Time", f"{st.session_state.search_time:.1f}ms")
        
        with col3:
            if 'results' in locals():
                st.metric("Results Found", len(results))
            else:
                st.metric("Results Found", 0)
        
        with col4:
            if ai_available:
                st.metric("Search Type", "AI Semantic")
            else:
                st.metric("Search Type", "Keyword")
    
    # About section
    with st.expander("ℹ️ About Semantic Search"):
        st.markdown("""
        **Semantic Search** finds documents based on meaning and context, not just keyword matching.
        
        **How it works:**
        1. **Text Analysis**: Documents are converted into numerical vectors that capture semantic meaning
        2. **AI Understanding**: Similar concepts have similar vector representations
        3. **Smart Matching**: Finds relevant content even with different wording
        
        **Example**: Searching for "happy dog" might find documents about "joyful puppy" or "cheerful canine"
        
        **Benefits:**
        - Understands context and meaning
        - Finds relevant results with different wording
        - Handles synonyms and related concepts
        - More intuitive than keyword search
        
        **Powered by:**
        - **Sentence Transformers** for text embeddings
        - **FAISS** for efficient vector search
        - **Streamlit** for the web interface
        """)

if __name__ == "__main__":
    main()
