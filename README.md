# Unalengua API

unalengua is a free and unlimited python library that implemented Unalengua API. 

## Installation

```bash
pip install unalengua
```

## Usage

```python
from unalengua import Unalengua

unalengua = Unalengua(lang='Spanish')
print(unalengua.translate('Hola mundo!'))
```

For get all languages supported by Unalengua API, you can use the following code:

```python

from unalengua import show_languages

print(show_languages())
```