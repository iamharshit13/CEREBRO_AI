# Simple worker stub - replace with Celery or RQ for production
import time

def main():
    print('Worker started (stub). Listening for jobs...')
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print('Worker stopped.')

if __name__ == '__main__':
    main()
