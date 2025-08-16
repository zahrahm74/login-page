(cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF'
diff --git a/test_simple.py b/test_simple.py
--- a/test_simple.py
 b/test_simple.py
@@ -0,0 1,26 @@
#!/usr/bin/env python3
"""
Simple test script to verify Flask application can start
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, db
    print("✅ Successfully imported Flask app and database")
    
    # Test database initialization
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully")
    
    print("✅ Flask application is ready to run!")
    print("🌐 You can start the server with: python app.py")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
EOF
)
