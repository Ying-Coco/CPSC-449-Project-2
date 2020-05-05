export PATH="$HOME/.local/bin:$PATH"

locust -f load_test.py --host=http://localhost:2015
