import time
import json
from tools import execute_code

# Add retry logic to execute_code function
def execute_with_retry(code, language='python', retries=3, delay=5):
    for attempt in range(retries):
        try:
            return execute_code(code, language)
        except Exception as e:
            if '429' in str(e):
                print(f'Rate limited - retrying in {delay} seconds...')
                time.sleep(delay)
            else:
                raise
    return {'error': 'Max retries exceeded'}

# Test the new function
if __name__ == '__main__':
    result = execute_with_retry('print("Testing rate limit retry")')
    print(result)