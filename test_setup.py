#!/usr/bin/env python3
"""
Test script to verify chatbot setup
"""

def test_imports():
    """Test if all required packages can be imported"""
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        from azure.ai.inference import ChatCompletionsClient
        from azure.ai.inference.models import SystemMessage, UserMessage
        from azure.core.credentials import AzureKeyCredential
        print("✅ Azure AI imports successful")
    except ImportError as e:
        print(f"❌ Azure AI imports failed: {e}")
        return False
    
    try:
        from config import GITHUB_ENDPOINT, GITHUB_MODEL, GITHUB_TOKEN
        print("✅ Config imports successful")
    except ImportError as e:
        print(f"❌ Config imports failed: {e}")
        return False
    
    return True

def test_config():
    """Test if configuration is properly set"""
    try:
        from config import GITHUB_ENDPOINT, GITHUB_MODEL, GITHUB_TOKEN
        
        print(f"🔗 Endpoint: {GITHUB_ENDPOINT}")
        print(f"🤖 Model: {GITHUB_MODEL}")
        print(f"🔑 Token: {GITHUB_TOKEN[:10]}...")
        
        if GITHUB_TOKEN and GITHUB_TOKEN != "your_token_here":
            print("✅ Configuration looks good")
            return True
        else:
            print("❌ Please update your GitHub token in config.py")
            return False
            
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

def test_flask_app():
    """Test if Flask app can be created"""
    try:
        from app import app
        print("✅ Flask app created successfully")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Chatbot Setup...\n")
    
    tests = [
        ("Import Test", test_imports),
        ("Config Test", test_config),
        ("Flask App Test", test_flask_app)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"📋 {test_name}:")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your chatbot is ready to run.")
        print("💡 Run 'python app.py' to start the chatbot")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main() 