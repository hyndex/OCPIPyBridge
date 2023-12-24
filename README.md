# OCPIPyBridge: A Python Library for OCPI Protocol

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/hyndex/OCPIPyBridge)
[![Made with Love](https://img.shields.io/badge/made%20with-love-ff69b4)](https://github.com/hyndex/OCPIPyBridge)
[![Electric Vehicle](https://img.shields.io/badge/electric-vehicle-blue)](https://github.com/hyndex/OCPIPyBridge)
[![Eco Friendly](https://img.shields.io/badge/eco-friendly-green)](https://github.com/hyndex/OCPIPyBridge)
[![Tree](https://img.shields.io/badge/tree-%F0%9F%8C%B3-green)](https://github.com/hyndex/OCPIPyBridge)

## Overview

`OCPIPyBridge` is a Python library tailored for implementing the Open Charge Point Interface (OCPI) protocol. It offers structured models and validation for various OCPI entities, ideal for developers creating applications for EV charging infrastructure and services.

## Features

- Models for key OCPI entities: `Location`, `EVSE`, `Connector`, `CDR`, `Command`, `Transaction`, `Feedback`, `Meter`, `Reservation`, `Tariff`, `User`, and `Credentials`.
- Validations align with OCPI standards using Pydantic.
- Supports diverse OCPI operations and functionalities.

## Installation

Install `OCPIPyBridge` using pip:

```bash
pip install OCPIPyBridge
```

## Usage

Import the required models from `OCPIPyBridge`:

```python
from ocpi_py_bridge.models import Location, EVSE, Connector, CDR, Command, Transaction, Feedback, Meter, Reservation, Tariff, User, Credentials
```

### Model Usage Examples

Example of how to instantiate and use each model:

#### Location

```python
from ocpi_py_bridge.models import Location

location_data = {
    "id": "loc1",
    "type": "ON_STREET",
    "name": "Main Street Charging Station",
    # ... other location details ...
}

location = Location(**location_data)
print(location.json())
```

... (Similar examples for other models)

## Integration with Flask/FastAPI

### Flask Example

```python
from flask import Flask, request, jsonify
from ocpi_py_bridge.models import CDR

app = Flask(__name__)

@app.route('/api/cdr', methods=['POST'])
def handle_cdr():
    try:
        cdr_data = request.json
        cdr = CDR(**cdr_data)
        # Process and save CDR data
        return jsonify({"message": "CDR data processed successfully."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI Example

```python
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from ocpi_py_bridge.models import CDR

app = FastAPI()

@app.post('/api/cdr')
async def handle_cdr(cdr_data: CDR):
    try:
        cdr_data.validate()
        # Process and save CDR data
        return {"message": "CDR data processed successfully."}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

```

## Contributing

To contribute to `OCPIPyBridge`:

1. Fork the repository.
2. Create a new feature branch.
3. Develop your feature or fix.
4. Update tests and documentation as needed.
5. Commit and push changes.
6. Open a pull request.

## Author

- Medium: [dikibhuyan](https://medium.com/@dikibhuyan)
- LinkedIn: [Chinmoy Bhuyan](https://www.linkedin.com/in/chinmoy-bhuyan-785b73ba/)

## License

`OCPIPyBridge` is under the MIT License. See the [LICENSE](LICENSE.md) file for details.
