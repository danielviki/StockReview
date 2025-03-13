# Contributing to Stock Review

First off, thank you for considering contributing to Stock Review! It's people like you that make Stock Review such a great tool.

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Request Process

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.

## Getting Started

1. Clone the repo:
```bash
git clone https://github.com/yourusername/StockReview.git
cd StockReview
```

2. Set up development environment:
```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

## Development Workflow

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and test them:
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

3. Commit your changes:
```bash
git add .
git commit -m "Add your commit message"
```

## Code Style

### Python (Backend)
- Follow PEP 8 style guide
- Use type hints
- Add docstrings for functions and classes
- Keep functions focused and small

Example:
```python
from typing import Optional

def process_data(data: dict, start_date: Optional[str] = None) -> dict:
    """
    Process stock data with optional date filtering.

    Args:
        data (dict): Raw stock data
        start_date (str, optional): Start date for filtering

    Returns:
        dict: Processed stock data
    """
    # Implementation
```

### TypeScript (Frontend)
- Use functional components with hooks
- Type all props and state
- Use meaningful variable names
- Add comments for complex logic

Example:
```typescript
interface ChartProps {
  symbol: string;
  interval: '1d' | '1w' | '1m' | '1y';
}

const Chart: React.FC<ChartProps> = ({ symbol, interval }) => {
  // Implementation
};
```

## Reporting Bugs

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/StockReview/issues/new).

### Bug Report Template
```markdown
**Description:**
A clear description of what the bug is.

**To Reproduce:**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior:**
What you expected to happen.

**Screenshots:**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g. macOS]
 - Browser: [e.g. chrome, safari]
 - Version: [e.g. 22]
```

## Feature Requests

We love to hear new ideas. Feel free to request features by creating an issue with the tag 'enhancement'.

### Feature Request Template
```markdown
**Problem:**
A clear description of what the problem is.

**Proposed Solution:**
A clear description of what you want to happen.

**Alternatives:**
Any alternative solutions or features you've considered.

**Additional Context:**
Add any other context about the feature request here.
```

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Questions?

Feel free to contact the project maintainers if you have any questions.

---

Remember: The best way to contribute is to lead by example! 🚀