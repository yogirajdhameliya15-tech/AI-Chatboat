def chatbot():
    print("🤖 Welcome to TechBot - Your IT & Python Assistant!")
    print("I can help with Python programming, IT concepts, and technology trends.")
    print("Type 'exit' to quit, 'help' for assistance, or 'topics' to see what I can discuss.")
    
    while True:
        user_input = input("\nYou: ").strip().lower()
        
        if user_input == 'exit':
            print("TechBot: Goodbye! Stay curious and keep learning! 👋")
            break
            
        elif user_input == 'help':
            print("TechBot: I can discuss:")
            print("- Python programming basics and advanced topics")
            print("- IT fundamentals and concepts")
            print("- Current technology trends and innovations")
            print("- Career advice in tech")
            print("Ask me anything related to these areas!")
            
        elif user_input == 'topics':
            print("TechBot: Here are the topics I can help with:")
            print("🔹 Python: syntax, libraries, frameworks, best practices")
            print("🔹 IT: networking, security, cloud computing, databases")
            print("🔹 Trends: AI/ML, cloud, cybersecurity, blockchain, IoT")
            print("🔹 Careers: skills, job market, learning paths")
            
        # Python-related questions
        elif any(word in user_input for word in ['python', 'pyton', 'pythn']):
            if "what is python" in user_input:
                print("TechBot: Python is a high-level, interpreted programming language known for its readability and simplicity. Created by Guido van Rossum in 1991, it's widely used in web development, data science, AI, and automation.")
                
            elif "python version" in user_input or "which python" in user_input:
                print("TechBot: Python 3.x is the current version (Python 2 reached end-of-life in 2020). Latest stable version is Python 3.12. Always use Python 3 for new projects!")
                
            elif "python frameworks" in user_input or "python web framework" in user_input:
                print("TechBot: Popular Python frameworks:")
                print("- Web: Django (batteries included), Flask (microframework), FastAPI (ASGI)")
                print("- Data Science: Pandas, NumPy, SciPy, Scikit-learn")
                print("- Testing: pytest, unittest")
                print("- Async: Asyncio, Trio")
                
            elif "python data types" in user_input:
                print("TechBot: Python has several built-in data types:")
                print("- Numeric: int, float, complex")
                print("- Sequence: list, tuple, range")
                print("- Text: str")
                print("- Mapping: dict")
                print("- Set: set, frozenset")
                print("- Boolean: bool")
                print("- Binary: bytes, bytearray, memoryview")
                
            elif "python library" in user_input or "python package" in user_input:
                print("TechBot: Essential Python libraries:")
                print("- Data: pandas, numpy, matplotlib, seaborn")
                print("- Web: requests, beautifulsoup, selenium")
                print("- ML: scikit-learn, tensorflow, pytorch")
                print("- DevOps: docker, kubernetes, ansible")
                
            elif "python oop" in user_input or "object oriented" in user_input:
                print("TechBot: Python OOP concepts:")
                print("- Classes and Objects")
                print("- Inheritance (single, multiple, multilevel)")
                print("- Polymorphism (method overriding, duck typing)")
                print("- Encapsulation (public, protected, private)")
                print("- Abstraction (ABC modules)")
                
            else:
                print("TechBot: Python is a versatile language! Ask me about specific Python topics like: syntax, libraries, frameworks, or best practices.")
        
        # IT-related questions
        elif any(word in user_input for word in ['it', 'information technology', 'computer']):
            if "what is it" in user_input:
                print("TechBot: Information Technology (IT) involves using computers, storage, networking, and other physical devices to create, process, store, secure, and exchange electronic data.")
                
            elif "cloud computing" in user_input:
                print("TechBot: Cloud computing delivers computing services over the internet. Main models:")
                print("- IaaS (Infrastructure as a Service): AWS, Azure, GCP")
                print("- PaaS (Platform as a Service): Heroku, Google App Engine")
                print("- SaaS (Software as a Service): Google Workspace, Microsoft 365")
                
            elif "networking" in user_input or "tcp/ip" in user_input:
                print("TechBot: Networking fundamentals:")
                print("- OSI Model: 7 layers (Physical to Application)")
                print("- TCP/IP: Foundation of internet communication")
                print("- Protocols: HTTP/HTTPS, FTP, SSH, DNS")
                print("- IP Addressing: IPv4 vs IPv6")
                
            elif "cybersecurity" in user_input or "security" in user_input:
                print("TechBot: Cybersecurity protects systems from digital attacks. Key areas:")
                print("- Network security")
                print("- Application security")
                print("- Endpoint security")
                print("- Data security")
                print("- Identity management")
                
            elif "database" in user_input or "sql" in user_input:
                print("TechBot: Database types:")
                print("- SQL (Relational): MySQL, PostgreSQL, SQL Server")
                print("- NoSQL: MongoDB (document), Redis (key-value), Cassandra (column)")
                print("- NewSQL: CockroachDB, Google Spanner")
                
            else:
                print("TechBot: IT covers many areas! Ask about cloud, networking, security, databases, or DevOps.")
        
        # Technology trends
        elif any(word in user_input for word in ['trend', 'new', 'latest', 'ai', 'ml', 'blockchain', 'iot']):
            if "ai" in user_input or "artificial intelligence" in user_input:
                print("TechBot: AI trends 2024:")
                print("- Generative AI (ChatGPT, DALL-E, Midjourney)")
                print("- AI ethics and responsible AI")
                print("- Edge AI (on-device processing)")
                print("- AI in healthcare and finance")
                
            elif "ml" in user_input or "machine learning" in user_input:
                print("TechBot: Machine Learning trends:")
                print("- Large Language Models (LLMs)")
                print("- Automated Machine Learning (AutoML)")
                print("- Reinforcement Learning")
                print("- MLOps (ML operations)")
                
            elif "cloud trends" in user_input or "cloud computing trends" in user_input:
                print("TechBot: Cloud trends 2024:")
                print("- Multi-cloud and hybrid cloud strategies")
                print("- Serverless computing")
                print("- Edge computing")
                print("- Cloud security and compliance")
                
            elif "blockchain" in user_input or "crypto" in user_input:
                print("TechBot: Blockchain beyond cryptocurrency:")
                print("- Smart contracts")
                print("- DeFi (Decentralized Finance)")
                print("- NFTs and digital ownership")
                print("- Supply chain transparency")
                
            elif "iot" in user_input or "internet of things" in user_input:
                print("TechBot: IoT trends:")
                print("- Smart cities and homes")
                print("- Industrial IoT (IIoT)")
                print("- 5G enabling faster IoT")
                print("- Edge computing for IoT")
                
            else:
                print("TechBot: Current tech trends include AI/ML, cloud computing, cybersecurity, blockchain, IoT, and quantum computing.")
        
        # Career and learning questions
        elif any(word in user_input for word in ['career', 'job', 'learn', 'study', 'skill']):
            if "python career" in user_input or "python job" in user_input:
                print("TechBot: Python career paths:")
                print("- Data Scientist/Analyst")
                print("- Python Developer")
                print("- DevOps Engineer")
                print("- Machine Learning Engineer")
                print("- Backend Developer")
                
            elif "it career" in user_input or "tech career" in user_input:
                print("TechBot: IT career options:")
                print("- Software Developer")
                print("- Network Engineer")
                print("- Cybersecurity Analyst")
                print("- Cloud Architect")
                print("- Data Engineer")
                
            elif "learn python" in user_input or "python beginners" in user_input:
                print("TechBot: Python learning path:")
                print("1. Python basics (syntax, data types)")
                print("2. Control flow (loops, conditionals)")
                print("3. Functions and modules")
                print("4. OOP concepts")
                print("5. Popular libraries (requests, pandas)")
                print("6. Build projects!")
                
            elif "tech skills" in user_input or "in demand skills" in user_input:
                print("TechBot: In-demand tech skills 2024:")
                print("- Python/JavaScript/Go")
                print("- Cloud platforms (AWS/Azure/GCP)")
                print("- DevOps tools (Docker, Kubernetes)")
                print("- AI/ML technologies")
                print("- Cybersecurity skills")
                
            else:
                print("TechBot: Tech careers are booming! Ask about specific roles, skills, or learning paths.")
        
        # General greetings and small talk
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
            print("TechBot: Hello! 👋 How can I help you with Python, IT, or technology today?")
            
        elif any(word in user_input for word in ['how are you', 'how you doing']):
            print("TechBot: I'm running smoothly like well-optimized code! 💻 Ready to help with your tech questions.")
            
        elif any(word in user_input for word in ['thanks', 'thank you', 'appreciate']):
            print("TechBot: You're welcome! Happy to help. 😊")
            
        elif any(word in user_input for word in ['who are you', 'what are you']):
            print("TechBot: I'm TechBot, a rule-based chatbot designed to help with Python programming, IT concepts, and technology trends!")
        
        # Fallback response
        else:
            print("TechBot: I'm not sure I understand. Try asking about:")
            print("- Python programming concepts")
            print("- IT fundamentals and technologies")
            print("- Current tech trends and innovations")
            print("- Career advice in technology")
            print("Or type 'help' for more options.")

if __name__ == "__main__":
    chatbot()
