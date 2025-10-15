# Vision OCR Agent

An intelligent invoice processing system that combines OCR capabilities with conversational AI to extract, structure, and analyze invoice data.

## Overview

This project implements a complete invoice processing pipeline that:
- Extracts text from invoice images using Mistral AI's vision model
- Converts unstructured text into structured JSON format
- Enables natural language conversations about invoice data using Google's Gemini AI
- Provides an interactive chat interface for invoice analysis

## Features

- **Advanced OCR**: Utilizes Mistral's `pixtral-large-latest` model for accurate text extraction from invoice images
- **Smart Data Structuring**: Automatically organizes extracted data into JSON format with key invoice fields
- **AI-Powered Chat**: Ask questions about invoices in natural language and get intelligent responses
- **Multi-Format Support**: Handles JPG, JPEG, PNG, and WEBP image formats
- **Interactive Mode**: Continuous Q&A session for deep invoice analysis

## Architecture

```
Invoice Image → OCR (Mistral) → Text Extraction
                                      ↓
                            JSON Conversion (Mistral)
                                      ↓
                            Structured Data
                                      ↓
                        Chat Analysis (Gemini + CrewAI)
```

## Prerequisites

- Python 3.8+
- Mistral API key
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd vision-ocr-agent
```

2. Install required dependencies:
```bash
pip install python-dotenv mistralai pillow crewai google-generativeai
```

3. Create a `.env` file with your API keys:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

### Basic Usage

Run the Jupyter notebook `main.ipynb` or execute the pipeline programmatically:

```python
from invoice_processor import process_invoice, chat_with_invoice

# Process an invoice
invoice_data = process_invoice("path/to/invoice.jpg")

# Ask questions about the invoice
answer = chat_with_invoice(invoice_data, "What is the total amount?")
print(answer)
```

### Example Questions

The system can answer various questions about your invoices:

- "What is the total amount of this invoice?"
- "Who is the vendor?"
- "List all the items in the invoice"
- "When was this invoice issued?"
- "Calculate the tax percentage"

### Interactive Mode

For a continuous Q&A session:

```python
interactive_chat(invoice_data)
```

Type your questions and get instant answers. Type 'exit', 'quit', or 'q' to end the session.

## Project Structure

```
vision-ocr-agent/
│
├── main.ipynb              # Main Jupyter notebook
├── .env                    # API keys (not tracked)
├── sample_invoice_2.webp   # Sample invoice image
└── README.md              # This file
```

## Extracted Data Fields

The system extracts and structures the following invoice information:

- **Invoice Details**: Number, date
- **Vendor Information**: Name, address, VAT number
- **Customer Information**: Name, address
- **Line Items**: Description, quantity, unit price, total
- **Financial Summary**: Subtotal, tax, total amount, currency

## Technologies Used

- **Mistral AI**: OCR and text-to-JSON conversion
  - `pixtral-large-latest`: Vision model for OCR
  - `mistral-small-latest`: Language model for structured data extraction
- **Google Gemini**: Conversational AI for invoice analysis
  - `gemini-2.0-flash-exp`: Fast, efficient language model
- **CrewAI**: Agent framework for orchestrating AI tasks
- **PIL (Pillow)**: Image processing

## API Models

### Mistral AI
- **OCR Model**: `pixtral-large-latest` - Specialized for vision tasks and text extraction
- **Conversion Model**: `mistral-small-latest` - Efficient for structured data generation

### Google Gemini
- **Chat Model**: `gemini-2.0-flash-exp` - Optimized for conversational interactions

## Error Handling

The system includes comprehensive error handling for:
- Missing or invalid image files
- API failures
- JSON parsing errors
- Invalid invoice formats

## Limitations

- Requires valid API keys for both Mistral and Gemini
- Performance depends on image quality
- Best results with clear, high-resolution invoice images
- English language invoices recommended for optimal accuracy

## Future Enhancements

- [ ] Support for multi-page invoices
- [ ] Batch processing capabilities
- [ ] Export to various formats (CSV, Excel, PDF)
- [ ] Custom field extraction templates
- [ ] Multi-language support
- [ ] Invoice validation rules
- [ ] Database integration for invoice storage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/Labellerr/Hands-On-Learning-in-Computer-Vision).

## Acknowledgments

- Mistral AI for powerful OCR capabilities
- Google for Gemini AI
- CrewAI for the agent framework
- Labellerr for project inspiration

---

**Note**: Ensure you have valid API keys and sufficient API credits before running the application. Some API calls may incur costs based on your provider's pricing structure.