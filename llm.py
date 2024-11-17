from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


TEMPLATE = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **Empty Response:** If no information matches the description, return an empty string ('')."
    "3. **Improve the text, if necessary:** Make any necessary adjustments to the input text to improve the accuracy of the extracted information."
)

class ChatModel:
    def __init__(self, google_api_key: str) -> None:
        self.llm = ChatGoogleGenerativeAI(
            api_key=google_api_key,
            model="gemini-1.5-flash"
        )

    def get_document_contents(self, raw_content: str, user_prompt: str, chunk_size: int) -> str:
        dom_chunks = split_dom_content(raw_content, chunk_size)
        return self.generatePrompt(dom_chunks, user_prompt)
        

    def generatePrompt(self, info_chunks: list[str], parse_description: str) -> str:
        prompt = ChatPromptTemplate.from_template(TEMPLATE)
        chain = prompt | self.llm

        parsed_results = []

        for i, chunk in enumerate(info_chunks, start=1):
            response = chain.invoke({
                "dom_content": chunk,
                "parse_description": parse_description,
            })
            print(f"Parsed batch: {i} of {len(info_chunks)}")
            parsed_results.append(response.content)

        print(parsed_results)

        return "\n".join(parsed_results)

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]