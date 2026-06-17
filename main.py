import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_processor import DataProcessor
from src.topic_detector import TopicDetector
from src.rag_system import RAGSystem
from src.persona_extractor import PersonaExtractor
from src.chatbot import PersonaChatbot

def main():
    print("=== Conversation RAG System with Persona Extraction ===\n")

    print("Step 1: Loading conversations...")
    processor = DataProcessor("data/conversations.csv")
    messages = processor.load_and_process()
    print(f"✓ Loaded {len(messages)} messages\n")

    print("Step 2: Detecting topics...")
    detector = TopicDetector()
    topic_segments = detector.detect_topics(messages)
    print(f"✓ Found {len(topic_segments)} topic segments\n")

    print("Step 3: Building RAG system with checkpoints...")
    rag = RAGSystem()
    rag.build(messages, topic_segments)
    print("✓ RAG system ready\n")

    print("Step 4: Extracting user persona...")
    extractor = PersonaExtractor()
    persona = extractor.extract(messages)
    print("✓ Persona extracted\n")

    print("Step 5: Starting chatbot...\n")
    chatbot = PersonaChatbot(rag, persona)
    chatbot.run()

if __name__ == "__main__":
    main()
