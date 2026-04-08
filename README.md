# basic-python-project

Proyecto Python básico pensado como punto de partida para practicar una CI sencilla con GitHub Actions.

## Estructura

```text
basic-python-project/
	README.md
	src/app.py
	test/test_app.py
```

## Requisitos

- Python 3.10+

## Ejecutar en local

Ejecutar tests:

```bash
python -m unittest discover -s test -p "test_*.py"
```

Ejecutar la aplicación:

```bash
python src/app.py
```

Salida esperada:

```text
Hello world!
```

## Idea de CI basica

Para un workflow inicial de GitHub Actions, puedes empezar con estos pasos:

1. Checkout del repositorio.
2. Setup de Python 3.11.
3. Ejecutar tests con `python -m unittest discover -s test -p "test_*.py"`.
