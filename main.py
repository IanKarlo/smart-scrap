import os
from dotenv import load_dotenv
from ui import start_streamlit_app

load_dotenv()

def main():
    BRITHG_DATA_DRIVER_PATH = os.getenv('BRIGHTDATA_DRIVER_PATH')
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 6000))
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    start_streamlit_app(
        chrome_driver_path=CHROMEDRIVER_PATH,
        bright_data_driver_path=BRITHG_DATA_DRIVER_PATH,
        chunk_size=CHUNK_SIZE,
        gemini_api_key=GEMINI_API_KEY
    )

if __name__ == '__main__':
    main()